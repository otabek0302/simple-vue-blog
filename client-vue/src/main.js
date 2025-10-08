import { createApp } from "vue";
import { Toaster } from "vue-sonner";
import App from "./App.vue";
import router from "./router";
import components from "@/components";
import store from "@/store";

import 'vue-sonner/style.css'
const app = createApp(App);

app.use(components);
app.component("Toaster", Toaster);
app.use(router);
app.use(store);

store.dispatch("authentication/initializeAuth");

app.mount("#app");
