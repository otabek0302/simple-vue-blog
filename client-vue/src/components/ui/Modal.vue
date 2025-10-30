<style scoped>
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10001;
}

.app-modal {
  background: #fff;
  width: 100%;
  max-width: 560px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  overflow: hidden;
}

.app-modal__header,
.app-modal__footer {
  padding: 12px 16px;
  background: #fafafa;
  border-bottom: 1px solid #eaeaea;
}

.app-modal__footer {
  border-top: 1px solid #eaeaea;
  border-bottom: none;
}

.app-modal__body {
  padding: 32px;
}

.app-modal__title {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.2;
}

.modal-btn {
  padding: 8px 16px;
  border-radius: 10px;
  border: 1px solid #e0e0e0;
  background: #f5f5f5;
  cursor: pointer;
}
</style>

<template>
  <teleport to="#app">
    <div v-if="open" class="modal-backdrop" @click.self="close">
      <section class="app-modal" :style="{ maxWidth: width }">
        <header class="app-modal__header">
          <slot name="header">
            <h3 class="app-modal__title">{{ title }}</h3>
          </slot>
        </header>
        <div class="app-modal__body">
          <slot />
        </div>
        <footer class="app-modal__footer">
          <slot name="footer">
            <Button variant="secondary" class="modal-btn" @click="close">Close</Button>
          </slot>
        </footer>
      </section>
    </div>
  </teleport>
</template>

<script>
import Button from './Button.vue';

export default {
  name: "Modal",
  props: {
    modelValue: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      default: "",
    },
    width: {
      type: String,
      default: "560px",
    },
  },
  emits: ["update:modelValue", "close"],
  computed: {
    open() {
      return this.modelValue;
    },
  },
  methods: {
    close() {
      this.$emit("update:modelValue", false);
      this.$emit("close");
    },
  },
};
</script>