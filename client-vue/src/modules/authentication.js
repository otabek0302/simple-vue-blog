import AuthenticationService from "@/service/authentication";
import { gettersTypes } from "./types";

export default {
    namespaced: true,

    state: {
        user: null,
        tokens: null,
        success: null,
        error: null,
        loading: false,
    },

    getters: {
        [gettersTypes.IS_AUTHENTICATED]: (state) => !!state.tokens,
        [gettersTypes.USER]: (state) => state.user,
    },

    mutations: {
        SET_USER: (state, user) => {
            state.user = user;
            if (user) {
                localStorage.setItem("user", JSON.stringify(user));
            } else {
                localStorage.removeItem("user");
            }
        },
        SET_TOKENS: (state, tokens) => {
            state.tokens = tokens;
            if (tokens) {
                localStorage.setItem("tokens", JSON.stringify(tokens));
            } else {
                localStorage.removeItem("tokens");
            }
        },
        SET_SUCCESS: (state, msg) => (state.success = msg),
        SET_ERROR: (state, msg) => (state.error = msg),
        SET_LOADING: (state, loading) => (state.loading = loading),
        LOGOUT: (state) => {
            state.user = null;
            state.tokens = null;
            localStorage.removeItem("tokens");
            localStorage.removeItem("user");
        },
    },

    actions: {
        async register({ commit }, payload) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.register(payload);
                commit("SET_USER", response.user);
                commit("SET_TOKENS", response.tokens);
                commit("SET_SUCCESS", response.message || "Registration successful");
                return { success: true, message: response.message };
            } catch (err) {
                const message = err.response?.data?.message || "Registration failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async login({ commit }, payload) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.login(payload);
                commit("SET_USER", response.user);
                commit("SET_TOKENS", response.tokens);
                commit("SET_SUCCESS", response.message || "Login successful");
                return { success: true, message: response.message };
            } catch (err) {
                const message = err.response?.data?.message || "Login failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async forgotPassword({ commit }, payload) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.forgotPassword(payload);
                commit("SET_SUCCESS", response.message || "Forgot password successful");
                return { success: true, message: response.message };
            } catch (err) {
                const message = err.response?.data?.message || "Forgot password failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async resetPassword({ commit }, payload) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.resetPassword(payload);
                commit("SET_SUCCESS", response.message || "Reset password successful");
                return { success: true, message: response.message };
            } catch (err) {
                const message = err.response?.data?.message || "Reset password failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async updateProfile({ commit, state }, payload) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.updateProfile(payload);
                const nextUser = response?.user || { ...state.user, ...payload };
                commit("SET_USER", nextUser);
                commit("SET_SUCCESS", response?.message || "Profile updated successfully");
                return { success: true, user: nextUser, message: response?.message };
            } catch (err) {
                const message = err.response?.data?.message || "Update profile failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async changePassword({ commit }, payload) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.changePassword(payload);
                commit("SET_SUCCESS", response?.message || "Password updated successfully");
                return { success: true, message: response?.message };
            } catch (err) {
                const message = err.response?.data?.message || "Update password failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async updateAvatar({ commit }, file) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.updateAvatar(file);
                if (response?.user) {
                    commit("SET_USER", response.user);
                }
                commit("SET_SUCCESS", response?.message || "Avatar updated successfully");
                return { success: true, message: response?.message };
            } catch (err) {
                const message = err.response?.data?.message || "Avatar update failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        async removeAvatar({ commit }) {
            commit("SET_LOADING", true);
            commit("SET_ERROR", null);
            try {
                const response = await AuthenticationService.removeAvatar();
                if (response?.user) {
                    commit("SET_USER", response.user);
                }
                commit("SET_SUCCESS", response?.message || "Avatar removed successfully");
                return { success: true, message: response?.message };
            } catch (err) {
                const message = err.response?.data?.message || "Avatar remove failed";
                commit("SET_ERROR", message);
                return { success: false, message };
            } finally {
                commit("SET_LOADING", false);
            }
        },
        logout({ commit }) {
            commit("LOGOUT");
        },
        initializeAuth({ commit }) {
            const tokens = localStorage.getItem("tokens");
            const user = localStorage.getItem("user");
            
            if (tokens) {
                try {
                    const parsedTokens = JSON.parse(tokens);
                    commit("SET_TOKENS", parsedTokens);
                } catch (error) {
                    localStorage.removeItem("tokens");
                }
            }
            
            if (user) {
                try {
                    const parsedUser = JSON.parse(user);
                    commit("SET_USER", parsedUser);
                } catch (error) {
                    localStorage.removeItem("user");
                }
            }
        },
    }
}