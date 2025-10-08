<style scoped>
.register-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 154px);
}

.register-view__container {
  width: 100%;
  max-width: 480px;
  padding: 0 16px;
}

.register-view__form {
  width: 100%;
  padding: 32px;
  border: 1px solid #e0e0e0;
  border-radius: 16px;
}

.register-view__form-header {
  padding: 16px 0;
}

.register-view__form-body {
  margin: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.register-view__form-footer {
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-view__form-footer-button {
  width: 100%;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.25;
}

.register-view__form-links {
  margin-top: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.register-view__form-link {
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
  text-decoration: none;
  color: #0057ff;
}

.register-view__form-link:hover {
  color: #0041cc;
}

.register-view__form-link-separator {
  color: #0057ff;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.25;
}
</style>

<template>
  <section class="register-view">
    <div class="register-view__container">
      <form name="register-form" @submit.prevent="handleRegister" class="register-view__form">
        <div class="register-view__form-header">
          <Text type="h3" variant="primary" weight="bold" align="center" transform="uppercase">Register</Text>
        </div>
        <div class="register-view__form-body">
          <Input v-model="username" type="text" label="Username" placeholder="Username" autocomplete="username" :error="errors.username" />
          <Input v-model="email" type="email" label="Email" placeholder="Email" autocomplete="email" :error="errors.email" />
          <Input v-model="password" type="password" label="Password" placeholder="Password" autocomplete="new-password" :error="errors.password" />
          <Input v-model="confirmPassword" type="password" label="Confirm Password" placeholder="Confirm Password" autocomplete="new-password" :error="errors.confirmPassword" />
          <Button variant="outline" type="submit" :disabled="!isFormValid || $store.state.authentication.loading" class="register-view__form-footer-button"> Register </Button>
        </div>
        <div class="register-view__form-links">
          <RouterLink :to="{ name: 'login' }" class="register-view__form-link"> Login </RouterLink>
          <span class="register-view__form-link-separator">|</span>
          <RouterLink :to="{ name: 'forgot-password' }" class="register-view__form-link"> Forgot Password? </RouterLink>
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
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      errors: {
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
      },
      toast,
    };
  },
  computed: {
    isFormValid() {
      return this.username.trim() && this.email.trim() && this.password.trim() && this.confirmPassword.trim();
    },
  },
  methods: {
    validateForm() {
      this.errors = { username: "", email: "", password: "", confirmPassword: "" };

      if (!this.username) this.errors.username = "Username is required";
      if (!this.email) this.errors.email = "Email is required";
      else if (!/\S+@\S+\.\S+/.test(this.email)) this.errors.email = "Invalid email format";

      if (!this.password) this.errors.password = "Password is required";
      if (!this.confirmPassword) this.errors.confirmPassword = "Confirm Password is required";
      else if (this.password !== this.confirmPassword) this.errors.confirmPassword = "Passwords do not match";
    },

    async handleRegister() {
      this.validateForm();

      if (Object.values(this.errors).some((error) => error !== "")) return;

      try {
        const { success, message } = await this.$store.dispatch("authentication/register", {
          username: this.username,
          email: this.email,
          password: this.password,
        });

        if (success) {
          toast.success(message || "Registration successful!");
          setTimeout(() => {
            this.$router.push({ name: "login" });
          }, 3000);
        } else {
          toast.error(message || "Registration failed!");
        }
      } catch (err) {
        toast.error(err.response?.data?.message || "Unexpected error");
      }
    },
  },
};
</script>
