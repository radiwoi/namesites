<template>
  <div class="names-list container">
    <table-view v-bind:namesList="namesList" v-bind:currentPage="currentPage" v-bind:listFav="listFav"></table-view>
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
      data['url'] = this.backend_url + this.urlsMapper[this.currentPage] + "/?limit=" + this.searchObject.limit + "&offset=" + this.searchObject.limit * (value - 1) + "&is_girl_name=True";
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
      let url = this.backend_url + this.urlsMapper[this.currentPage] + "/?limit=" + this.searchObject.limit + "&offset=" + this.searchObject.skip + "&is_girl_name=True";
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
      if (!self.$el.contains(e.target)){
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
