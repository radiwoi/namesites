<template>
  <div class="names-list container">
    <table-view v-bind:namesList="namesList" v-bind:currentPage="currentPage" v-bind:listFav="listFav"></table-view>
    <div v-if="namesList.length > 0" class="pagination">
      <div v-if="currentPage !== 'favorite-page'">
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
      </div>
      <div class="names-counter">{{total_results}} namn</div>
    </div>
    <div v-if="isLoad" class="loader-wrapper">
      <div class="loader"></div>
    </div>
    <div v-if="noResults" class="alert alert-info">Din sökning gav inga träffar</div>
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
      showPageTooltip:false,
      namesList: [],
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
      backend_url: "https://pojknamn.se/api/v1/",
//      backend_url: "http://names_project.devhost1.com/api/v1/"
    }
  },
  methods: {
    paginationClick(value) {
      if (value !== null) {
        let urlParams = new URLSearchParams(value);
        let element = document.getElementsByClassName("filters")[0];
        let top = element.offsetTop;
        value = value.replace('http://localhost:8000/api/v1/', this.backend_url);
        axios.post(value, this.searchObject)
          .then(r => {
            window.scrollTo(0, top);
            this.prepareResponseData(r);
            if (!parseInt(urlParams.get('offset'))) {
              this.page_number = 1;
            }
            else {
              this.page_number = parseInt(urlParams.get('offset')) / this.searchObject.limit + 1;
            }
          })
          .catch(error => {
            this.prepareRejectData(error)
          });
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
    getRequestData(){
      let postData = this.searchObject;
      postData.ids = this.listFav;
      let url = (this.currentPage != 'favorite-page') ? this.backend_url + this.urlsMapper[this.currentPage] + "/?limit=" + this.searchObject.limit + "&offset=" + this.searchObject.skip : this.backend_url + this.urlsMapper[this.currentPage] + "/?limit=10000&offset=0";
      let requestData = {
        "postData": postData,
        "url": url
      };
      return requestData;
    },
  },
  created() {
    let self = this;

    window.addEventListener('click', function(e){
      if (!self.$el.contains(e.target) ||
        e.target.classList.contains('pagination') ||
        e.target.classList.contains('names-counter') ||
        e.target.classList.contains('names-list') ||
        e.target.classList.contains('table-cell') ||
        e.target.classList.contains('fa-info-circle')){
        self.showPageTooltip = false
      }
    })
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

<style scoped>
  .names-list{
    font-family: 'Quicksand';
    margin-bottom: 15px;
    /*margin-top: 15px;*/
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
  .names-counter{
    text-align: center;
    color: #ceced0;
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
    box-shadow: 0px 2px 15px #dc8796;
    width: 120px;
    max-height: 288px;
    overflow: auto;
    text-align: left;
    font-size: 16px;
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
  .p-item{
    cursor: pointer;
    width: 100%;
    padding-left: 25px;
  }
  .p-item:hover{
    cursor: pointer;
    background: #eafffc;
  }
  .p-item{
    cursor: pointer;
    width: 100%;
    padding-left: 25px;
  }
  .p-item:hover{
    cursor: pointer;
    background: #fff9f8;
  }

  .alert-info {
    background: #38c8b2;
    border: 2px solid #38c8b2;
    height: 52px;
    box-shadow: 0px 2px 5px #8edcd1;
    font-family: 'Quicksand';
    border-radius: 5px;
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
    .names-list.container{
      padding: 0;
    }
  }

</style>
