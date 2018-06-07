import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
// import axios from 'axios'
import VueRouter from 'vue-router'
import './components'
import router from './router/router'
import store from './store/store'

Vue.use(Vuex);
Vue.use(VueRouter);
// Vue.use(axios);

new Vue({
  router,
  el: '#app',
  store: new Vuex.Store(store),
  render: h => h(App)
});
