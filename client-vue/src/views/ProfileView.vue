<style scoped>
.profile-view__container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}

.profile-view__content {
  height: 100vh;
}

.profile-view__header-view {
  position: relative;
  margin-bottom: 32px;
}

.profile-view__header-view-banner {
  width: 100%;
  height: 160px;
  border-radius: 12px;
  background-image: url("https://picsum.photos/1280/720");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow: hidden;
}

.profile-view__header-view-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: -32px;
  padding: 0 24px;
}

.profile-view__header-view-content__actions {
  display: flex;
  gap: 8px;
}

.profile-view__header-view-content__actions__button {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.25;
}

.profile-view__header-view-content__user-information {
  display: flex;
  align-items: center;
  gap: 16px;
}

.profile-view__header-view-content__user-information__avatar {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  border: 3px solid #fafafa;
  background-color: #fff;

  display: flex;
  align-items: center;
  justify-content: center;
}

.profile-view__header-view-content__user-information__avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-view__header-view-content__user-information__name {
  display: flex;
  align-items: start;
  flex-direction: column;
}

.profile-view__body-view {
  margin-top: 16px;
}
/* Posts grid */
.posts-grid {
  padding: 32px 0;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
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
.profile-view__tab-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}
.profile-view__tab-title {
  margin: 0;
}
.profile-view__tab-header-right {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
.profile-view__search-wrapper {
  min-width: 200px;
  max-width: 400px;
  width: 100%;
  flex: 1;
}
.profile-view__search-wrapper .form-float {
  margin-bottom: 0;
}

:deep(.profile-view__search-wrapper .form-float input) {
  padding: 8px 12px;
  border-radius: 10px;
}

@media (max-width: 768px) {
  .profile-view__tab-header {
    flex-direction: column;
    align-items: flex-start;
  }
  .profile-view__tab-header-right {
    width: 100%;
    justify-content: space-between;
  }
  .profile-view__search-wrapper {
    flex: 1;
    min-width: 0;
  }
  .profile-view__search-wrapper .form-float {
    margin-bottom: 0;
  }
}
</style>

<template>
  <section class="profile-view">
    <div class="profile-view__container">
      <div class="profile-view__header-view">
        <div class="profile-view__header-view-banner">
          <img :src="`https://picsum.photos/1200/220?random=${user?.id || user?.username || 1}`" alt="Profile banner" style="width: 100%; height: 220px; object-fit: cover" />
        </div>
        <div class="profile-view__header-view-content">
          <div class="profile-view__header-view-content__user-information">
            <div class="profile-view__header-view-content__user-information__avatar">
              <Uploader :src="user?.avatar" :can-remove="!!user?.avatar" @select="onAvatarSelect" @remove="onAvatarRemove">
                <Text type="h1" variant="primary" align="center" transform="uppercase" weight="bold">{{ user?.username?.charAt(0) }}</Text>
              </Uploader>
            </div>
            <div class="profile-view__header-view-content__user-information__name">
              <Text type="h4" variant="primary" weight="bold" align="center" transform="uppercase">{{ user?.username }}</Text>
              <Text type="p" variant="text" align="center" style="font-size: 14px">{{ user?.email }}</Text>
            </div>
          </div>
          <div class="profile-view__header-view-content__actions">
            <Button variant="primary" class="profile-view__header-view-content__actions__button" @click="isEditProfileOpen = true">Edit Profile</Button>
            <Button variant="outline" class="profile-view__header-view-content__actions__button" @click="isEditPasswordOpen = true">Change Password</Button>
          </div>
        </div>
      </div>
      <div class="profile-view__body-view">
        <div class="profile-view__body-item" style="margin-top: 16px">
          <Tabs v-model="activeTab" :tabs="['My Posts', 'Liked Posts']">
            <template #tab-1>
              <div class="profile-view__body-item-content">
                <div class="profile-view__tab-header">
                  <Text type="h3" variant="primary" weight="bold" transform="uppercase" class="profile-view__tab-title">My Posts</Text>
                  <div class="profile-view__tab-header-right">
                    <div class="profile-view__search-wrapper">
                      <Input v-model="searchQuery" type="text" placeholder="Search my posts..." @input="onSearchInput" @keyup.enter="onMyPostsSearch" />
                    </div>
                    <Button variant="outline" @click="onAddPost">Add Post</Button>
                  </div>
                </div>
                <div v-if="isLoadingPosts" style="display: flex; flex-direction: column; gap: 12px">
                  <Skeleton type="post" />
                  <Skeleton type="post" />
                </div>
                <div v-else-if="posts.length === 0" style="display: flex; align-items: center; justify-content: center; padding: 24px">
                  <Button variant="outline" @click="onAddPost">Add your first post</Button>
                </div>
                <div v-else>
                  <div class="posts-grid">
                    <Post v-for="post in posts" :key="post.id" :post="post" @edit="onEditPost" @delete="onDeletePost" @like="onLike" />
                  </div>
                  <Pagination v-if="pagination.totalPages > 1" :currentPage="pagination.currentPage" :totalPages="pagination.totalPages" @pageChange="onPageChange" />
                </div>
              </div>
            </template>
            <template #tab-2>
              <div class="profile-view__body-item-content">
                <div class="profile-view__tab-header">
                  <Text type="h3" variant="primary" weight="bold" transform="uppercase" class="profile-view__tab-title">Liked Posts</Text>
                  <div class="profile-view__tab-header-right">
                    <div class="profile-view__search-wrapper">
                      <Input v-model="likedPostsSearchQuery" type="text" placeholder="Search liked posts..." @input="onLikedPostsSearchInput" @keyup.enter="onLikedPostsSearch" />
                    </div>
                  </div>
                </div>
                <div v-if="isLoadingLikedPosts" style="display: flex; flex-direction: column; gap: 12px">
                  <Skeleton type="post" />
                  <Skeleton type="post" />
                </div>
                <div v-else-if="likedPosts.length === 0" style="display: flex; align-items: center; justify-content: center; padding: 24px">
                  <Text type="p" variant="text" align="center">No liked posts yet</Text>
                </div>
                <div v-else>
                  <div class="posts-grid">
                    <Post v-for="post in likedPosts" :key="post.id" :post="post" :showActions="false" @like="onLikeLikedPost" />
                  </div>
                  <Pagination v-if="pagination.totalPages > 1" :currentPage="pagination.currentPage" :totalPages="pagination.totalPages" @pageChange="onLikedPostsPageChange" />
                </div>
              </div>
            </template>
          </Tabs>
        </div>
      </div>
      <EditProfile v-model="isEditProfileOpen" :user="user" @save="onSaveProfile" />
      <EditPassword v-model="isEditPasswordOpen" @save="onSavePassword" />
      <CreatePost v-model="isCreatePostOpen" :saving="isCreatingPost" @save="onCreatePost" />
      <UpdatePost v-if="updatingPost" v-model="isUpdatePostOpen" :post="updatingPost" :saving="isUpdatingPost" @save="onUpdatePost" />
    </div>
  </section>
</template>

<script>
import Tabs from "@/components/ui/Tabs.vue";
import Card from "@/components/ui/Card.vue";
import Post from "@/components/blocks/Post.vue";
import EditProfile from "@/components/blocks/EditProfile.vue";
import EditPassword from "@/components/blocks/EditPassword.vue";
import CreatePost from "@/components/blocks/CreatePost.vue";
import UpdatePost from "@/components/blocks/UpdatePost.vue";
import Uploader from "@/components/ui/Uploader.vue";
import Pagination from "@/components/ui/Pagination.vue";
import Input from "@/components/ui/Input.vue";
import Skeleton from "@/components/ui/Skeleton.vue";

import { toast } from "vue-sonner";
import { mapGetters } from "vuex";
import { gettersTypes } from "@/modules/types";

export default {
  components: { Tabs, Card, Post, EditProfile, EditPassword, CreatePost, UpdatePost, Uploader, Skeleton, Pagination, Input, toast },
  data() {
    return {
      activeTab: 0,
      isEditProfileOpen: false,
      isEditPasswordOpen: false,
      posts: [],
      likedPosts: [],
      isCreatePostOpen: false,
      isCreatingPost: false,
      isLoadingPosts: true,
      isLoadingLikedPosts: false,
      isUpdatePostOpen: false,
      updatingPost: null,
      isUpdatingPost: false,
      currentPage: 1,
      likedPostsPage: 1,
      searchQuery: "",
      likedPostsSearchQuery: "",
      searchTimeout: null,
      likedPostsSearchTimeout: null,
    };
  },
  computed: {
    ...mapGetters("authentication", {
      isAuthenticated: gettersTypes.IS_AUTHENTICATED,
      user: gettersTypes.USER,
    }),
    pagination() {
      return this.$store.state.posts.pagination;
    },
  },
  async mounted() {
    await this.fetchPosts(1, "");
  },
  watch: {
    activeTab(newTab) {
      if (newTab === 1 && this.likedPosts.length === 0) {
        // Tab 2 is "Liked Posts"
        this.fetchLikedPosts(1, "");
      }
    },
  },
  methods: {
    async fetchPosts(page, search = "") {
      this.isLoadingPosts = true;
      this.currentPage = page;
      const { success } = await this.$store.dispatch("posts/fetchMine", { page, search });
      if (success) {
        this.posts = this.$store.state.posts.myItems || [];
      }
      this.isLoadingPosts = false;
      // Scroll to top when page changes
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    onPageChange(page) {
      this.fetchPosts(page, this.searchQuery);
    },
    async fetchLikedPosts(page, search = "") {
      this.isLoadingLikedPosts = true;
      this.likedPostsPage = page;
      const { success } = await this.$store.dispatch("posts/fetchLiked", { page, search });
      if (success) {
        this.likedPosts = this.$store.state.posts.likedItems || [];
      }
      this.isLoadingLikedPosts = false;
      // Scroll to top when page changes
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    onLikedPostsPageChange(page) {
      this.fetchLikedPosts(page, this.likedPostsSearchQuery);
    },
    onSearchInput() {
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(() => {
        this.onMyPostsSearch();
      }, 500);
    },
    async onMyPostsSearch() {
      await this.fetchPosts(1, this.searchQuery.trim());
    },
    onLikedPostsSearchInput() {
      clearTimeout(this.likedPostsSearchTimeout);
      this.likedPostsSearchTimeout = setTimeout(() => {
        this.onLikedPostsSearch();
      }, 500);
    },
    async onLikedPostsSearch() {
      await this.fetchLikedPosts(1, this.likedPostsSearchQuery.trim());
    },
    async onSaveProfile(payload) {
      const { success, message } = await this.$store.dispatch("authentication/updateProfile", payload || {});
      if (success) {
        toast.success(message || "Profile updated successfully");
      } else {
        toast.error(message || "Profile update failed");
      }
    },
    async onSavePassword(payload) {
      const { success, message } = await this.$store.dispatch("authentication/changePassword", payload);
      if (success) {
        toast.success(message || "Password updated successfully");
      } else {
        toast.error(message || "Password update failed");
      }
    },
    async onAvatarSelect(file) {
      const { success, message } = await this.$store.dispatch("authentication/updateAvatar", file);
      if (success) toast.success(message || "Avatar updated successfully");
      else toast.error(message || "Avatar update failed");
    },
    async onAvatarRemove() {
      const { success, message } = await this.$store.dispatch("authentication/removeAvatar");
      if (success) toast.success(message || "Avatar removed successfully");
      else toast.error(message || "Avatar remove failed");
    },
    onAddPost() {
      this.isCreatePostOpen = true;
    },
    async onCreatePost(payload) {
      this.isCreatingPost = true;
      try {
        const { success, post, message } = await this.$store.dispatch("posts/createPost", payload);
        if (success) {
          toast.success("Post created successfully!");
          this.isCreatePostOpen = false;
          this.posts = this.$store.state.posts.myItems || [];
        } else {
          toast.error(message || "Failed to create post");
        }
      } catch (err) {
        console.error("Error creating post:", err);
        toast.error("An error occurred while creating the post");
      } finally {
        this.isCreatingPost = false;
      }
    },
    onEditPost(post) {
      this.updatingPost = { ...post };
      this.isUpdatePostOpen = true;
    },
    async onUpdatePost(payload) {
      this.isUpdatingPost = true;
      try {
        const { id, title, content, image, removeImage } = payload;
        const { success, post, message } = await this.$store.dispatch("posts/updatePost", { id, title, content, image, removeImage });
        if (success) {
          const idx = this.posts.findIndex((p) => p.id === id);
          if (idx !== -1) this.posts.splice(idx, 1, post);
          toast.success("Post updated successfully!");
          this.isUpdatePostOpen = false;
          this.updatingPost = null;
        } else {
          toast.error(message || "Failed to update post");
        }
      } catch (err) {
        console.error("Error updating post:", err);
        toast.error("An error occurred while updating the post");
      } finally {
        this.isUpdatingPost = false;
      }
    },
    async onDeletePost(post) {
      const confirmDelete = window.confirm("Are you sure you want to delete this post?");
      if (!confirmDelete) return;
      try {
        const { success, message } = await this.$store.dispatch("posts/deletePost", post.id);
        if (success) {
          const idx = this.posts.findIndex((p) => p.id === post.id);
          if (idx !== -1) this.posts.splice(idx, 1);
          toast.success("Post deleted successfully!");
        } else {
          toast.error(message || "Failed to delete post");
        }
      } catch (err) {
        console.error("Error deleting post:", err);
        toast.error("An error occurred while deleting the post");
      }
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
    async onLikeLikedPost(post) {
      const action = post.is_liked ? "posts/unlikePost" : "posts/likePost";
      const wasLiked = post.is_liked;
      const { success, data: updatedPost, message } = await this.$store.dispatch(action, post.id);
      if (success && updatedPost) {
        if (!updatedPost.is_liked && wasLiked) {
          // If unliked, remove from liked posts list
          const idx = this.likedPosts.findIndex((p) => p.id === post.id);
          if (idx !== -1) {
            this.likedPosts.splice(idx, 1);
          }
          toast.success("Post unliked");
        } else {
          // Update local post state with server response
          const idx = this.likedPosts.findIndex((p) => p.id === post.id);
          if (idx !== -1) {
            this.likedPosts[idx] = updatedPost;
          }
          toast.success("Post liked!");
        }
      } else {
        toast.error(message || "Failed to like post");
      }
    },
  },
};
</script>