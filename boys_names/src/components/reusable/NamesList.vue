<template>
  <div class="names-list">
    {{ listener }}
    {{namesList}}
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
  name: 'names-list',
  data () {
    return {
      namesList: []
    }
  },
  methods: {
//    onClickChild (value) {
//        console.log(value)
//    }
  },
//  beforeMount () {
//    console.log(this.$store.state.doSearch)
//
//  },
  computed: {
    listener () {
      return this.$store.state.doSearch
    },
    ...mapGetters({
      doSearch: 'getDoSearch'
    })
  },
  mounted () {
//    console.log(this.doSearch)
    axios.post('http://127.0.0.1:8000/api/v1/test/', this.$store.state.searchObject)
            .then(r => {
                this.namesList = r.data
                this.$store.commit('changeDoSearch', false);
            })
  },
  watch: {
      doSearch: function (n, o) {
        console.log(n, o)
        if (n) {
            axios.post('http://127.0.0.1:8000/api/v1/test/', this.$store.state.searchObject)
            .then(r => {
                this.namesList = r.data
                this.$store.commit('changeDoSearch', false);
            })
        }
      }
  }
}
</script>
