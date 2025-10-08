import Header from "@/components/layout/Header.vue";
import Footer from "@/components/layout/Footer.vue";
import Input from "@/components/ui/Input.vue";
import Button from "@/components/ui/Button.vue";
import Text from "@/components/ui/Text.vue";

export default {
  install(app) {
    app.component("Header", Header);
    app.component("Footer", Footer);
    app.component("Input", Input);
    app.component("Button", Button);
    app.component("Text", Text);
  },
};
