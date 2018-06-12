<template>
  <div class="names-list container">
    <table class="table table-striped names-table">
      <tbody>
        <tr v-for="nameObj in namesList">
          <td class="fav"><i class="fa fa-heart"></i></td>
          <td class="table-cell namn">
            <span class="popular-rate" v-if="currentPage == 'popular-page'">{{nameObj.popular.position}}</span>
            <span>{{nameObj.name}}</span> <i class="fa fa-info-circle"></i>
            <div v-if="nameObj.variants.length > 0 && nameObj.meaning.length > 0" class="tooltip main-tooltip">
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
    <div v-if="namesList.length > 0" class="pagination">
      <ul class="top-pagination pagination">
       <li class="page-item page-prev" v-bind:class="{disabled: !prev}" @click="paginationClick(prev, 'prev')"><i class="fa fa-angle-left"></i></li>
       <span class="page-counter">
         Sida {{page_number}} / {{total_pages}} <i class="fa fa-angle-down"></i>
       </span>
      <li class="page-item page-next" v-bind:class="{disabled: !next}" @click="paginationClick(next, 'next')"><i class="fa fa-angle-right"></i></li>
      </ul>
      <div class="names-counter">{{total_results}} names</div>
    </div>
    <div v-if="namesList.length == 0" class="alert alert-info">No results found</div>
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
      currentPage: "",
      total_results: 0,
      prev: "",
      next: "",
      total_pages: 1,
      page_number: 1,
      part: 'test',
//      backend_url: "http://127.0.0.1:8000/api/v1/",
      backend_url: "http://names_project.devhost1.com/api/v1/"
    }
  },
  methods: {
    paginationClick (value, direction) {
        let urlParams = new URLSearchParams(value);

        if(value !== null) {
            axios.post(value, this.$store.state.searchObject)
            .then(r => {
                this.prepareResponseData(r);
                if(!parseInt(urlParams.get('offset'))){
                    this.page_number = 1;
                }
                else {
                    this.page_number = parseInt(urlParams.get('offset')) / this.$store.state.searchObject.limit + 1;
                }
            })
        }
    },
    prepareResponseData(r){
        this.namesList = r.data.results;
        this.total_results = r.data.count;
        this.prev = r.data.previous;
        this.next = r.data.next;
        this.total_pages = Math.ceil(this.total_results / this.$store.state.searchObject.limit);
        this.$store.commit('changeDoSearch', false);
    }
  },
  computed: {
    listener () {
      return this.$store.state.doSearch
    },
    ...mapGetters({
      doSearch: 'getDoSearch'
    })
  },
  mounted () {
    this.currentPage = this.$route.name;
    if (this.$route.name == 'search-page') {
      axios.post(this.backend_url + 'test/?limit=5&offset=0', this.$store.state.searchObject)
            .then(r => {
                this.prepareResponseData(r);
            })
    }
    if (this.currentPage == 'popular-page') {
        axios.post(this.backend_url + 'popular-names/?limit=5&offset=0', this.$store.state.searchObject)
            .then(r => {
                this.prepareResponseData(r);
            })
    }

  },
  watch: {
    doSearch: function (n, o) {
        console.log("watch", n, o);
//      todo from ALL pages
      if(this.currentPage == 'popular-page'){
          this.part = 'popular-names'
      } else {
          this.part = 'test'
      }
      if (n) {
          axios.post(this.backend_url + this.part + '/?limit=5&offset=0', this.$store.state.searchObject)
          .then(r => {
              this.prepareResponseData(r);
              this.page_number = 1;
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
    outline-style:none;

  }
  .top-pagination, .top-pagination:before, .top-pagination:after {
    -webkit-user-select: none; /* Chrome/Safari */
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* IE10+ */
}
  .page-counter {
    -webkit-tap-highlight-color:transparent;
    outline-style:none;
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
  .namn{
    max-width: 297px;
  }
  .frequency, .namn{
    position: relative;
  }
  .fa-info-circle:hover + .tooltip,
  .fa-info-circle:focus + .tooltip,
  .fa-info-circle:active + .tooltip{
    /*opacity: 1;*/
    z-index: 2;
    display: block;
  }
  .fa-info-circle:hover{
    /*z-index: 50;*/
    /*opacity: 0;*/
    /*position: absolute;*/
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
    top:25px;
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
    top:25px;
    left: 0;
    box-shadow: 0px 2px 15px #8edcd1;
  }
  .popular-rate {
    font-family: 'Quicksand-Bold';
    color: #38c8b2;
  }
</style>
