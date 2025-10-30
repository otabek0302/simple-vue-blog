<style scoped>
.post-card {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  border-radius: 12px;
  background: #fff;
  color: #334155;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}
.post-card__top {
  position: relative;
  margin: 0 16px;
  margin-top: -24px;
  height: 180px;
  overflow: hidden;
  border-radius: 12px;
  background: linear-gradient(90deg, #3b82f6, #2563eb);
  box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.25);
}
.post-card__top img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.post-card__body {
  padding: 32px 24px;
}
.post-card__title {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 600;
  color: #0f172a;
}
.post-card__content {
  margin: 0;
  font-size: 14px;
  line-height: 1.6;
  white-space: pre-line;
}
.post-card__date {
  font-size: 12px;
  color: #555555;
  font-weight: 400;
}
.post-card__footer {
  padding: 24px;
  padding-top: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.post-card__footer-left {
  display: flex;
  align-items: center;
  gap: 8px;
}
.post-card__meta {
  width: 100%;
  display: flex;
  gap: 8px;
  font-size: 12px;
  justify-content: flex-end;
  align-items: center;
}

.post-card__actions {
  display: inline-flex;
  gap: 8px;
}

.icon-btn {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  background: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.icon-btn:hover {
  background: #f7f7f7;
}
.icon-eye {
  color: #0057ff;
}
.icon-edit {
  color: #0057ff;
}
.icon-trash {
  color: #dc3545;
}
.post-card__title-link {
  text-decoration: none;
  color: inherit;
  display: block;
}
.post-card__title-link:hover .post-card__title {
  color: #3b82f6;
  transition: color 0.2s ease;
}
.like-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: none;
  background: transparent;
  color: #6b7280;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.25;
  cursor: pointer;
  transition: all 0.2s ease;
}
.like-btn:hover:not(:disabled) {
  color: #ef4444;
  background: transparent;
}
.like-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.like-btn--liked i {
  color: #ef4444;
}
.like-btn i {
  font-size: 16px;
}
</style>

<template>
  <div class="post-card">
    <div class="post-card__top">
      <img v-if="normalizedImage" :src="normalizedImage" alt="post" />
    </div>
    <div class="post-card__body">
      <RouterLink :to="{ name: 'post-detail', params: { id: post.id } }" class="post-card__title-link">
        <Text type="h5" variant="primary" weight="bold" class="post-card__title">{{ post.title.slice(0, 30) + (post.title.length > 30 ? "..." : "") }}</Text>
      </RouterLink>
      <Text type="p" variant="text" weight="normal" class="post-card__content">{{ shortContent.slice(0, 100) + (shortContent.length > 100 ? "..." : "") }}</Text>
      <Text type="p" variant="text" weight="normal" class="post-card__date" v-if="formatDate(post.created_at)">{{ formatDate(post.created_at) }}</Text>
    </div>
    <div class="post-card__footer">
      <div class="post-card__actions" v-if="showActions">
        <button class="icon-btn" title="Read More" @click="$emit('readMore', post)"><i class="fas fa-eye icon-eye"></i></button>
        <button class="icon-btn" title="Edit" @click="$emit('edit', post)"><i class="fas fa-pen icon-edit"></i></button>
        <button class="icon-btn" title="Delete" @click="$emit('delete', post)"><i class="fas fa-trash icon-trash"></i></button>
      </div>
      <div class="post-card__footer-left">
        <button class="like-btn" :class="{ 'like-btn--liked': post.is_liked }" @click="handleLike" :disabled="isLiking">
          <i :class="post.is_liked ? 'fas' : 'far'" class="fa-heart"></i>
          <span>{{ post.likes_count || 0 }}</span>
        </button>
      </div>
      <div class="post-card__meta">
        <Text type="span" variant="text" weight="normal" v-if="post.author.email">By:</Text>
        <Text type="span" variant="text" weight="normal" v-if="post.author.username">{{ post.author.username }}</Text>
      </div>
    </div>
  </div>
</template>

<script>
import Text from "@/components/ui/Text.vue";

export default {
  components: {
    Text,
  },
  name: "Post",
  props: {
    post: {
      type: Object,
      required: true,
    },
    showActions: {
      type: Boolean,
      default: true,
    },
    backendBase: {
      type: String,
      default: "http://localhost:8000",
    },
  },
  data() {
    return {
      isLiking: false,
    };
  },
  computed: {
    shortContent() {
      const text = this.post.content || "";
      return text.length > 160 ? text.slice(0, 160) + "…" : text;
    },
    normalizedImage() {
      const src = this.post.image;
      if (!src) return "";
      if (typeof src !== "string") return "";
      if (src.startsWith("http://") || src.startsWith("https://")) return src;
      return `${this.backendBase}${src}`;
    },
  },
  methods: {
    formatDate(value) {
      try {
        const d = new Date(value);
        return d.toLocaleDateString();
      } catch (e) {
        return "";
      }
    },
    async handleLike() {
      if (this.isLiking) return;
      this.isLiking = true;
      this.$emit("like", this.post);
      // Reset loading state after a short delay to allow parent to update
      setTimeout(() => {
        this.isLiking = false;
      }, 300);
    },
  },
};
</script>


