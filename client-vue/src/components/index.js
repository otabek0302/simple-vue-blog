import Header from "@/components/layout/Header.vue";
import Footer from "@/components/layout/Footer.vue";
import Input from "@/components/ui/Input.vue";
import Button from "@/components/ui/Button.vue";
import Text from "@/components/ui/Text.vue";
import Modal from "@/components/ui/Modal.vue";
import Tabs from "@/components/ui/Tabs.vue";
import Card from "@/components/ui/Card.vue";
import Post from "@/components/blocks/Post.vue";
import EditProfile from "@/components/blocks/EditProfile.vue";
import EditPassword from "@/components/blocks/EditPassword.vue";

export default {
  install(app) {
    app.component("Header", Header);
    app.component("Footer", Footer);
    app.component("Input", Input);
    app.component("Button", Button);
    app.component("Text", Text);
    app.component("Modal", Modal);
    app.component("Tabs", Tabs);
    app.component("Card", Card);
    app.component("Post", Post);
    app.component("EditProfile", EditProfile);
    app.component("EditPassword", EditPassword);
  },
};
