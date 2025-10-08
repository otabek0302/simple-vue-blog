<style scoped>
.header-view {
  padding: 8px 0;
}

.header-view__container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
  border-bottom: 1px solid #e0e0e0;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-view__logo {
  width: 60px;
  height: 60px;
}

.header-view__logo-link {
  width: 100%;
  height: 100%;
  display: block;
  cursor: pointer;
}

.header-view__logo-link img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.header-view__user {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.header-view__user-link {
  text-decoration: none;
  color: #010101;
  cursor: pointer;
}

.header-view__user-link:hover {
  color: #0057ff;
}

.header-view__user-name {
  color: #010101;
  font-weight: 500;
}

.header-view__user-link {
  background: none;
  border: none;
  cursor: pointer;
  font-size: inherit;
  font-family: inherit;
}
</style>

<template>
  <header class="header-view">
    <div class="header-view__container">
      <div class="header-view__logo">
        <RouterLink :to="{ name: 'home' }" class="header-view__logo-link">
          <img src="@/assets/images/logo.png" alt="logo" />
        </RouterLink>
      </div>
      <div class="header-view__user">
        <template v-if="isAuthenticated">
          <span class="header-view__user-name">Welcome, {{ user?.username || user?.email || "User" }}</span>
          <button @click="handleLogout" class="header-view__user-link">Logout</button>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'login' }" class="header-view__user-link">Login</RouterLink>
          <RouterLink :to="{ name: 'register' }" class="header-view__user-link">Register</RouterLink>
        </template>
      </div>
    </div>
  </header>
</template>

<script>
import { gettersTypes } from "@/modules/types";
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("authentication", {
      isAuthenticated: gettersTypes.IS_AUTHENTICATED,
      user: gettersTypes.USER,
    }),
  },
  methods: {
    handleLogout() {
      this.$store.dispatch("authentication/logout");
      this.$router.push({ name: "login" });
    },
  },
};
</script>
