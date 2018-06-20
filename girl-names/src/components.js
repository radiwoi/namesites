import Vue from 'vue'

import Header from './components/reusable/Header.vue'
import Footer from './components/reusable/Footer.vue'
import StartPage from './components/pages/startpage/StartPage.vue'
import SearchForm from './components/reusable/SearchForm.vue'

Vue.component('main-header', Header);
Vue.component('start-page', StartPage);


// reusable components
Vue.component('search-form', SearchForm);
Vue.component('main-footer', Footer);
