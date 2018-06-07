export default {
  state: {
    searchObject: {
      "frequency": ["Ovanligt", "Mindre vanligt"],
      "age_distribution": [10,20,30],
      "double_name": false,
      "letters_range": "4 - 5",
      "search_phrase": "",
      "search_criteria": "start",
      "limit": 5,
      "skip": 0
    }
  },
  mutations: {
    test (state, value) {
      state.searchObject.search_phrase = value
    },
    changeCriteria (state, value) {
      state.searchObject.search_criteria = value
    }
  },
  actions: {
    test(context) {
      context.commit('test')
    }
  }
}
