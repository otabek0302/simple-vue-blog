<style scoped>
.reset-password-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 154px);
}
.reset-password-view__container {
  width: 100%;
  max-width: 480px;
  padding: 0 16px;
}

.reset-password-view__form {
  width: 100%;
  padding: 32px;
  border: 1px solid #e0e0e0;
  border-radius: 16px;
}

.reset-password-view__form-header {
  padding: 16px 0;
}

.reset-password-view__form-body {
  margin: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.reset-password-view__form-footer {
  display: flex;
  justify-content: center;
  align-items: center;
}

.reset-password-view__form-footer-button {
  width: 100%;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.25;
}

.reset-password-view__form-links {
  margin-top: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.reset-password-view__form-link {
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
  text-decoration: none;
  color: #0057ff;
}

.reset-password-view__form-link:hover {
  color: #0041cc;
}

.reset-password-view__form-link-separator {
  color: #0057ff;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
}
</style>

<template>
  <section class="reset-password-view">
    <div class="reset-password-view__container">
      <form name="reset-password-form" @submit.prevent="handleResetPassword" class="reset-password-view__form">
        <div class="reset-password-view__form-header">
          <Text type="h3" variant="primary" weight="bold" align="center" transform="uppercase">Reset Password</Text>
        </div>
        <div class="reset-password-view__form-body">
          <Input v-model="password" type="password" label="New Password" placeholder="New Password" autocomplete="new-password" />
          <Input v-model="confirmPassword" type="password" label="Confirm Password" placeholder="Confirm Password" autocomplete="new-password" />
        </div>
        <div class="reset-password-view__form-footer">
          <Button variant="outline" type="submit" :disabled="!password || !confirmPassword" class="reset-password-view__form-footer-button"> Reset Password </Button>
        </div>
        <div class="reset-password-view__form-links">
          <RouterLink :to="{ name: 'login' }" class="reset-password-view__form-link"> Login </RouterLink>
          <span class="reset-password-view__form-link-separator">|</span>
          <RouterLink :to="{ name: 'register' }" class="reset-password-view__form-link"> Register </RouterLink>
        </div>
      </form>
    </div>
  </section>
</template>

<script>
import { toast } from "vue-sonner";

export default {
  data() {
    return {
      password: "",
      confirmPassword: "",
      token: "",
      toast,
    };
  },
  mounted() {
    this.token = this.$route.query.token;
  },
  methods: {
    async handleResetPassword() {
      if (!this.password || !this.confirmPassword) {
        toast.error("Please fill in all fields");
        return;
      }

      if (this.password !== this.confirmPassword) {
        toast.error("Passwords do not match");
        return;
      }

      try {
        const { success, message } = await this.$store.dispatch("authentication/resetPassword", {
          token: this.token,
          password: this.password,
        });

        if (success) {
          toast.success(message || "Password reset successful!");
          setTimeout(() => {
            this.$router.push({ name: "login" });
          }, 3000);
        } else {
          toast.error(message || "Password reset failed!");
        }
      } catch (err) {
        toast.error(err.response?.data?.message || "Unexpected error");
      }
    },
  },
};
</script>