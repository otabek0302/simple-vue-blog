<style>
p {
  margin: 0;
  padding: 0;
}
.footer-view {
  padding: 8px 0;
}
.footer-view__container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
  border-top: 1px solid #e0e0e0;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.footer-view__logo-link {
  width: 60px;
  height: 60px;
  display: block;
}

.footer-view__logo-link img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.footer-view__center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-view__center-text {
  font-size: 16px;
  font-weight: 400;
  line-height: 1.25;
}

.footer-view__center-link {
  text-decoration: none;
  color: #010101;
  font-weight: 600;
  line-height: 1.25;
}

.footer-view__center-link:hover {
  color: #0057ff;
}

.footer-view__copyright {
  font-size: 16px;
  font-weight: 400;
  line-height: 1.25;
}
</style>

<template>
  <footer class="footer-view">
    <div class="footer-view__container">
      <div class="footer-view__left">
        <RouterLink :to="{ name: 'home' }" class="footer-view__logo-link">
          <img src="@/assets/images/logo.png" alt="logo" />
        </RouterLink>
      </div>
      <div class="footer-view__center">
        <p class="footer-view__center-text">
          Developed by
          <a href="https://github.com/otabek0302" target="_blank" class="footer-view__center-link">@amonovotabek</a>
        </p>
      </div>
      <div class="footer-view__right">
        <p class="footer-view__copyright">Copyright 2025</p>
      </div>
    </div>
  </footer>
</template>

<script></script>
