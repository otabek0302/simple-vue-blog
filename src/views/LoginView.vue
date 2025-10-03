<style scoped>
.login-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 154px);
}

.login-view__container {
  width: 100%;
  max-width: 480px;
  padding: 0 16px;
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
      <form class="login-view__form" name="login-form" @submit.prevent="handleLogin">
        <div class="login-view__form-header">
          <Text type="h3" variant="primary" weight="bold" align="center" transform="uppercase">Login</Text>
        </div>
        <div class="login-view__form-body">
          <Input v-model="email" type="email" label="Email" placeholder="Email" autocomplete="email" @blur="onBlur" @focus="onFocus" />
          <Input v-model="password" type="password" label="Password" placeholder="Password" autocomplete="current-password" @blur="onBlur" @focus="onFocus" />
        </div>
        <div class="login-view__form-footer">
          <Button variant="outline" type="submit" :disabled="!email || !password" class="login-view__form-footer-button" > Login </Button>
        </div>
        <div class="login-view__form-links">
          <RouterLink :to="{ name: 'forgot-password' }" class="login-view__form-link"> Forgot Password? </RouterLink>
          <span class="login-view__form-link-separator">|</span>
          <RouterLink :to="{ name: 'register' }" class="login-view__form-link"> Create Account </RouterLink>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const email = ref("");
const password = ref("");

const handleLogin = () => {
  console.log("Login with:", email.value, password.value);
};

const onBlur = () => {
  console.log("Blur");
};

const onFocus = () => {
  console.log("Focus");
};
</script>