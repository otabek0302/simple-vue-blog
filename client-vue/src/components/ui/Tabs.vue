<style scoped>
.tabs {
  width: 100%;
}

.tabs__nav {
  display: flex;
  gap: 8px;
  border-bottom: 1px solid #e0e0e0;
  margin-bottom: 12px;
}

.tabs__button {
  padding: 8px 12px;
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  font-size: 14px;
}

.tabs__button--active {
  color: #0057ff;
  border-bottom-color: #0057ff;
}

.tabs__panel {
  padding: 8px 0;
}
</style>

<template>
  <div class="tabs">
    <nav class="tabs__nav">
      <button
        v-for="(tab, index) in tabs"
        :key="index"
        type="button"
        class="tabs__button"
        :class="{ 'tabs__button--active': activeIndex === index }"
        @click="setActive(index)"
      >
        {{ tab }}
      </button>
    </nav>

    <section class="tabs__panel">
      <slot :name="`tab-${activeIndex + 1}`" />
    </section>
  </div>
</template>

<script>
export default {
  name: "Tabs",
  props: {
    tabs: {
      type: Array,
      required: true,
      validator: (value) => value.every((t) => typeof t === 'string' && t.length > 0),
    },
    modelValue: {
      type: Number,
      default: null,
    },
  },
  emits: ["update:modelValue", "change"],
  data() {
    return {
      activeInternal: 0,
    };
  },
  computed: {
    isControlled() {
      return this.modelValue !== null && this.modelValue !== undefined;
    },
    activeIndex() {
      const value = this.isControlled ? this.modelValue : this.activeInternal;
      if (value < 0 || value >= this.tabs.length) return 0;
      return value;
    },
  },
  methods: {
    setActive(index) {
      if (this.isControlled) {
        this.$emit("update:modelValue", index);
      } else {
        this.activeInternal = index;
      }
      this.$emit("change", index);
    },
  },
};
</script>
