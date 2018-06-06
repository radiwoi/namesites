<template>
  <div class="start-page">
    <div class="container">
      <div class="start-page-title">Dags att hitta ett namn till er son?</div>
      <div class="start-page-subtitle">Sok bland Sveriges samthiga pojknamn</div>
      <div class="row start-page-form">
        <div class="col col-lg-2"><img class="img-fluid1 woman-png" src="../../../assets/Woman.png" alt=""></div>
        <div class="col col-lg-6 offset-lg-1 start-page-core">
          <div class="form">
            <div class="input-group">
              <input type="text" class="form-control main-search-control" placeholder="Sok" v-model="searchInput">
              <span class="input-group-btn main-page-search">
              <router-link v-bind:to="{name: 'search-page', params: {'searchInput': searchInput}}">
                <button class="btn btn-default main-page-search-btn" @click="search" type="submit">
                    <i class="fa fa-search"></i>
                </button>
              </router-link>
            </span>
            </div>
            <small id="emailHelp" class="form-text text-muted under-search">
              Visa Namn Som
              <span class="search-criteria" @click="chooseCriteriaWindow">{{search_criteria.name}} <i class="fas fa-angle-down"></i>
                <div v-if="seen" class="criterias-list">
                  <div v-for="criteria, index in criterias" @click="chooseCriteria(index)" v-if="!criteria.chosen">{{criteria.name}}</div>
                </div>
              </span>
            </small>
          </div>
          <div class="results">
            <router-link v-bind:to="'/popular-page'">
              <div class="results-head">Popular names</div>
            </router-link>
            <div class="results-wrapper row">
              <div v-for="item in popular_names" class="col-lg-3">
                {{item.name}}
              </div>
            </div>
          </div>
        </div>
        <div class="col col-lg-3"><img class="img-fluid1" src="../../../assets/Man.png" alt=""></div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default {
  name: 'start-header',

  props: [''],
  data () {
    return {
      popular_names: null,
      seen: false,
      search_criteria: {name: "borjar med sokstrangen ", action: "start"},
      criterias: [
          {name: "innehar sokstrangen", action: "middle", chosen: false},
          {name: "borjar med sokstrangen ", action: "start", chosen: true},
          {name: "slutar med sokstrangen", action: "end", chosen: false},
      ],
      searchInput: ''
    }
  },
  mounted() {
      axios
      .get("http://127.0.0.1:8000/api/v1/popular-names/?order=rand")
      .then(response => (this.popular_names = response.data));
  },
  methods: {
      search () {
          alert('G!!@');
      },
      chooseCriteriaWindow () {
          this.seen = !this.seen
      },
      chooseCriteria (index) {
        console.log(this.criterias[index])
        this.criterias.map(criteria => { return criteria.chosen = false });
        this.criterias[index]['chosen'] = true;
        this.search_criteria = this.criterias[index];
      }
  }
}
</script>

<style>
  .start-page {
    margin-top: 40px;
    margin-bottom: 20px;
  }
  .start-page-title{
    font-family: "Quicksand-Bold";
    font-weight: bold;
    font-size: 48px;
    line-height: 56px;
  }
  .start-page-subtitle{
    font-family: "Quicksand";
    font-size: 28px;
    line-height: 64px;
  }
  .start-page-form{
    margin-top: 40px;
  }
  .woman-png{
    margin-top: 40px;
  }
  .form{
    padding-left: 20px;
    padding-right: 20px;
  }
  .input-group{

    border-color: #38c8b2;
  }
  .input-group{
    position: relative;
  }
  .results a, .results a:hover, .results a:focus, .results a:active {
    color: #424242;
    text-decoration: none;
  }
  .main-page-search{
    position: absolute;
    right: 0;
    z-index: 4;
  }
  .main-page-search-btn{
    background: #38c8b2;
    color: #fff;
    height:52px;
    width: 53px;
    border: 2px solid #38c8b2;
  }
  .main-search-control{
    border: 2px solid #38c8b2;
    height: 52px;
  }
  .main-search-control:focus{
    /*color: #38c8b2;*/
    background-color: #fff;
    border-color: #38c8b2;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(29, 255, 92, 0.25);
  }
  .under-search{
    color: #424242;
    font-family: 'Quicksand';
    font-size: 14px;
    text-align: left;

  }
  .search-criteria{
    font-family: 'Quicksand-Bold';
    cursor: pointer;
    position: relative;
  }
  .criterias-list{
    position: absolute;
    padding-left: 15px;
    padding-top: 10px;
    border:1px solid #38c8b2;
    height: 70px;
    width: 210px;
    right:-15px;
    background: #ffffff;
    z-index: 5;
    line-height: 25px;
  }
  .results-head{
    font-family: 'Quicksand-Bold';
    margin-bottom: 15px;
    line-height: 40px;
    margin-top: 30px;
  }
  .results-wrapper{
    font-family: 'Quicksand';
    line-height: 32px;
    font-size: 15px;
  }
</style>
