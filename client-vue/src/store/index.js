import { createStore } from 'vuex'
import authentication from '@/modules/authentication'
import posts from '@/modules/posts'

const store = createStore({
  state() { },
  mutations: {},
  actions: {},
  modules: { authentication, posts }
})

export default store