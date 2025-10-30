<style scoped>
.author {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.author__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
  border: 1px solid #e0e0e0;
}

.author__name {
  font-size: 14px;
  font-weight: 500;
}

.author__meta {
  font-size: 12px;
  color: #666;
}
</style>

<template>
  <div class="author" :class="authorClass">
    <img v-if="avatar" :src="avatar" alt="author" class="author__avatar" />
    <div class="author__content">
      <div class="author__name">{{ name }}</div>
      <div v-if="meta" class="author__meta">{{ meta }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Author",
  props: {
    name: {
      type: String,
      required: true,
    },
    avatar: {
      type: String,
      default: "",
    },
    meta: {
      type: String,
      default: "",
    },
    authorClass: {
      type: String,
      default: "",
    },
  },
};
</script>


