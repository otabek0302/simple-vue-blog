<style scoped>
.home-view__container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}
.home-view__content {
  min-height: 100vh;
  padding: 32px 0;
}
.posts-grid {
  padding: 32px 0;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  column-gap: 16px;
  row-gap: 48px;
}
@media (max-width: 1024px) {
  .posts-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 640px) {
  .posts-grid {
    grid-template-columns: 1fr;
  }
}
.home-view__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
</style>

<template>
  <section class="home-view">
    <div class="home-view__container">
      <div class="home-view__content">
        <div class="home-view__header">
          <Text type="h2" variant="primary" weight="bold" transform="uppercase">Latest Posts</Text>
        </div>
        <div v-if="isLoading" style="display: flex; flex-direction: column; gap: 12px">
          <Skeleton type="post" />
          <Skeleton type="post" />
        </div>
        <div v-else>
          <div v-if="posts.length === 0" class="posts-empty">
            <Text type="p" variant="text" align="center">No posts found</Text>
          </div>
          <div v-else>
            <div class="posts-grid">
              <Post v-for="post in posts" :key="post.id" :post="post" :showActions="false" @like="onLike" />
            </div>
            <Pagination
              :currentPage="pagination.currentPage"
              :totalPages="pagination.totalPages"
              @pageChange="onPageChange"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Post from "@/components/blocks/Post.vue";
import Skeleton from "@/components/ui/Skeleton.vue";
import Pagination from "@/components/ui/Pagination.vue";
import Text from "@/components/ui/Text.vue";
import { toast } from "vue-sonner";

export default {
  components: { Post, Skeleton, Pagination, Text },
  data() {
    return {
      posts: [],
      isLoading: true,
      currentPage: 1,
      searchQuery: "",
    };
  },
  computed: {
    pagination() {
      return this.$store.state.posts.pagination;
    },
  },
  watch: {
    "$route.query.search"(newVal) {
      this.searchQuery = newVal || "";
      if (newVal) {
        this.fetchPosts(1, newVal);
      } else {
        this.fetchPosts(1, "");
      }
    },
  },
  async mounted() {
    // Check for search query in URL
    const searchParam = this.$route.query.search;
    if (searchParam) {
      this.searchQuery = searchParam;
      await this.fetchPosts(1, searchParam);
    } else {
      await this.fetchPosts(1, "");
    }
  },
  methods: {
    async fetchPosts(page, search = "") {
      this.isLoading = true;
      this.currentPage = page;
      const { success } = await this.$store.dispatch("posts/fetchAll", { page, search });
      if (success) {
        this.posts = this.$store.state.posts.items || [];
      }
      this.isLoading = false;
      // Scroll to top when page changes
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    onPageChange(page) {
      this.fetchPosts(page, this.searchQuery);
    },
    async onLike(post) {
      const action = post.is_liked ? "posts/unlikePost" : "posts/likePost";
      const { success, data: updatedPost, message } = await this.$store.dispatch(action, post.id);
      if (success && updatedPost) {
        // Update local post state with server response
        const idx = this.posts.findIndex((p) => p.id === post.id);
        if (idx !== -1) {
          this.posts[idx] = updatedPost;
        }
        toast.success(updatedPost.is_liked ? "Post liked!" : "Post unliked");
      } else {
        toast.error(message || "Failed to like post");
      }
    },
  },
};
</script>
