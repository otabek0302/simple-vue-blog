<style scoped>
.update-comment__form { display: flex; flex-direction: column; gap: 16px; }
.update-comment__textarea { width: 100%; min-height: 100px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 10px; }
.update-comment__footer { display: flex; gap: 16px; justify-content: flex-end; }
</style>

<template>
  <Modal v-model="open" title="Update Comment" width="560px">
    <div class="update-comment__form">
      <textarea v-model="comment" class="update-comment__textarea" placeholder="Update your comment..."></textarea>
    </div>
    <template #footer>
      <div class="update-comment__footer">
        <Button variant="secondary" @click="cancel">Cancel</Button>
        <Button variant="primary" @click="save" :disabled="!comment.trim()">Save</Button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "@/components/ui/Modal.vue";
import Button from "@/components/ui/Button.vue";

export default {
  name: "UpdateComment",
  components: { Modal, Button },
  props: { modelValue: { type: Boolean, default: false }, commentId: { type: Number, required: true }, initial: { type: String, default: "" } },
  emits: ["update:modelValue", "save"],
  data() { return { comment: this.initial }; },
  computed: { open: { get() { return this.modelValue; }, set(v) { this.$emit("update:modelValue", v); } } },
  methods: {
    cancel() { this.open = false; },
    save() { this.$emit("save", { commentId: this.commentId, comment: this.comment.trim() }); this.open = false; },
  },
};
</script>


