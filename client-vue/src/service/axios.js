import axios from "axios";
import store from "@/store";

const api = axios.create({
    baseURL: "http://localhost:8000/api/v1",
});

api.interceptors.request.use((config) => {
    const tokens = localStorage.getItem("tokens");
    if (tokens) {
        config.headers.Authorization = `Bearer ${JSON.parse(tokens).access}`;
    }
    // Let the browser set proper multipart boundaries
    if (config.data instanceof FormData) {
        if (config.headers && config.headers["Content-Type"]) {
            delete config.headers["Content-Type"]; 
        }
    } else {
        // Default JSON for non-FormData bodies
        if (config.headers && !config.headers["Content-Type"]) {
            config.headers["Content-Type"] = "application/json";
        }
    }
    return config;
});

export default api;

// Auto-refresh access token on 401 and retry the original request
let isRefreshing = false;
let pendingRequests = [];

function onRefreshed(newAccessToken) {
    pendingRequests.forEach((cb) => cb(newAccessToken));
    pendingRequests = [];
}

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        const status = error.response?.status;

        if (status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            const tokensRaw = localStorage.getItem("tokens");
            if (!tokensRaw) return Promise.reject(error);
            let tokens;
            try {
                tokens = JSON.parse(tokensRaw);
            } catch (_) {
                return Promise.reject(error);
            }

            const refreshToken = tokens?.refresh;
            if (!refreshToken) return Promise.reject(error);

            if (isRefreshing) {
                return new Promise((resolve) => {
                    pendingRequests.push((newAccessToken) => {
                        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                        resolve(api(originalRequest));
                    });
                });
            }

            isRefreshing = true;
            try {
                const { data } = await api.post("/token/refresh/", { refresh: refreshToken });
                const newTokens = { ...tokens, access: data.access };

                // Persist tokens in both store and localStorage
                store.commit("authentication/SET_TOKENS", newTokens);

                onRefreshed(newTokens.access);

                // Update the original request header and retry
                originalRequest.headers.Authorization = `Bearer ${newTokens.access}`;
                return api(originalRequest);
            } catch (refreshErr) {
                // Cleanup and logout if refresh fails
                store.commit("authentication/SET_ERROR", "Session expired. Please sign in again.");
                store.commit("authentication/LOGOUT");
                // redirect to login without importing router
                if (typeof window !== 'undefined') {
                    window.location.href = '/login';
                }
                return Promise.reject(refreshErr);
            } finally {
                isRefreshing = false;
            }
        }

        return Promise.reject(error);
    }
);