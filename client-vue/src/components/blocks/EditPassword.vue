<style scoped>
.edit-password__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.edit-password__form__footer {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
}
</style>

<template>
  <Modal v-model="open" title="Change Password">
    <div class="edit-password__form">
      <Input v-model="form.password" type="password" label="New Password" placeholder="New Password" autocomplete="new-password" />
      <Input v-model="form.confirmPassword" type="password" label="Confirm Password" placeholder="Confirm Password" autocomplete="new-password" />
    </div>
    <template #footer>
      <div class="edit-password__form__footer">
        <Button variant="secondary" @click="cancel">Cancel</Button>
        <Button variant="primary" @click="save" :disabled="!form.password || form.password !== form.confirmPassword">Save</Button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "@/components/ui/Modal.vue";
import Button from "@/components/ui/Button.vue";
import Input from "@/components/ui/Input.vue";

export default {
  name: "EditPassword",
  components: { Modal, Button, Input },
  props: {
    modelValue: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["update:modelValue", "save"],
  data() {
    return {
      form: {
        password: "",
        confirmPassword: "",
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
      if (!this.form.password || this.form.password !== this.form.confirmPassword) return;
      this.$emit("save", { password: this.form.password });
      this.open = false;
    },
  },
};
</script>


