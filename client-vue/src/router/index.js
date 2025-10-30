import { createRouter, createWebHistory } from "vue-router";
import { HomeView, LoginView, RegisterView, ForgotPasswordView, ResetPasswordView, ProfileView, PostDetailView } from "@/views";

import store from "@/store";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/forgot-password",
      name: "forgot-password",
      component: ForgotPasswordView,
    },
    {
      path: "/reset-password",
      name: "reset-password",
      component: ResetPasswordView,
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/posts/:id",
      name: "post-detail",
      component: PostDetailView,
      meta: {
        requiresAuth: true,
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  // Check if user is authenticated by looking at both store and localStorage
  const storeTokens = store.state.authentication.tokens;
  const localTokens = localStorage.getItem("tokens");
  const isAuthenticated = !!(storeTokens || localTokens);

  // If user is authenticated and trying to access login/register, redirect to home
  if ((to.name === "login" || to.name === "register") && isAuthenticated) {
    return next({ name: "home" });
  }

  // If route requires authentication and user is not authenticated, redirect to login
  if (to.meta.requiresAuth && !isAuthenticated) {
    return next({ name: "login" });
  }

  next();
});

export default router;
