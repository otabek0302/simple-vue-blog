<style scoped>
.form-float {
  position: relative;
  margin-bottom: 16px;
}

.form-float label {
  position: absolute;
  top: 12px;
  left: 12px;
  transform: translateY(15%);
  pointer-events: none;
  transition: all 0.3s ease;
  color: #666;
  font-size: 14px;
  background: white;
  width: 50%;
  padding: 0 4px;
}

.form-float input,
.form-float textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  outline: none;
  font-size: 16px;
  transition: all 0.3s ease;
  background: white;
  font-family: inherit;
  resize: vertical;
}

.form-float textarea {
  min-height: 120px;
  line-height: 1.5;
}

.form-float input:focus,
.form-float textarea:focus {
  border-color: #0057ff;
  box-shadow: 0 0 0 3px rgba(0, 87, 255, 0.1);
}

.form-float input:focus + label,
.form-float input:not(:placeholder-shown) + label,
.form-float textarea:focus + label,
.form-float textarea:not(:placeholder-shown) + label {
  top: -24px;
  left: 8px;
  font-size: 12px;
  color: #0057ff;
}

.form-float__label--error {
  color: #dc3545 !important;
}

.form-float__error {
  display: block;
  color: #dc3545;
  font-size: 12px;
  margin-top: 4px;
  min-height: 14px;
}

.form-float--error input,
.form-float--error textarea {
  border-color: #dc3545;
}

.form-float--error input:focus,
.form-float--error textarea:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1);
}

.form-float__error--error {
  display: block;
  font-size: 12px;
  color: #dc3545;
}
</style>

<template>
  <div class="form-float" :class="[divClass, { 'form-float--error': error }]">
    <input
      v-if="type !== 'textarea'"
      :id="inputId"
      :type="type"
      :placeholder="placeholder"
      :value="modelValue"
      :disabled="disabled"
      :required="required"
      :autocomplete="autocomplete"
      :class="[inputClass, { 'form-float__input--error': error }]"
      @input="$emit('update:model-value', $event.target.value)"
      @focus="$emit('focus', $event)"
      @blur="$emit('blur', $event)"
    />
    <textarea
      v-else
      :id="inputId"
      :placeholder="placeholder"
      :value="modelValue"
      :disabled="disabled"
      :required="required"
      :class="[inputClass, { 'form-float__input--error': error }]"
      @input="$emit('update:model-value', $event.target.value)"
      @focus="$emit('focus', $event)"
      @blur="$emit('blur', $event)"
    ></textarea>
    <label v-if="label" :for="inputId" :class="[labelClass, { 'form-float__label--error': error }]">{{ label }}</label>
    <span v-if="error" :class="[errorClass, { 'form-float__error--error': error }]">{{ error }}</span>
  </div>
</template>

<script>
export default {
  name: "Input",
  props: {
    label: {
      type: String,
      required: false,
      default: "",
    },
    modelValue: {
      type: [String, Number],
      default: "",
    },
    type: {
      type: String,
      default: "text",
      validator: (value) => ["text", "email", "password", "number", "tel", "url", "textarea", ""].includes(value),
    },
    placeholder: {
      type: String,
      default: "",
    },
    error: {
      type: String,
      default: "",
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    required: {
      type: Boolean,
      default: false,
    },
    divClass: {
      type: String,
      default: "",
    },
    inputClass: {
      type: String,
      default: "",
    },
    labelClass: {
      type: String,
      default: "",
    },
    errorClass: {
      type: String,
      default: "",
    },
    autocomplete: {
      type: String,
      default: "",
    },
  },
  emits: ["update:model-value", "focus", "blur"],
  computed: {
    inputId() {
      return `input-${Math.random().toString(36).substr(2, 9)}`;
    },
  },
};
</script>
