import api from "@/service/axios";

const PostsService = {
  fetchAll: async (page = 1, search = "") => {
    const params = { page };
    if (search) params.search = search;
    const { data } = await api.get("/posts/", { params });
    return data;
  },
  fetchMine: async (page = 1, search = "") => {
    const params = { page };
    if (search) params.search = search;
    const { data } = await api.get("/posts/me/", { params });
    return data;
  },
  fetchLiked: async (page = 1, search = "") => {
    const params = { page };
    if (search) params.search = search;
    const { data } = await api.get("/posts/liked/", { params });
    return data;
  },
  fetchOthers: async (page = 1, search = "") => {
    const params = { page };
    if (search) params.search = search;
    const { data } = await api.get("/posts/others/", { params });
    return data;
  },
  fetchById: async (id) => {
    const { data } = await api.get(`/posts/${id}/`);
    return data;
  },
  create: async ({ title, content, image }) => {
    const form = new FormData();
    form.append("title", title);
    form.append("content", content);
    if (image) form.append("image", image);
    const { data } = await api.post("/posts/", form);
    return data;
  },
  update: async (id, { title, content, image, removeImage }) => {
    if (image || removeImage) {
      const form = new FormData();
      form.append("title", title);
      form.append("content", content);
      if (image) form.append("image", image);
      if (removeImage) form.append("removeImage", "true");
      const { data } = await api.put(`/posts/${id}/`, form);
      return data;
    }
    const { data } = await api.put(`/posts/${id}/`, { title, content });
    return data;
  },
  remove: async (id) => {
    await api.delete(`/posts/${id}/`);
  },
  like: async (id) => {
    const { data } = await api.post(`/posts/${id}/like/`);
    return data;
  },
  unlike: async (id) => {
    const { data } = await api.post(`/posts/${id}/unlike/`);
    return data;
  },
  fetchComments: async (postId) => {
    const { data } = await api.get(`/posts/${postId}/comments/`);
    return data;
  },
  addComment: async (postId, comment) => {
    const { data } = await api.post(`/posts/${postId}/comments/`, { comment });
    return data;
  },
  updateComment: async (commentId, comment) => {
    const { data } = await api.put(`/comments/${commentId}/`, { comment });
    return data;
  },
  deleteComment: async (commentId) => {
    await api.delete(`/comments/${commentId}/`);
  },
};

export default PostsService;


