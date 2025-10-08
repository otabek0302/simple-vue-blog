import api from "./axios";

const AuthenticationService = {
    register: async (payload) => {
        const { data } = await api.post("/register/", payload);
        return data;
    },
    login: async (payload) => {
        const { data } = await api.post("/login/", payload);
        return data;
    },
    forgotPassword: async (payload) => {
        const { data } = await api.post("/forgot-password/", payload);
        return data;
    },
    resetPassword: async (payload) => {
        const { data } = await api.post("/reset-password/", payload);
        return data;
    },
}

export default AuthenticationService;