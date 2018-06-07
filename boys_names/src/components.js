import Vue from 'vue'

import Header from './components/reusable/Header.vue'
import SecondHeader from './components/reusable/SecondHeader.vue'
import Footer from './components/reusable/Footer.vue'
import StartPage from './components/pages/startpage/StartPage.vue'
import SearchPage from './components/pages/searchpage/SearchPage.vue'
import PopularPage from './components/pages/popularpage/PopularPage.vue'
import SearchForm from './components/reusable/SearchForm.vue'

Vue.component('main-header', Header);
Vue.component('second-header', SecondHeader);
Vue.component('start-page', StartPage);
Vue.component('search-page', SearchPage);
Vue.component('popular-page', PopularPage);


// reusable components
Vue.component('search-form', SearchForm);
Vue.component('main-footer', Footer);
