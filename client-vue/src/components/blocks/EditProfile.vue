<style scoped>
.edit-profile__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.edit-profile__form__footer {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
}
</style>

<template>
  <Modal v-model="open" title="Edit Profile">
    <div class="edit-profile__form">
      <Input v-model="form.username" label="Username" placeholder="Username" autocomplete="username" />
      <Input v-model="form.email" type="email" label="Email" placeholder="Email" autocomplete="email" />
    </div>
    <template #footer>
      <div class="edit-profile__form__footer">
        <Button variant="secondary" @click="cancel">Cancel</Button>
        <Button variant="primary" @click="save">Save</Button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "@/components/ui/Modal.vue";
import Button from "@/components/ui/Button.vue";
import Input from "@/components/ui/Input.vue";

export default {
  name: "EditProfile",
  components: { Modal, Button, Input },
  props: {
    modelValue: {
      type: Boolean,
      default: false,
    },
    user: {
      type: Object,
      default: () => ({}),
    },
  },
  emits: ["update:modelValue", "save"],
  data() {
    return {
      form: {
        username: this.user?.username || "",
        email: this.user?.email || "",
      },
    };
  },
  computed: {
    open: {
      get() {
        return this.modelValue;
      },
      set(v) {
        this.$emit("update:modelValue", v);
      },
    },
  },
  methods: {
    cancel() {
      this.open = false;
    },
    save() {
      this.$emit("save", { ...this.form });
      this.open = false;
    },
  },
};
</script>


