import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import './components'
import router from './router/router'
import store from './store/store'

Vue.use(Vuex);
Vue.use(VueRouter);

new Vue({
  router,
  el: '#app',
  store: new Vuex.Store(store),
  render: h => h(App)
});
