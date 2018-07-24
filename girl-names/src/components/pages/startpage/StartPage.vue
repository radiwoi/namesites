<template>
  <div>
    <div class="start-page">
      <main-header></main-header>
      <div class="container">
        <div class="start-page-title">Letar du efter ett namn till din dotter?</div>
        <div class="start-page-subtitle">Sök bland svenska flicknamn och unisexnamn</div>
        <div class="row start-page-form">
          <div class="col col-lg-2 d-none d-sm-block"><img class="img-fluid1 woman-png hidden-sm"
                                                           src="../../../assets/Woman.png" alt=""></div>
          <div class="col col-lg-6 offset-lg-1 start-page-core col-sm-12">
            <search-form></search-form>
            <div class="results">
              <router-link v-bind:to="'/populara'">
                <div class="results-head">Populära namn</div>
              </router-link>
              <div class="results-wrapper row">
                <div v-for="item in popular_names" class="col-lg-3 col-4">
                  <router-link v-bind:to="'/populara'">
                    {{item.name}}
                  </router-link>
                </div>
              </div>
            </div>
          </div>
          <div class="col col-lg-3 d-none d-sm-block"><img class="img-fluid1" src="../../../assets/Man.png" alt="">
          </div>
        </div>
      </div>
    </div>
    <main-footer></main-footer>
  </div>
</template>

<!--http://names_project.devhost1.com-->
<script>
import axios from 'axios'
export default {
  name: 'start-page',
  metaInfo: {
    title: 'Flicknamn.se - Sök bland svenska flicknamn och tjejnamn',
     meta: [
      { name: 'description', content: 'Sök och bläddra bland svenska flicknamn och unisexnamn. Inspireras och få uppslag till namn. Se hur vanligt förekommande olika namn är i olika åldrar.' }
    ]
  },
  props: [''],
  data () {
    return {
      popular_names: null,
    }
  },
  mounted() {
      axios
      .get("https://flicknamn.se/api/v1/popular-names/?order=rand&is_girl_name=True")
      .then(response => (this.popular_names = response.data));
  },
  methods: {

  }
}
</script>

<style>
  .start-page {
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

  .results a, .results a:hover, .results a:focus, .results a:active {
    color: #424242;
    text-decoration: none;
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

  @media (max-width: 1200px) {}

  @media (max-width: 992px) {}

  @media (max-width: 768px) {}

  @media (max-width: 576px) {
    .start-page-subtitle{
      margin-top: 20px;
      line-height: 1;
    }
  }
</style>
