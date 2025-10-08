<style scoped></style>

<template>
  <div id="app">
    <Header />
    <RouterView />
    <Footer />
    <Toaster position="top-right" :duration="3000" rich-colors :close-button="true" />
  </div>
</template>

<script>
import { RouterView } from "vue-router";
import { Toaster } from "vue-sonner";

export default {
  components: {
    RouterView,
    Toaster,
  },
};
</script>
