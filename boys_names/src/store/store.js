export default {
  state: {
    searchObject: {
      "frequency": ["Ovanligt", "Mindre vanligt", "Mycket vanligt", "Mycket ovanligt", "Ganska vanligt", "Vanligt"],
      "age_distribution": [10,20,30,50,70],
      "popular_year": 2016,
      "double_name": false,
      "letters_range": false,
      "search_phrase": "",
      "search_criteria": "start",
      "limit": 13,
      "skip": 0
    },
    availableYears: [],
    doSearch: false
  },
  mutations: {
    test (state, value) {
      state.searchObject.search_phrase = value
    },
    changeCriteria (state, value) {
      state.searchObject.search_criteria = value
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
    getDoSearch: state => state.doSearch
  }
}
