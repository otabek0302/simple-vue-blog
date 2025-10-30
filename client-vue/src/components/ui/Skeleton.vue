<style scoped>
.skeleton { width: 100%; display: block; }
.shimmer { position: relative; overflow: hidden; background: #f0f2f5; }
.shimmer::after { content: ""; position: absolute; inset: 0; transform: translateX(-100%); background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.7) 50%, rgba(255,255,255,0) 100%); animation: shimmer 1.4s infinite; }
@keyframes shimmer { 100% { transform: translateX(100%); } }

.skel-post { padding: 16px; border: 1px solid #eaeaea; border-radius: 12px; }
.skel-post__header { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
.skel-post__avatar { width: 40px; height: 40px; border-radius: 50%; }
.skel-post__title { height: 14px; width: 180px; border-radius: 8px; }
.skel-post__image { height: 160px; border-radius: 12px; margin: 12px 0; }
.skel-post__line { height: 10px; width: 100%; border-radius: 6px; margin: 8px 0; }

.skel-comment { display: flex; align-items: flex-start; gap: 12px; }
.skel-comment__avatar { width: 32px; height: 32px; border-radius: 50%; }
.skel-comment__body { flex: 1; }
.skel-comment__line { height: 10px; width: 100%; border-radius: 6px; margin: 6px 0; }

.skel-avatar { width: 80px; height: 80px; border-radius: 50%; }
</style>

<template>
  <div class="skeleton">
    <template v-if="type === 'post'">
      <div class="skel-post">
        <div class="skel-post__header">
          <div class="skel-post__avatar shimmer"></div>
          <div class="skel-post__title shimmer"></div>
        </div>
        <div class="skel-post__image shimmer"></div>
        <div class="skel-post__line shimmer" style="width: 90%"></div>
        <div class="skel-post__line shimmer" style="width: 70%"></div>
      </div>
    </template>
    <template v-else-if="type === 'comment'">
      <div class="skel-comment">
        <div class="skel-comment__avatar shimmer"></div>
        <div class="skel-comment__body">
          <div class="skel-comment__line shimmer" style="width: 80%"></div>
          <div class="skel-comment__line shimmer" style="width: 60%"></div>
        </div>
      </div>
    </template>
    <template v-else-if="type === 'avatar'">
      <div class="skel-avatar shimmer"></div>
    </template>
  </div>
</template>

<script>
export default {
  name: "Skeleton",
  props: {
    type: {
      type: String,
      default: "post",
      validator: (v) => ["post", "comment", "avatar"].includes(v),
    },
  },
};
</script>


