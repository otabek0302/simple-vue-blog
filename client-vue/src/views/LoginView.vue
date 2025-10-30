<style scoped>
.login-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 154px);
}

.login-view__container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}

.login-view__content {
  width: 100%;
  max-width: 480px;
  padding: 0 16px;
  margin: 0 auto;
  
}

.login-view__form {
  width: 100%;
  padding: 32px;
  border: 1px solid #e0e0e0;
  border-radius: 16px;
}

.login-view__form-header {
  padding: 16px 0;
}

.login-view__form-body {
  margin: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.login-view__form-footer {
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-view__form-footer-button {
  width: 100%;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.25;
}

.login-view__form-links {
  margin-top: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.login-view__form-link {
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
  text-decoration: none;
  color: #0057ff;
}

.login-view__form-link:hover {
  color: #0041cc;
}

.login-view__form-link-separator {
  color: #0057ff;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
}
</style>

<template>
  <section class="login-view">
    <div class="login-view__container">
      <div class="login-view__content">
        <form class="login-view__form" name="login-form" @submit.prevent="handleLogin">
          <div class="login-view__form-header">
            <Text type="h3" variant="primary" weight="bold" align="center" transform="uppercase">Login</Text>
          </div>
          <div class="login-view__form-body">
            <Input v-model="email" type="email" label="Email" placeholder="Email" autocomplete="email" />
            <Input v-model="password" type="password" label="Password" placeholder="Password" autocomplete="current-password" />
          </div>
          <div class="login-view__form-footer">
            <Button variant="outline" type="submit" :disabled="!email || !password" class="login-view__form-footer-button"> Login </Button>
          </div>
          <div class="login-view__form-links">
            <RouterLink :to="{ name: 'forgot-password' }" class="login-view__form-link"> Forgot Password? </RouterLink>
            <span class="login-view__form-link-separator">|</span>
            <RouterLink :to="{ name: 'register' }" class="login-view__form-link"> Create Account </RouterLink>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import { toast } from "vue-sonner";

export default {
  data() {
    return {
      email: "",
      password: "",
      toast,
    };
  },
  methods: {
    async handleLogin() {
      if (!this.email || !this.password) {
        toast.error("Please fill in all fields");
        return;
      }

      try {
        const { success, message } = await this.$store.dispatch("authentication/login", {
          email: this.email,
          password: this.password,
        });

        if (success) {
          toast.success(message || "Login successful!");
          this.$router.push({ name: "home" });
        } else {
          toast.error(message || "Login failed!");
        }
      } catch (err) {
        toast.error(err.response?.data?.message || "Unexpected error");
      }
    },
  },
};
</script>