export default {
  state: {
    searchObject: {
      // "frequency": ["Ovanligt", "Mindre vanligt", "Mycket vanligt", "Mycket ovanligt", "Ganska vanligt", "Vanligt"],
      "frequency": [],
      // "age_distribution": [10,20,30,50,70],
      "age_distribution": [],
      "popular_year": 2016,
      "double_name": false,
      "letters_range": [],
      "search_phrase": "",
      "search_criteria": "start",
      "limit": 13,
      "skip": 0
    },
    availableYears: [],
    doSearch: false,
    listFav: typeof localStorage.getItem('listFav') === 'undefined' ?  localStorage.getItem('listFav'): [],
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
      state.listFav = value
    },
    changeDoSearch (state, value) {
      state.doSearch = value
    }
  },
  actions: {
    test(context) {
      context.commit('test')
    }
  },
  getters: {
    getDoSearch: state => state.doSearch,
    getListFav: state => state.listFav
  }
}
