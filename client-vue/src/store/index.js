import { createStore } from 'vuex'
import authentication from '@/modules/authentication'

const store = createStore({
  state() { },
  mutations: {},
  actions: {},
  modules: { authentication }
})

export default store