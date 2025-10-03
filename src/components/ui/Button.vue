<style scoped>
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 8px 24px;
  border: 1px solid transparent;
  transition: all 0.3s ease;
  border-radius: 10px;
  cursor: pointer;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background-color: #0057ff;
  color: white;
  border-color: #0057ff;
}

.btn-primary:hover:not(:disabled) {
  background-color: #0041cc;
  border-color: #0041cc;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
  border-color: #6c757d;
}

.btn-secondary:hover:not(:disabled) {
  background-color: #545b62;
  border-color: #545b62;
}

.btn-outline {
  background-color: transparent;
  color: #0057ff;
  border-color: #0057ff;
}

.btn-outline:hover:not(:disabled) {
  background-color: #0057ff;
  color: white;
}

.btn-success {
  background-color: #28a745;
  color: white;
  border-color: #28a745;
}

.btn-success:hover:not(:disabled) {
  background-color: #218838;
  border-color: #218838;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
  border-color: #dc3545;
}

.btn-danger:hover:not(:disabled) {
  background-color: #c82333;
  border-color: #c82333;
}

.btn-loading i {
  margin-left: 8px;
}
</style>

<template>
  <button :type="type" :disabled="disabled || loading" :class="classes" @click="$emit('click', $event)">
    <slot></slot>
    <i v-if="loading" class="fas fa-spinner fa-spin"></i>
  </button>
</template>

<script>
export default {
  name: "Button",
  emits: ["click"],
  props: {
    type: {
      type: String,
      default: "button",
      validator: (value) => ["button", "submit", "reset"].includes(value),
    },
    variant: {
      type: String,
      default: "primary",
      validator: (value) => ["primary", "secondary", "outline", "success", "danger"].includes(value),
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    buttonClass: {
      type: String,
      default: "",
    },
  },
  computed: {
    classes() {
      const classes = ["btn"];

      // Add variant class
      classes.push(`btn-${this.variant}`);

      // Add loading class
      if (this.loading) {
        classes.push("btn-loading");
      }

      // Add custom class
      if (this.buttonClass) {
        classes.push(this.buttonClass);
      }

      return classes;
    },
  },
};
</script>
