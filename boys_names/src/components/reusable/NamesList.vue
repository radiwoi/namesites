<template>
  <div class="names-list container">
    <table class="table table-striped names-table">
      <tbody>
        <tr v-for="nameObj in namesList">
          <td class="fav" width="10%">
            <div class="make-fav"  v-bind:class="{'active':checkIfFavorite(nameObj.id)}" @click="makeFavorite(nameObj.id)"></div>
          </td>
          <td class="table-cell namn" width="35%">
            <span class="popular-rate" v-if="currentPage == 'popular-page'">{{nameObj.popular.position}}</span>
            <span >{{nameObj.name}}</span> <i v-if="nameObj.variants.length > 0 && nameObj.meaning.length > 0" class="fa fa-info-circle"></i>
            <div v-if="nameObj.variants.length > 0 && nameObj.meaning.length > 0" class="tooltip tooltip-list main-tooltip">
              <div v-if="nameObj.variants.length > 0" class="variants-list">
                <div class="tooltip-title">
                  Variants
                </div>
                <span v-for="variant in nameObj.variants">
                  {{variant.variants}} ({{variant.language}}),
                </span>
              </div>
              <div v-if="nameObj.meaning.length > 0">
                <div class="tooltip-title">Betudelse</div>
                {{nameObj.meaning}}
              </div>
            </div>
          </td>
          <td class="table-cell frequency" width="35%">
            {{nameObj.frequency}} <i class="fa fa-info-circle"></i>
            <div class="tooltip tooltip-list freq-tooltip">{{nameObj.total_bearing_name}} personer bar detta namn</div>
          </td>
          <td class="table-cell dist-age d-none d-sm-table-cell" width="20%">
            {{nameObj.average_age}} år<i class="fa fa-info-circle"></i>
            <div class="tooltip tooltip-list chart-tooltip">
              <div class="chart-top">
                <div class="green-cols-wrapper">
                  <span class="a" style="height:100%; width: 30px; background: transparent"></span>
                  <span class="a" :style="{'height': style(nameObj.age_distribution_10) + '%'}">
                    <span class="percents">{{nameObj.age_distribution_10}}%</span>
                  </span>
                  <span class="a" :style="{'height': style(nameObj.age_distribution_20) + '%'}">
                    <span class="percents">{{nameObj.age_distribution_20}}%</span>
                  </span>
                  <span class="a" :style="{'height': style(nameObj.age_distribution_30) + '%'}">
                    <span class="percents">{{nameObj.age_distribution_30}}%</span>
                  </span>
                  <span class="a" :style="{'height': style(nameObj.age_distribution_50) + '%'}">
                    <span class="percents">{{nameObj.age_distribution_50}}%</span>
                  </span>
                  <span class="a" :style="{'height': style(nameObj.age_distribution_70) + '%'}">
                    <span class="percents">{{nameObj.age_distribution_70}}%</span>
                  </span>
                  <span class="a" :style="{'height': style(nameObj.age_distribution_71) + '%'}">
                    <span class="percents">{{nameObj.age_distribution_71}}%</span>
                  </span>
                </div>
              </div>
              <div class="chart-bottom">
                <span style="width: 45px;" class="item-chart-label">Alder:</span>
                <span class="item-chart-label">0-10</span>
                <span class="item-chart-label">11-20</span>
                <span class="item-chart-label">21-30</span>
                <span class="item-chart-label">31-50</span>
                <span class="item-chart-label">51-70</span>
                <span class="item-chart-label">71 ></span>
              </div>

            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="namesList.length > 0" class="pagination">
      <ul class="top-pagination pagination">
       <li class="page-item page-prev" v-bind:class="{disabled: !prev}" @click="paginationClick(prev)"><i class="fa fa-angle-left"></i></li>
       <span @click="showPageTooltip = !showPageTooltip" class="page-counter">
         Sida {{page_number}} / {{total_pages}} <i class="fa fa-angle-down"></i>
         <div v-if="showPageTooltip" class="tooltip page-tooltip">
           <div class="p-item" @click="pagesTooltipClick(p)" v-for="p in total_pages_arr">
              {{p}} / {{total_pages}}
           </div>
         </div>
       </span>
      <li class="page-item page-next" v-bind:class="{disabled: !next}" @click="paginationClick(next)"><i class="fa fa-angle-right"></i></li>
      </ul>
      <div class="names-counter">{{total_results}} names</div>
    </div>
    <div v-if="isLoad" class="loader-wrapper">
      <div class="loader"></div>
    </div>
    <div v-if="noResults" class="alert alert-info">No results found</div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
  name: 'names-list',
  data () {
    return {
      urlsMapper:{
        "search-page": "boy-names",
        "popular-page": "popular-names",
        "favorite-page": "favorite-names",
      },
      namesList: [],
      showPageTooltip: false,
      total_pages_arr: [],
      currentPage: "",
      isLoad: true,
      noResults: false,
      total_results: 0,
      prev: "",
      next: "",
      total_pages: 1,
      page_number: 1,
      part: 'test',
      backend_url: "http://34.254.119.140/api/v1/",
//      backend_url: "http://names_project.devhost1.com/api/v1/"
    }
  },
  methods: {
    paginationClick (value) {
        if(value !== null) {
            let urlParams = new URLSearchParams(value);
            value = value.replace('http://localhost:8000/api/v1/', this.backend_url);
            axios.post(value, this.searchObject)
            .then(r => {
                this.prepareResponseData(r);
                if(!parseInt(urlParams.get('offset'))){
                    this.page_number = 1;
                }
                else {
                    this.page_number = parseInt(urlParams.get('offset')) / this.searchObject.limit + 1;
                }
            })
            .catch(error => { this.prepareRejectData(error) });
        }
    },
    pagesTooltipClick(value){
      let data = this.getRequestData();
      data['url'] = this.backend_url + this.urlsMapper[this.currentPage] + "/?limit=" + this.searchObject.limit + "&offset=" + this.searchObject.limit * (value - 1);
      axios.post(
        data['url'],
        data["postData"]
      ).then(r => {
          this.prepareResponseData(r);
          this.page_number = value;
      })
      .catch(error => { this.prepareRejectData(error) });
    },
    prepareResponseData(r){
        if(r.data.results == 0){
            this.noResults = true;
        }
        this.namesList = r.data.results;
        this.total_results = r.data.count;
        this.prev = r.data.previous;
        this.next = r.data.next;
        this.total_pages = Math.ceil(this.total_results / this.searchObject.limit);
        this.$store.commit('changeDoSearch', false);
        this.isLoad = false;
        this.total_pages_arr = [];
        for(let i=1; i <= this.total_pages; i++){
            this.total_pages_arr.push(i);
        }
    },
    prepareRejectData(error) {
      this.noResults = true;
      this.isLoad = false;
      this.page_number = 1;
      this.prev = false;
      this.next = false;
      this.$store.commit('changeDoSearch', false);
    },
    makeFavorite(nameId) {
        //      todo make through store commit
        if (this.checkIfFavorite(nameId)){
          let index = this.listFav.indexOf(nameId);
          this.listFav.splice(index, 1);
        } else {
          this.listFav.push(nameId);
        }
        this.$store.commit('changeListFav', this.listFav);
        if(this.$route.name == 'favorite-page') {
            this.$store.commit('changeDoSearch', true);
        }
    },
    checkIfFavorite(id){
        if(this.listFav.includes(id)){
          return true;
        }
    },
    getRequestData(){
      let postData = this.searchObject;
      postData.ids = this.listFav;
      let url = this.backend_url + this.urlsMapper[this.currentPage] + "/?limit=" + this.searchObject.limit + "&offset=" + this.searchObject.skip;
      let requestData = {
        "postData": postData,
        "url": url
      };
      return requestData;
    },
    style (width) {
      if(width == 100) {
          return 70;
      } if(width == 0) {
          return 5;
      } else {
        return width + 10
      }
    }
  },
  computed: {
    ...mapGetters({
      doSearch: 'getDoSearch',
      listFav: 'getListFav',
      searchObject: "getSearchObject"
    })
  },
  mounted () {
    this.currentPage = this.$route.name;
    let requestData = this.getRequestData();
      axios
      .post(
        requestData['url'],
        requestData["postData"]
      )
      .then(r => { this.prepareResponseData(r);})
      .catch(error => { this.prepareRejectData(error) });
  },
  watch: {
    doSearch: function (n, o) {
      if(!n){
          return
      }
      this.isLoad = true;
      this.noResults = false;
      this.namesList = [];

      let requestData = this.getRequestData();

      if (n) {
          axios.post(
            requestData['url'],
            requestData["postData"]
          ).then(r => {
              this.prepareResponseData(r);
              this.page_number = 1;
          })
          .catch(error => { this.prepareRejectData(error) });
      }
    }
  }
}
</script>

<style>
  .names-list{
    font-family: 'Quicksand';
    margin-bottom: 15px;
    /*margin-top: 15px;*/
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
  .make-fav{
    background: url("../../assets/Heart.png");
    background-repeat: no-repeat;
    background-position: 1px 5px;
    width: 25px;
    height: 25px;
    background-size: contain;
    margin: 0 auto;
    cursor: pointer;
  }
  .make-fav.active {
    background: url("../../assets/Heart-filled.png");
    background-repeat: no-repeat;
    background-position: 1px 5px;
    width: 25px;
    height: 25px;
    background-size: contain;
    margin: 0 auto;
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
    position: relative;
    cursor: pointer;
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
  .frequency, .namn, .dist-age{
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
  .main-tooltip {
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
  .chart-tooltip{
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
    right:0%;
    min-width: 400px;
    box-shadow: 0px 2px 15px #8edcd1;
  }
  .chart-top {
    height: 100px;
    position: relative;
  }
  .green-cols-wrapper{
    position: absolute;
    bottom:0;
    width: 100%;
    height: 100%;
  }
  .a{
    background: #38c8b2;
    display: inline-block;
    width: 40px;
    margin-right: 10px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    position: relative;
  }
  .item-chart-label{
    width: 50px;
    display: inline-block;
    font-size: 13px;
  }
  .percents{
    font-family: "Quicksand-Bold";
    position: absolute;
    top: -22px;
    left: 8px;
  }
  .popular-rate {
    font-family: 'Quicksand-Bold';
    color: #38c8b2;
  }
  .loader {
    border: 8px solid rgba(239, 239, 240, 1);
    border-radius: 50%;
    border-top: 8px solid #38c8b2;
    width: 50px;
    height: 50px;
    -webkit-animation: spin 2s linear infinite; /* Safari */
    animation: spin 2s linear infinite;
    margin: 0 auto;
  }
  .page-tooltip {
    font-family: 'Quicksand';
    display: block;
    top: 100%;
    right:-10px;
    opacity: 1;
    background: #fff;
    padding-top: 3px;
    padding-bottom: 10px;
    padding-left: 0px;
    padding-right: 0px;
    box-shadow: 0px 2px 15px #8edcd1;
    width: 120px;
    max-height: 288px;
    overflow: auto;
    text-align: left;
    font-size: 16px;
  }
  .tooltip-list {
    pointer-events: none;
  }
  .p-item{
    cursor: pointer;
    width: 100%;
    padding-left: 25px;
  }
  .p-item:hover{
    cursor: pointer;
    background: #eafffc;
  }

  /* Safari */
  @-webkit-keyframes spin {
    0% { -webkit-transform: rotate(0deg); }
    100% { -webkit-transform: rotate(360deg); }
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }


  @media (max-width: 1200px) {}

  @media (max-width: 992px) {}

  @media (max-width: 768px) {}

  @media (max-width: 576px) {
    .names-table td{
      padding: 0.25rem;
    }
  }

</style>
