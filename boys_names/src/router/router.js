import VueRouter from 'vue-router'
import Vue from 'vue'

import StartPage from '../components/pages/startpage/StartPage.vue'
import SearchPage from '../components/pages/searchpage/SearchPage.vue'
import PopularPage from '../components/pages/popularpage/PopularPage.vue'

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: __dirname,
  routes: [
    { path: '/search-page', component: SearchPage, name: "search-page", props: true },
    { path: '/popular-page', component: PopularPage, name: "popular-page" },
    { path: '/', component: StartPage, name: "start-page" }
  ]
})
