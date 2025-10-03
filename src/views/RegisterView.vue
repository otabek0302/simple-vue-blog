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
          <Input v-model="email" type="email" label="Email" placeholder="Email" autocomplete="email" />
          <Input v-model="password" type="password" label="Password" placeholder="Password" autocomplete="new-password" />
          <Input v-model="confirmPassword" type="password" label="Confirm Password" placeholder="Confirm Password" autocomplete="new-password" />
          <Button variant="outline" type="submit" :disabled="!email || !password || !confirmPassword" class="register-view__form-footer-button"> Register </Button>
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

<script setup>
import { ref } from "vue";

const email = ref("");
const password = ref("");
const confirmPassword = ref("");

const handleRegister = () => {
  console.log("Register with:", email.value, password.value, confirmPassword.value);
};
</script>
