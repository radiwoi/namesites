<template>
  <div class="names-list container">
    <table class="table table-striped names-table">
      <tbody>
        <tr v-for="nameObj in namesList">
          <td class="fav"><i class="fa fa-heart"></i></td>
          <td class="table-cell namn">
            <span class="popular-rate" v-if="page == 'popular-page'">{{nameObj.popular.position}}</span>
            <span>{{nameObj.name}}</span> <i class="fa fa-info-circle"></i>
            <div class="tooltip main-tooltip">
              <div v-if="nameObj.variants.length > 0" class="variants-list">
                <div class="tooltip-title">
                  Variants
                </div>
                <span v-for="variant in nameObj.variants">
                  {{variant.name}} ({{variant.language}}),
                </span>
              </div>
              <div v-if="nameObj.meaning.length > 0">
                <div class="tooltip-title">Betudelse</div>
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
      <ul class="top-pagination pagination">
       <li class="page-item page-prev" v-bind:class="{disabled: !prev}" @click="paginationClick(prev)"><i class="fa fa-angle-left"></i></li>
       Sida {{page_number}} / {{total_pages}} <i class="fa fa-angle-down"></i>
      <li class="page-item page-next" v-bind:class="{disabled: !next}" @click="paginationClick(next)"><i class="fa fa-angle-right"></i></li>
      </ul>
      <div class="names-counter">{{total_results}} names</div>
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
      namesList: [],
      page: "",
      total_results: 0,
      prev: "",
      next: "",
      total_pages: 1,
      page_number: 1
    }
  },
  methods: {
    paginationClick (value) {
        axios.post(value, this.$store.state.searchObject)
            .then(r => {
                this.namesList = r.data.results;
                this.total_results = r.data.count;
                this.total_pages = this.total_results / this.namesList.length;
                this.prev = r.data.previous;
                this.next = r.data.next;
                this.$store.commit('changeDoSearch', false);
            })
    }
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
//    console.log(this.$route);
    this.page = this.$route.name
    if (this.$route.name == 'search-page') {
      axios.post('http://127.0.0.1:8000/api/v1/test/', this.$store.state.searchObject)
            .then(r => {
                this.namesList = r.data;
                this.$store.commit('changeDoSearch', false);
            })
    }
    if (this.page == 'popular-page') {
        axios.post('http://127.0.0.1:8000/api/v1/popular-names/?limit=5&offset=0', this.$store.state.searchObject)
            .then(r => {
                this.namesList = r.data.results;
                this.total_results = r.data.count;
                this.total_pages = this.total_results / this.namesList.length;
                this.prev = r.data.previous;
                this.next = r.data.next;
                this.$store.commit('changeDoSearch', false);
            })
    }

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
  .page-item {
    cursor: pointer;
    background: #38c8b2;
    color: #fff;
    display: inline-block;
    padding-right: 15px;
    padding-left: 15px;
    padding-top: 7px;
    padding-bottom: 7px;
    border-radius: 5px;
  }
  .page-item.disabled{
    cursor: auto;
    background: rgba(239, 239, 240, 1);
    color: #8c8c8c;
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
    font-size:14px;
    width: 200%;
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
  .tooltip-title{
    font-family: 'Quicksand-Bold';
    margin-bottom: 5px;
  }
  .variants-list{
    margin-bottom: 10px;
    font-family: 'Quicksand';
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
  .popular-rate {
    font-family: 'Quicksand-Bold';
    color: #38c8b2;
  }
</style>
