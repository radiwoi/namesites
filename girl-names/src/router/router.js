import VueRouter from 'vue-router'
import Vue from 'vue'

import StartPage from '../components/pages/startpage/StartPage.vue'

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: __dirname,
  routes: [
    // { path: '/search-page', component: SearchPage, name: "search-page" },
    // { path: '/popular-page', component: PopularPage, name: "popular-page" },
    // { path: '/favorite-page', component: FavoritePage, name: "favorite-page" },
    { path: '/', component: StartPage, name: "start-page" }
  ]
})
