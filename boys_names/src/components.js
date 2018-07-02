import Vue from 'vue'

import Header from './components/reusable/Header.vue'
import SecondHeader from './components/reusable/SecondHeader.vue'
import SubHeader from './components/reusable/SubHeader.vue'
import Footer from './components/reusable/Footer.vue'
import StartPage from './components/pages/startpage/StartPage.vue'
import SearchPage from './components/pages/searchpage/SearchPage.vue'
import PopularPage from './components/pages/popularpage/PopularPage.vue'
import FavoritePage from './components/pages/favoritepage/FavoritePage.vue'
import SearchForm from './components/reusable/SearchForm.vue'
import NamesList from './components/reusable/NamesList.vue'
import Filters from './components/reusable/Filters.vue'
import YearsFilter from './components/reusable/YearsFilter.vue'
import TableView from './components/reusable/TableView.vue'

Vue.component('main-header', Header);
Vue.component('second-header', SecondHeader);
Vue.component('start-page', StartPage);
Vue.component('search-page', SearchPage);
Vue.component('popular-page', PopularPage);
Vue.component('favorite-page', FavoritePage);


// reusable components
Vue.component('search-form', SearchForm);
Vue.component('main-footer', Footer);
Vue.component('names-list', NamesList);
Vue.component('sub-header', SubHeader);
Vue.component('filters', Filters);
Vue.component('years-filter', YearsFilter);
Vue.component('table-view', TableView);
