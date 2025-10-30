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
    updateProfile: async (payload) => {
        // expected payload: { username?, email? }
        const { data } = await api.put("/update-profile/", payload);
        return data;
    },
    changePassword: async (payload) => {
        // expected payload: { currentPassword?, password }
        const { data } = await api.post("/change-password/", payload);
        return data;
    },
    updateAvatar: async (file) => {
        const form = new FormData();
        form.append("avatar", file);
        const { data } = await api.post("/update-avatar/", form, {
            headers: { "Content-Type": "multipart/form-data" },
        });
        return data;
    },
    removeAvatar: async () => {
        const form = new FormData();
        form.append("remove", "true");
        const { data } = await api.post("/update-avatar/", form);
        return data;
    },
}

export default AuthenticationService;