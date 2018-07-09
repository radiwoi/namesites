import VueRouter from 'vue-router'
import Vue from 'vue'

import StartPage from '../components/pages/startpage/StartPage.vue'
import SearchPage from '../components/pages/searchpage/SearchPage.vue'
import PopularPage from '../components/pages/popularpage/PopularPage.vue'
import FavoritePage from '../components/pages/favoritepage/FavoritePage.vue'

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: __dirname,
  routes: [
    { path: '/sokresultat', component: SearchPage, name: "search-page" },
    { path: '/populara', component: PopularPage, name: "popular-page" },
    { path: '/mina-favoriter', component: FavoritePage, name: "favorite-page" },
    { path: '/', component: StartPage, name: "start-page" }
  ]
})
