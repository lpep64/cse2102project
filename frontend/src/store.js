import { createStore } from 'vuex';

export default createStore({
  state: {
    profile: null,
  },
  mutations: {
    setProfile(state, profile) {
      state.profile = profile;
    },
  },
  actions: {
    updateProfile(context, profile) {
      context.commit('setProfile', profile);
    },
  },
  getters: {
    profile: state => state.profile,
  },
});