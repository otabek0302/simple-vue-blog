import App from "./App.vue";
import router from "./router";
import components from "@/components";
import { createApp } from "vue";

const app = createApp(App);

app.use(components);
app.use(router);

app.mount("#app");
