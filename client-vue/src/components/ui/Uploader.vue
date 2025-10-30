<style scoped>
.uploader {
  position: relative;
  display: inline-block;
}
.uploader__preview {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  border: 3px solid #fafafa;
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}
.uploader__preview img {
  width: 90%;
  height: 90%;
  object-fit: contain;
}
.uploader__actions {
  position: absolute;
  right: 8px;
  bottom: 8px;
  display: flex;
  z-index: 10000;
  gap: 6px;
}
.uploader__btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  background: #0057ff;
  color: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.uploader__btn--remove {
  background: #dc3545;
}
.uploader__file-input { display: none; }

</style>

<template>
  <div class="uploader">
    <div class="uploader__preview">
      <img v-if="currentSrc" :src="currentSrc" alt="preview" />
      <slot v-else />
    </div>
    <div class="uploader__actions">
      <button class="uploader__btn" type="button" @click="triggerSelect" title="Change">
        <i class="fas fa-pen"></i>
      </button>
      <button v-if="canRemove" class="uploader__btn uploader__btn--remove" type="button" @click="$emit('remove')" title="Remove">
        <i class="fas fa-trash"></i>
      </button>
    </div>
    <input ref="fileInput" class="uploader__file-input" type="file" accept="image/*" @change="onSelect" />
  </div>
</template>

<script>
export default {
  name: "Uploader",
  props: {
    src: { type: String, default: "" },
    backendBase: { type: String, default: "http://localhost:8000" },
    canRemove: { type: Boolean, default: true },
  },
  emits: ["select", "remove"],
  data() {
    return { previewUrl: "" };
  },
  watch: {
    src(val) {
      this.previewUrl = "";
    },
  },
  computed: {
    normalizedSrc() {
      if (!this.src) return "";
      if (this.src.startsWith("http://") || this.src.startsWith("https://")) return this.src;
      return `${this.backendBase}${this.src}`;
    },
    currentSrc() {
      return this.previewUrl || this.normalizedSrc;
    },
  },
  methods: {
    triggerSelect() {
      this.$refs.fileInput?.click();
    },
    onSelect(e) {
      const file = e.target.files?.[0];
      if (!file) return;
      const url = URL.createObjectURL(file);
      this.previewUrl = url;
      this.$emit("select", file);
    },
  },
};
</script>


