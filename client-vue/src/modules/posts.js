import PostsService from "@/service/posts";

export default {
  namespaced: true,

  state: {
    items: [], // all posts
    myItems: [], // my posts
    likedItems: [], // liked posts
    othersItems: [], // others' posts
    commentsByPostId: {}, // { [postId]: comments[] }
    loading: false,
    error: null,
    success: null,
    pagination: {
      count: 0,
      next: null,
      previous: null,
      currentPage: 1,
      totalPages: 0,
    },
  },

  mutations: {
    SET_LOADING(state, loading) { state.loading = loading; },
    SET_ERROR(state, msg) { state.error = msg; },
    SET_SUCCESS(state, msg) { state.success = msg; },

    SET_ITEMS(state, posts) { state.items = posts || []; },
    SET_MY_ITEMS(state, posts) { state.myItems = posts || []; },
    SET_LIKED_ITEMS(state, posts) { state.likedItems = posts || []; },
    SET_OTHERS_ITEMS(state, posts) { state.othersItems = posts || []; },
    SET_PAGINATION(state, { count, next, previous, currentPage }) {
      const pageSize = 10;
      const totalPages = Math.ceil(count / pageSize);
      state.pagination = {
        count: count || 0,
        next,
        previous,
        currentPage: currentPage || 1,
        totalPages: totalPages || 0,
      };
    },

    UPSERT_POST(state, post) {
      const upsert = (arr) => {
        const idx = arr.findIndex(p => p.id === post.id);
        if (idx === -1) arr.unshift(post);
        else arr.splice(idx, 1, post);
      };
      upsert(state.items);
      upsert(state.myItems);
      upsert(state.likedItems);
      upsert(state.othersItems);
    },
    REMOVE_POST(state, postId) {
      const removeFrom = (arr) => {
        const idx = arr.findIndex(p => p.id === postId);
        if (idx !== -1) arr.splice(idx, 1);
      };
      removeFrom(state.items);
      removeFrom(state.myItems);
      removeFrom(state.likedItems);
      removeFrom(state.othersItems);
    },

    SET_COMMENTS(state, { postId, comments }) {
      state.commentsByPostId = {
        ...state.commentsByPostId,
        [postId]: comments || [],
      };
    },
    ADD_COMMENT(state, { postId, comment }) {
      const curr = state.commentsByPostId[postId] || [];
      state.commentsByPostId = { ...state.commentsByPostId, [postId]: [comment, ...curr] };
    },
    UPDATE_COMMENT(state, { postId, comment }) {
      const curr = state.commentsByPostId[postId] || [];
      const idx = curr.findIndex(c => c.id === comment.id);
      if (idx !== -1) curr.splice(idx, 1, comment);
      state.commentsByPostId = { ...state.commentsByPostId, [postId]: [...curr] };
    },
    REMOVE_COMMENT(state, { postId, commentId }) {
      const curr = state.commentsByPostId[postId] || [];
      const idx = curr.findIndex(c => c.id === commentId);
      if (idx !== -1) curr.splice(idx, 1);
      state.commentsByPostId = { ...state.commentsByPostId, [postId]: [...curr] };
    },
  },

  actions: {
    async fetchAll({ commit }, { page = 1, search = "" } = {}) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        const data = await PostsService.fetchAll(page, search);
        commit("SET_ITEMS", data?.results || []);
        commit("SET_PAGINATION", {
          count: data?.count || 0,
          next: data?.next,
          previous: data?.previous,
          currentPage: page,
        });
        return { success: true, data };
      } catch (err) {
        const message = err.response?.data?.message || "Failed to load posts";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async fetchMine({ commit }, { page = 1, search = "" } = {}) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        const data = await PostsService.fetchMine(page, search);
        commit("SET_MY_ITEMS", data?.results || []);
        commit("SET_PAGINATION", {
          count: data?.count || 0,
          next: data?.next,
          previous: data?.previous,
          currentPage: page,
        });
        return { success: true, data };
      } catch (err) {
        const message = err.response?.data?.message || "Failed to load my posts";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async fetchLiked({ commit }, { page = 1, search = "" } = {}) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        const data = await PostsService.fetchLiked(page, search);
        commit("SET_LIKED_ITEMS", data?.results || []);
        commit("SET_PAGINATION", {
          count: data?.count || 0,
          next: data?.next,
          previous: data?.previous,
          currentPage: page,
        });
        return { success: true, data };
      } catch (err) {
        const message = err.response?.data?.message || "Failed to load liked posts";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async fetchOthers({ commit }, { page = 1, search = "" } = {}) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        const data = await PostsService.fetchOthers(page, search);
        commit("SET_OTHERS_ITEMS", data?.results || []);
        commit("SET_PAGINATION", {
          count: data?.count || 0,
          next: data?.next,
          previous: data?.previous,
          currentPage: page,
        });
        return { success: true, data };
      } catch (err) {
        const message = err.response?.data?.message || "Failed to load others' posts";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async createPost({ commit }, payload) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        const post = await PostsService.create(payload);
        commit("UPSERT_POST", post);
        commit("SET_SUCCESS", "Post created");
        return { success: true, post };
      } catch (err) {
        const message = err.response?.data?.message || "Create post failed";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async updatePost({ commit }, { id, title, content, image, removeImage }) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        const post = await PostsService.update(id, { title, content, image, removeImage });
        commit("UPSERT_POST", post);
        commit("SET_SUCCESS", "Post updated");
        return { success: true, post };
      } catch (err) {
        const message = err.response?.data?.message || "Update post failed";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async deletePost({ commit }, id) {
      commit("SET_LOADING", true); commit("SET_ERROR", null);
      try {
        await PostsService.remove(id);
        commit("REMOVE_POST", id);
        commit("SET_SUCCESS", "Post deleted");
        return { success: true };
      } catch (err) {
        const message = err.response?.data?.message || "Delete post failed";
        commit("SET_ERROR", message); return { success: false, message };
      } finally { commit("SET_LOADING", false); }
    },

    async likePost({ commit, state }, id) {
      try {
        const updatedPost = await PostsService.like(id);
        // Update post in all arrays using the server response
        const updatePost = (arr) => {
          const idx = arr.findIndex(x => x.id === id);
          if (idx !== -1) {
            arr.splice(idx, 1, updatedPost);
          }
        };
        updatePost(state.items);
        updatePost(state.myItems);
        updatePost(state.likedItems);
        updatePost(state.othersItems);
        return { success: true, data: updatedPost };
      } catch (err) {
        return { success: false, message: err.response?.data?.message };
      }
    },

    async unlikePost({ commit, state }, id) {
      try {
        const updatedPost = await PostsService.unlike(id);
        // Update post in all arrays using the server response
        const updatePost = (arr) => {
          const idx = arr.findIndex(x => x.id === id);
          if (idx !== -1) {
            arr.splice(idx, 1, updatedPost);
          }
        };
        updatePost(state.items);
        updatePost(state.myItems);
        updatePost(state.likedItems);
        updatePost(state.othersItems);
        return { success: true, data: updatedPost };
      } catch (err) {
        return { success: false, message: err.response?.data?.message };
      }
    },

    async fetchComments({ commit }, postId) {
      try {
        const data = await PostsService.fetchComments(postId);
        commit("SET_COMMENTS", { postId, comments: data?.results || [] });
        return { success: true };
      } catch (err) {
        return { success: false, message: err.response?.data?.message };
      }
    },

    async addComment({ commit }, { postId, comment }) {
      try {
        const c = await PostsService.addComment(postId, comment);
        commit("ADD_COMMENT", { postId, comment: c });
        return { success: true };
      } catch (err) {
        return { success: false, message: err.response?.data?.message };
      }
    },

    async updateComment({ commit }, { postId, commentId, comment }) {
      try {
        const c = await PostsService.updateComment(commentId, comment);
        commit("UPDATE_COMMENT", { postId, comment: c });
        return { success: true };
      } catch (err) {
        return { success: false, message: err.response?.data?.message };
      }
    },

    async deleteComment({ commit }, { postId, commentId }) {
      try {
        await PostsService.deleteComment(commentId);
        commit("REMOVE_COMMENT", { postId, commentId });
        return { success: true };
      } catch (err) {
        return { success: false, message: err.response?.data?.message };
      }
    },
  },
};


