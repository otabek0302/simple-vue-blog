<style scoped>
.post-detail__container {
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
  padding: 32px 16px;
}
.post-detail__header {
  margin-bottom: 24px;
}
.post-detail__back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: #3b82f6;
  text-decoration: none;
  font-size: 14px;
  margin-bottom: 16px;
}
.post-detail__back-link:hover {
  text-decoration: underline;
}
.post-detail__card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}
.post-detail__image {
  width: 100%;
  height: 400px;
  object-fit: cover;
  display: block;
}
.post-detail__body {
  padding: 32px;
}
.post-detail__title {
  font-size: 32px;
  font-weight: 700;
  color: #0f172a;
  margin: 0 0 16px 0;
}
.post-detail__meta {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #e5e7eb;
  font-size: 14px;
  color: #64748b;
}
.post-detail__author {
  display: flex;
  align-items: center;
  gap: 8px;
}
.post-detail__content {
  font-size: 16px;
  line-height: 1.8;
  color: #334155;
  white-space: pre-line;
  margin-bottom: 32px;
}
.post-detail__actions {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 32px;
  padding-top: 24px;
  border-top: 1px solid #e5e7eb;
}
.post-detail__like-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border: none;
  background: transparent;
  color: #6b7280;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.25;
  cursor: pointer;
  transition: all 0.2s ease;
  border-radius: 8px;
}
.post-detail__like-btn:hover:not(:disabled) {
  color: #ef4444;
}
.post-detail__like-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.post-detail__like-btn--liked i{
  color: #ef4444;
}
.post-detail__edit-actions {
  display: flex;
  gap: 8px;
  margin-left: auto;
}
.post-detail__edit-btn,
.post-detail__delete-btn {
  padding: 8px 16px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  background: #fff;
  cursor: pointer;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.25;
  transition: all 0.2s ease;
}
.post-detail__edit-btn {
  color: #3b82f6;
}
.post-detail__edit-btn:hover {
  background: #eff6ff;
  border-color: #3b82f6;
}
.post-detail__delete-btn {
  color: #dc3545;
}
.post-detail__delete-btn:hover {
  background: #fef2f2;
  border-color: #dc3545;
}
.post-detail__comments-section {
  margin-top: 32px;
  padding-top: 32px;
  border-top: 1px solid #e5e7eb;
}
.post-detail__comments-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}
.post-detail__add-comment-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.25;
  transition: all 0.2s ease;
}
.post-detail__add-comment-btn i {
  font-size: 14px;
}
.post-detail__comments-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.post-detail__comment {
  padding: 16px;
  background: #f9fafb;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}
.post-detail__comment-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.post-detail__comment-author {
  font-weight: 600;
  font-size: 14px;
  color: #0f172a;
}
.post-detail__comment-date {
  font-size: 12px;
  color: #64748b;
}
.post-detail__comment-content {
  font-size: 14px;
  color: #334155;
  line-height: 1.6;
}
.post-detail__comment-actions {
  display: flex;
  gap: 8px;
}
.post-detail__comment-action {
  padding: 4px 8px;
  font-size: 12px;
  border: none;
  background: transparent;
  cursor: pointer;
  color: #64748b;
  border-radius: 4px;
  transition: all 0.2s ease;
}
.post-detail__comment-action:hover {
  background: #f3f4f6;
}
.post-detail__comment-action--edit {
  color: #3b82f6;
}
.post-detail__comment-action--delete {
  color: #dc3545;
}
.post-detail__loading {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 400px;
}
.post-detail__error {
  text-align: center;
  padding: 48px;
  color: #dc3545;
}
</style>

<template>
  <section class="post-detail">
    <div class="post-detail__container">
      <div class="post-detail__header">
        <RouterLink :to="{ name: 'home' }" class="post-detail__back-link">
          <i class="fas fa-arrow-left"></i>
          <span>Back to Posts</span>
        </RouterLink>
      </div>

      <div v-if="isLoading" class="post-detail__loading">
        <Skeleton type="post" />
      </div>

      <div v-else-if="error" class="post-detail__error">
        <p>{{ error }}</p>
      </div>

      <div v-else-if="post" class="post-detail__card">
        <img v-if="normalizedImage" :src="normalizedImage" alt="post" class="post-detail__image" />
        <div class="post-detail__body">
          <Text type="h1" variant="primary" weight="bold" class="post-detail__title">{{ post.title }}</Text>
          <div class="post-detail__meta">
            <div class="post-detail__author" v-if="post.author">
              <i class="fas fa-user"></i>
              <span>{{ post.author.username || post.author.email }}</span>
            </div>
            <span v-if="post.created_at">• {{ formatDate(post.created_at) }}</span>
          </div>
          <div class="post-detail__content">{{ post.content }}</div>

          <div class="post-detail__actions">
            <button class="post-detail__like-btn" :class="{ 'post-detail__like-btn--liked': post.is_liked }" @click="handleLike" :disabled="isLiking">
              <i :class="post.is_liked ? 'fas' : 'far'" class="fa-heart"></i>
              <span>{{ post.likes_count || 0 }} Likes</span>
            </button>

            <div class="post-detail__edit-actions" v-if="isPostOwner">
              <button class="post-detail__edit-btn" @click="onEdit"><i class="fas fa-pen"></i> Edit</button>
              <button class="post-detail__delete-btn" @click="onDelete"><i class="fas fa-trash"></i> Delete</button>
            </div>
          </div>

          <div class="post-detail__comments-section">
            <div class="post-detail__comments-header">
              <Text type="h3" variant="primary" weight="bold">{{ comments.length }} Comments</Text>
              <Button v-if="isAuthenticated" variant="primary" class="post-detail__add-comment-btn" @click="openAddComment"> <i class="fas fa-plus"></i> Add Comment </Button>
              <Text v-else type="p" variant="text" style="color: #64748b; font-size: 14px"> Please <RouterLink :to="{ name: 'login' }" style="color: #3b82f6; text-decoration: none">login</RouterLink> to add a comment </Text>
            </div>

            <div v-if="isLoadingComments" style="display: flex; flex-direction: column; gap: 12px">
              <Skeleton type="comment" />
              <Skeleton type="comment" />
            </div>

            <div v-else-if="comments.length === 0" style="text-align: center; padding: 24px; color: #64748b">
              <Text type="p" variant="text">No comments yet. Be the first to comment!</Text>
            </div>

            <div v-else class="post-detail__comments-list">
              <div v-for="comment in comments" :key="comment.id" class="post-detail__comment">
                <div class="post-detail__comment-header">
                  <div>
                    <span class="post-detail__comment-author">{{ comment.user?.username || comment.user?.email || "Anonymous" }}</span>
                    <span class="post-detail__comment-date"> • {{ formatDate(comment.created_at) }}</span>
                  </div>
                  <div class="post-detail__comment-actions" v-if="isCommentOwner(comment)">
                    <button class="post-detail__comment-action post-detail__comment-action--edit" @click="onEditComment(comment)">
                      <i class="fas fa-pen"></i>
                    </button>
                    <button class="post-detail__comment-action post-detail__comment-action--delete" @click="onDeleteComment(comment)">
                      <i class="fas fa-trash"></i>
                    </button>
                  </div>
                </div>
                <div class="post-detail__comment-content">{{ comment.comment }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <AddComment v-model="isAddCommentOpen" :postId="parseInt($route.params.id)" @save="onAddComment" />
      <UpdateComment v-if="editingComment" v-model="isUpdateCommentOpen" :commentId="editingComment.id" :initial="editingComment.comment" @save="onUpdateComment" />
      <UpdatePost v-if="editingPost" v-model="isUpdatePostOpen" :post="editingPost" @save="onUpdatePost" />
    </div>
  </section>
</template>

<script>
import Skeleton from "@/components/ui/Skeleton.vue";
import PostsService from "@/service/posts";
import Text from "@/components/ui/Text.vue";
import Button from "@/components/ui/Button.vue";
import AddComment from "@/components/blocks/AddComment.vue";
import UpdateComment from "@/components/blocks/UpdateComment.vue";
import UpdatePost from "@/components/blocks/UpdatePost.vue";
import { toast } from "vue-sonner";
import { mapGetters } from "vuex";
import { gettersTypes } from "@/modules/types";

export default {
  components: {
    Skeleton,
    Text,
    Button,
    AddComment,
    UpdateComment,
    UpdatePost,
  },
  name: "PostDetailView",
  data() {
    return {
      post: null,
      isLoading: true,
      error: null,
      backendBase: "http://localhost:8000",
      isLiking: false,
      comments: [],
      isLoadingComments: false,
      isAddCommentOpen: false,
      isUpdateCommentOpen: false,
      editingComment: null,
      isUpdatePostOpen: false,
      editingPost: null,
    };
  },
  computed: {
    normalizedImage() {
      if (!this.post?.image) return "";
      const src = this.post.image;
      if (typeof src !== "string") return "";
      if (src.startsWith("http://") || src.startsWith("https://")) return src;
      return `${this.backendBase}${src}`;
    },
    ...mapGetters("authentication", {
      _isAuthenticated: gettersTypes.IS_AUTHENTICATED,
      currentUser: gettersTypes.USER,
    }),
    isAuthenticated() {
      // Check both store state and localStorage as fallback
      const storeAuth = this.$store.getters["authentication/IS_AUTHENTICATED"];
      const hasLocalTokens = !!localStorage.getItem("tokens");
      return storeAuth || hasLocalTokens;
    },
    isPostOwner() {
      return this.post && this.currentUser && this.post.author?.id === this.currentUser.id;
    },
  },
  async mounted() {
    await this.fetchPost();
  },
  watch: {
    "$route.params.id": {
      handler: "fetchPost",
      immediate: false,
    },
  },
  methods: {
    async fetchPost() {
      const postId = this.$route.params.id;
      if (!postId) {
        this.error = "Post ID is required";
        this.isLoading = false;
        return;
      }

      this.isLoading = true;
      this.error = null;

      try {
        const data = await PostsService.fetchById(postId);
        this.post = data;
        await this.fetchComments();
      } catch (err) {
        this.error = err.response?.data?.message || "Failed to load post";
        console.error("Error fetching post:", err);
      } finally {
        this.isLoading = false;
      }
    },
    async fetchComments() {
      if (!this.post?.id) return;
      this.isLoadingComments = true;
      try {
        const data = await this.$store.dispatch("posts/fetchComments", this.post.id);
        this.comments = this.$store.state.posts.commentsByPostId[this.post.id] || [];
      } catch (err) {
        console.error("Error fetching comments:", err);
      } finally {
        this.isLoadingComments = false;
      }
    },
    async handleLike() {
      if (this.isLiking || !this.post) return;
      this.isLiking = true;
      const action = this.post.is_liked ? "posts/unlikePost" : "posts/likePost";
      const { success, data: updatedPost, message } = await this.$store.dispatch(action, this.post.id);
      if (success && updatedPost) {
        this.post = updatedPost;
        toast.success(this.post.is_liked ? "Post liked!" : "Post unliked");
      } else {
        toast.error(message || "Failed to like post");
      }
      setTimeout(() => {
        this.isLiking = false;
      }, 300);
    },
    onEdit() {
      this.editingPost = { ...this.post };
      this.isUpdatePostOpen = true;
    },
    async onUpdatePost(payload) {
      try {
        const { id, title, content, image, removeImage } = payload;
        const { success, post, message } = await this.$store.dispatch("posts/updatePost", {
          id,
          title,
          content,
          image,
          removeImage,
        });
        if (success) {
          this.post = post;
          toast.success("Post updated successfully!");
          this.isUpdatePostOpen = false;
          this.editingPost = null;
        } else {
          toast.error(message || "Failed to update post");
        }
      } catch (err) {
        console.error("Error updating post:", err);
        toast.error("An error occurred while updating the post");
      }
    },
    async onDelete() {
      const confirmDelete = window.confirm("Are you sure you want to delete this post?");
      if (!confirmDelete) return;
      try {
        const { success, message } = await this.$store.dispatch("posts/deletePost", this.post.id);
        if (success) {
          toast.success("Post deleted successfully!");
          this.$router.push({ name: "home" });
        } else {
          toast.error(message || "Failed to delete post");
        }
      } catch (err) {
        console.error("Error deleting post:", err);
        toast.error("An error occurred while deleting the post");
      }
    },
    openAddComment() {
      if (!this.isAuthenticated) {
        toast.error("Please login to add a comment");
        this.$router.push({ name: "login" });
        return;
      }
      this.isAddCommentOpen = true;
    },
    async onAddComment(payload) {
      try {
        const { success, message } = await this.$store.dispatch("posts/addComment", payload);
        if (success) {
          // Refresh comments after adding
          await this.fetchComments();
          toast.success("Comment added successfully");
          // The modal will close automatically via AddComment component
        } else {
          toast.error(message || "Failed to add comment");
        }
      } catch (err) {
        console.error("Error adding comment:", err);
        toast.error("An error occurred while adding the comment");
      }
    },
    onEditComment(comment) {
      this.editingComment = comment;
      this.isUpdateCommentOpen = true;
    },
    async onUpdateComment(payload) {
      try {
        const { commentId, comment } = payload;
        const { success, message } = await this.$store.dispatch("posts/updateComment", {
          postId: this.post.id,
          commentId,
          comment,
        });
        if (success) {
          await this.fetchComments();
          toast.success("Comment updated successfully!");
          this.editingComment = null;
        } else {
          toast.error(message || "Failed to update comment");
        }
      } catch (err) {
        console.error("Error updating comment:", err);
        toast.error("An error occurred while updating the comment");
      }
    },
    async onDeleteComment(comment) {
      const confirmDelete = window.confirm("Are you sure you want to delete this comment?");
      if (!confirmDelete) return;
      try {
        const { success, message } = await this.$store.dispatch("posts/deleteComment", {
          postId: this.post.id,
          commentId: comment.id,
        });
        if (success) {
          await this.fetchComments();
          toast.success("Comment deleted successfully!");
        } else {
          toast.error(message || "Failed to delete comment");
        }
      } catch (err) {
        console.error("Error deleting comment:", err);
        toast.error("An error occurred while deleting the comment");
      }
    },
    isCommentOwner(comment) {
      return this.currentUser && comment.user?.id === this.currentUser.id;
    },
    formatDate(value) {
      try {
        const d = new Date(value);
        return d.toLocaleDateString();
      } catch (e) {
        return "";
      }
    },
  },
};
</script>

