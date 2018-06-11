<template>
  <div class="names-list container">
    <table class="table table-striped names-table">
      <tbody>
        <tr v-for="nameObj in namesList">
          <td class="fav"><i class="fa fa-heart"></i></td>
          <td class="table-cell namn">
            {{nameObj.name}} <i class="fa fa-info-circle"></i>
            <div class="tooltip main-tooltip">
              <div v-for="variant in nameObj.variants">
                {{variant.name}} ({{variant.language}}),
              </div>
              <div v-if="nameObj.meaning.length > 0">
                {{nameObj.meaning}}
              </div>
            </div>
          </td>
          <td class="table-cell frequency">
            {{nameObj.frequency}} <i class="fa fa-info-circle"></i>
            <div class="tooltip freq-tooltip">{{nameObj.total_bearing_name}} personer bar detta namn</div>
          </td>
          <td class="table-cell">{{nameObj.average_age}} ar<i class="fa fa-info-circle"></i></td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <div class="top-pagination">

      </div>
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
    axios.post('http://127.0.0.1:8000/api/v1/test/', this.$store.state.searchObject)
            .then(r => {
                this.namesList = r.data
                this.$store.commit('changeDoSearch', false);
            })
  },
  watch: {
    doSearch: function (n, o) {
      if (n) {
          axios.post('http://127.0.0.1:8000/api/v1/test/', this.$store.state.searchObject)
          .then(r => {
              this.namesList = r.data;
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
    border-color: #fafafa;
  }
  .names-table td {
    padding: 0.65rem;
    border-color: #fafafa;
    border-right: 2px solid #fff;
  }
  .names-table tbody tr:nth-of-type(odd) {
    background-color: #fafafa;
    border-color: #fafafa;
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
  .frequency, .namn{
    position: relative;
  }
  .fa-info-circle:hover + .tooltip{
    /*opacity: 1;*/
    z-index: 2;
    display: block;
  }
  .main-tooltip{
    font-family: 'Quicksand';
    font-size:15px;
    opacity: 1;
    z-index: 0;
    display: none;
    padding: 10px;
    padding-right: 10px;
    padding-left: 10px;
    background: #ffffff;
    top:0px;
    left: 0;
    box-shadow: 0px 2px 15px #8edcd1;
  }
  .freq-tooltip{
    font-family: 'Quicksand';
    font-size:16px;
    opacity: 1;
    z-index: 0;
    display: none;
    padding: 10px;
    padding-right: 10px;
    padding-left: 10px;
    background: #ffffff;
    top:0px;
    left: 0;
    box-shadow: 0px 2px 15px #8edcd1;
  }
</style>
