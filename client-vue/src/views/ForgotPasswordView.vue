<style scoped>
.forgot-password-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 154px);
}
.forgot-password-view__container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}
.forgot-password-view__content {
  width: 100%;
  max-width: 480px;
  padding: 0 16px;
  margin: 0 auto;
}

.forgot-password-view__form {
  width: 100%;
  padding: 32px;
  border: 1px solid #e0e0e0;
  border-radius: 16px;
}

.forgot-password-view__form-header {
  padding: 16px 0;
}

.forgot-password-view__form-body {
  margin: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.forgot-password-view__form-footer {
  display: flex;
  justify-content: center;
  align-items: center;
}

.forgot-password-view__form-footer-button {
  width: 100%;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.25;
}

.forgot-password-view__form-links {
  margin-top: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.forgot-password-view__form-link {
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
  text-decoration: none;
  color: #0057ff;
}

.forgot-password-view__form-link:hover {
  color: #0041cc;
}

.forgot-password-view__form-link-separator {
  color: #0057ff;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
}
</style>

<template>
  <section class="forgot-password-view">
    <div class="forgot-password-view__container">
      <div class="forgot-password-view__content">
        <form name="forgot-password-form" @submit.prevent="handleForgotPassword" class="forgot-password-view__form">
          <div class="forgot-password-view__form-header">
            <Text type="h3" variant="primary" weight="bold" align="center" transform="uppercase">Forgot Password</Text>
          </div>
          <div class="forgot-password-view__form-body">
            <Input v-model="email" type="email" label="Email" placeholder="Email" autocomplete="email" />
          </div>
          <div class="forgot-password-view__form-footer">
            <Button variant="outline" type="submit" :disabled="!email" class="forgot-password-view__form-footer-button"> Forgot Password </Button>
          </div>
          <div class="forgot-password-view__form-links">
            <RouterLink :to="{ name: 'login' }" class="forgot-password-view__form-link"> Login </RouterLink>
            <span class="forgot-password-view__form-link-separator">|</span>
            <RouterLink :to="{ name: 'register' }" class="forgot-password-view__form-link"> Register </RouterLink>
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
      toast,
    };
  },
  methods: {
    async handleForgotPassword() {
      if (!this.email) {
        toast.error("Please fill in all fields");
        return;
      }

      try {
        const { success, message } = await this.$store.dispatch("authentication/forgotPassword", {
          email: this.email,
        });

        if (success) {
          toast.success(message || "Forgot password successful!");
          setTimeout(() => {
            this.$router.push({ name: "login" });
          }, 3000);
        } else {
          toast.error(message || "Forgot password failed!");
        }
      } catch (err) {
        toast.error(err.response?.data?.message || "Unexpected error");
      }
    },
  },
};
</script>
