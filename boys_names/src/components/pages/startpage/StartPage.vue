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
              <input type="text" class="form-control main-search-control" placeholder="Sok">
              <span class="input-group-btn main-page-search">
              <button class="btn btn-default main-page-search-btn" @click="search" type="submit">
                  <i class="fa fa-search"></i>
              </button>
            </span>
            </div>
            <small id="emailHelp" class="form-text text-muted under-search">Visa Namn Som</small>
          </div>
          <div class="results">
            <div class="results-head">Popular names</div>
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
  data () {
    return {
      popular_names: null
    }
  },
  mounted() {
      axios
      .get("http://127.0.0.1:8000/api/v1/popular-names/?order=rand")
      .then(response => (this.popular_names = response.data));
  },
  methods: {
      search () {
          alert('G!!@')
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
  .input-group{
    padding-left: 10px;
    border-color: #38c8b2;
  }
  .input-group{
    position: relative;
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
    padding-left: 10px;
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
