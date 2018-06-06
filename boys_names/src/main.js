import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import './components'
import router from './router/router'

Vue.use(VueRouter);

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
