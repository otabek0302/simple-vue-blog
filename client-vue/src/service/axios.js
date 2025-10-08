import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api/v1",
    headers: { "Content-Type": "application/json" },
});

api.interceptors.request.use((config) => {
    const tokens = localStorage.getItem("tokens");
    if (tokens) {
        config.headers.Authorization = `Bearer ${JSON.parse(tokens).access}`;
    }
    return config;
});

export default api;