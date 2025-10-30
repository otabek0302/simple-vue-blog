<style scoped>
.update-post__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.update-post__footer {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
}
.dropzone {
  border: 2px dashed #e0e0e0;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  color: #666;
  cursor: pointer;
}
.dropzone--active {
  border-color: #0057ff;
  background: rgba(0, 87, 255, 0.04);
}
.preview {
  position: relative;
  width: 100%;
  height: 200px;
}
.preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
}
.icon-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 1000;

  font-size: 16px;
  color: #dc3545;
  background: transparent;
  border: none;
  cursor: pointer;
}
</style>

<template>
  <Modal v-model="open" title="Update Post" width="640px">
    <div class="update-post__form">
      <Input v-model="form.title" label="Title" placeholder="Post title" />
      <Input v-model="form.content" type="textarea" label="Content" placeholder="Post content" />
      <div class="preview" v-if="currentImage && !removeCurrentImage">
        <img :src="currentImage" alt="current" />
        <button class="icon-btn" title="Delete" @click.stop="clearCurrentImage"><i class="fas fa-trash icon-trash"></i></button>
      </div>
      <div class="dropzone" :class="{ 'dropzone--active': isDragOver }" @dragover.prevent="isDragOver = true" @dragleave.prevent="isDragOver = false" @drop.prevent="onDrop" @click="trigger">
        <template v-if="previewUrl">
          <div class="preview">
            <img :src="previewUrl" alt="preview" />
            <button v-if="previewUrl" class="icon-btn" title="Delete" @click.stop="clearPreviewImage"><i class="fas fa-trash icon-trash"></i></button>
          </div>
        </template>
        <template v-else>
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px">
            <i class="fas fa-upload" style="font-size: 28px; color: #999"></i>
            <div>Drag 'n' drop an image here, or click to select</div>
          </div>
        </template>
        <input ref="file" type="file" accept="image/*" style="display: none" @change="onFileChange" />
      </div>
    </div>
    <template #footer>
      <div class="update-post__footer">
        <Button variant="secondary" @click="cancel">Cancel</Button>
        <Button variant="primary" @click="save" :disabled="!form.title || !form.content">Save</Button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "@/components/ui/Modal.vue";
import Button from "@/components/ui/Button.vue";
import Input from "@/components/ui/Input.vue";

export default {
  name: "UpdatePost",
  components: { Modal, Button, Input },
  props: {
    modelValue: { type: Boolean, default: false },
    post: { type: Object, default: () => ({}) },
  },
  emits: ["update:modelValue", "save"],
  data() {
    return {
      form: { title: this.post?.title || "", content: this.post?.content || "" },
      imageFile: null,
      previewUrl: "",
      isDragOver: false,
      removeCurrentImage: false,
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
    currentImage() {
      if (this.removeCurrentImage) return "";
      const src = this.post?.image;
      if (!src) return "";
      if (src.startsWith("http://") || src.startsWith("https://")) return src;
      return `http://localhost:8000${src}`;
    },
    hasImage() {
      return (this.currentImage && !this.removeCurrentImage) || this.previewUrl;
    },
  },
  watch: {
    post: {
      handler(newPost) {
        if (newPost) {
          this.form = {
            title: newPost.title || "",
            content: newPost.content || "",
          };
          this.imageFile = null;
          this.previewUrl = "";
          this.removeCurrentImage = false;
        }
      },
      immediate: true,
    },
  },
  methods: {
    cancel() {
      this.open = false;
    },
    save() {
      this.$emit("save", {
        id: this.post?.id,
        ...this.form,
        image: this.imageFile,
        removeImage: this.removeCurrentImage && !this.imageFile,
      });
      this.open = false;
    },
    trigger() {
      this.$refs.file?.click();
    },
    onFileChange(e) {
      const f = e.target.files?.[0];
      this.imageFile = f || null;
      if (this.previewUrl) URL.revokeObjectURL(this.previewUrl);
      this.previewUrl = this.imageFile ? URL.createObjectURL(this.imageFile) : "";
      // Reset remove flag if new image is uploaded
      if (this.imageFile) {
        this.removeCurrentImage = false;
      }
    },
    onDrop(e) {
      this.isDragOver = false;
      const f = e.dataTransfer.files?.[0];
      if (!f) return;
      this.imageFile = f;
      if (this.previewUrl) URL.revokeObjectURL(this.previewUrl);
      this.previewUrl = URL.createObjectURL(f);
      // Reset remove flag if new image is uploaded
      this.removeCurrentImage = false;
    },
    clearCurrentImage() {
      this.removeCurrentImage = true;
      this.imageFile = null;
      if (this.previewUrl) URL.revokeObjectURL(this.previewUrl);
      this.previewUrl = "";
    },
    clearPreviewImage() {
      this.imageFile = null;
      if (this.previewUrl) URL.revokeObjectURL(this.previewUrl);
      this.previewUrl = "";
    },
  },
};
</script>


