export default {
  state: {
    searchObject: {
      "frequency": ["Ovanligt", "Mindre vanligt", "Mycket vanligt", "Mycket ovanligt", "Ganska vanligt", "Vanligt"],
      // "frequency": [],
      "age_distribution": [10,20,30,50,70,71],
      // "age_distribution": [],
      "popular_year": 2017,
      "double_name": false,
      "letters_range": [true, "1 - 3", "4 - 5", "6 - 7", "8 - 9", "9 >"],
      "search_phrase": "",
      "search_criteria": "start",
      "limit": 40,
      "skip": 0
    },
    availableYears: [],
    doSearch: false,
    doResetFilters: false,
    listFav: localStorage.getItem("listFav") == null || localStorage.getItem("listFav") == undefined ?  [] : JSON.parse(localStorage.getItem('listFav')),
  },

  mutations: {
    test (state, value) {
      state.searchObject.search_phrase = value
    },
    changeCriteria (state, value) {
      state.searchObject.search_criteria = value
    },
    changeLettersRange (state, value) {
      state.searchObject.letters_range = value
    },
    changeAgeDistribution (state, value) {
      state.searchObject.age_distribution = value
    },
    changeFrequency (state, value) {
      state.searchObject.frequency = value
    },
    changeListFav (state, value) {
      state.listFav = value;

      localStorage.setItem('listFav', JSON.stringify(state.listFav))
    },
    changePopularYear(state, value) {
      state.searchObject.popular_year = value;
    },
    changeDoSearch (state, value) {
      state.doSearch = value
    },
    changeDoResetFilters (state, value) {
      state.doResetFilters = value
    }
  },
  actions: {
    test(context) {
      context.commit('test')
    }
  },
  getters: {
    getDoSearch: state => state.doSearch,
    getDoResetFilters: state => state.doResetFilters,
    getListFav: state => state.listFav,
    getSearchObject: state => state.searchObject,
  }
}
