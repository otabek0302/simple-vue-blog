<style scoped>
.add-comment__form { display: flex; flex-direction: column; gap: 16px; }
.add-comment__textarea { width: 100%; min-height: 100px; padding: 12px; border: 1px solid #e0e0e0; border-radius: 10px; }
.add-comment__footer { display: flex; gap: 16px; justify-content: flex-end; }
</style>

<template>
  <Modal v-model="open" title="Add Comment" width="560px">
    <div class="add-comment__form">
      <textarea v-model="comment" class="add-comment__textarea" placeholder="Write a comment..."></textarea>
    </div>
    <template #footer>
      <div class="add-comment__footer">
        <Button variant="secondary" @click="cancel">Cancel</Button>
        <Button variant="primary" @click="save" :disabled="!comment.trim()">Add</Button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "@/components/ui/Modal.vue";
import Button from "@/components/ui/Button.vue";

export default {
  name: "AddComment",
  components: { Modal, Button },
  props: { modelValue: { type: Boolean, default: false }, postId: { type: Number, required: true } },
  emits: ["update:modelValue", "save"],
  data() { return { comment: "" }; },
  computed: {
    open: {
      get() {
        return this.modelValue;
      },
      set(v) {
        this.$emit("update:modelValue", v);
        if (!v) {
          // Reset comment when modal closes
          this.comment = "";
        }
      },
    },
  },
  watch: {
    modelValue(newVal) {
      if (!newVal) {
        // Reset comment when modal closes
        this.comment = "";
      }
    },
  },
  methods: {
    cancel() {
      this.open = false;
    },
    save() {
      if (!this.comment.trim()) return;
      this.$emit("save", { postId: this.postId, comment: this.comment.trim() });
      this.open = false;
    },
  },
};
</script>


