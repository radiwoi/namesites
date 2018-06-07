<template>
  <div class="names-list container">
    <!--{{ listener }}-->
    <!--{{namesList}}-->
    <div class="filters" style="height:50px"></div>
    <table class="table table-striped names-table">
      <tbody>
        <tr v-for="nameObj in namesList">
          <td class="fav"><i class="fa fa-heart"></i></td>
          <td class="table-cell">{{nameObj.name}} <i class="fa fa-info-circle"></i></td>
          <td class="table-cell">{{nameObj.frequency}} <i class="fa fa-info-circle"></i></td>
          <td class="table-cell">{{nameObj.age_distribution_10}} <i class="fa fa-info-circle"></i></td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <div class="top-pagination"></div>
      <div class="names-counter">{{namesList.length}} names</div>
    </div>
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

<style>
  .names-list{
    font-family: 'Quicksand';
    margin-bottom: 15px;
    margin-top: 15px;
  }
  .names-table {
    text-align: left;
    font-size: 15px;
  }
  .table td {
    padding: 0.65rem;
  }
  .fav{
    text-align: center;
    color: #38c8b2;

  }
  .fav i{
    cursor: pointer;
  }
  .table-cell i{
    margin-left: 3px;
    color: #ceced0;
    cursor: pointer;
  }
  .pagination{
    text-align: center;
    display: block;
    margin-top: 25px;
    margin-bottom: 25px;
  }
  .names-counter{
    text-align: center;
    color: #ceced0;
  }
</style>
