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
  max-width: 240px;
  width: 100%;
}

.header-view__logo-link {
  width: 60px;
  height: 60px;
  display: block;
  cursor: pointer;
}

.header-view__logo-link img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.header-view__search {
  width: 100%;
  max-width: 480px;
}
.header-view__search .form-float {
  margin-bottom: 0;
}

:deep(.header-view__search .form-float input) {
  padding: 8px 12px;
  border-radius: 8px;
}

.header-view__user {
  max-width: 240px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: end;
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
  text-decoration: none;
  cursor: pointer;
}
.header-view__user-name:hover {
  color: #0057ff;
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
      <div class="header-view__search">
        <Input
          v-model="search"
          type="text"
          placeholder="Search posts..."
          @keyup.enter="onSearch"
          @input="onSearchInput"
        />
      </div>
      <div class="header-view__user">
        <template v-if="isAuthenticated">
          <RouterLink :to="{ name: 'profile' }" class="header-view__user-name">Welcome, {{ user?.username || user?.email || "User" }}</RouterLink>
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

import Input from "@/components/ui/Input.vue";  

export default {
  components: {
    Input,
  },
  data() {
    return {
      search: "",
      searchTimeout: null,
    };
  },
  computed: {
    ...mapGetters("authentication", {
      isAuthenticated: gettersTypes.IS_AUTHENTICATED,
      user: gettersTypes.USER,
    }),
  },
  watch: {
    "$route.query.search"(newVal) {
      if (newVal !== this.search) {
        this.search = newVal || "";
      }
    },
  },
  mounted() {
    // Sync search with URL query
    const searchParam = this.$route.query.search;
    if (searchParam) {
      this.search = searchParam;
    }
  },
  methods: {
    handleLogout() {
      this.$store.dispatch("authentication/logout");
      this.$router.push({ name: "login" });
    },
    onSearchInput() {
      // Debounce search
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.onSearch();
      }, 500);
    },
    onSearch() {
      // Navigate to home with search query
      if (this.$route.name !== "home") {
        this.$router.push({ name: "home", query: { search: this.search.trim() } });
      } else {
        // If already on home, just update query
        if (this.search.trim()) {
          this.$router.push({ query: { ...this.$route.query, search: this.search.trim() } });
        } else {
          const { search, ...rest } = this.$route.query;
          this.$router.push({ query: rest });
        }
      }
    },
  },
};
</script>
