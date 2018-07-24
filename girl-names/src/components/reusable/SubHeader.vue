<template>
  <div class="subheader">
    <div class="container">
      <div class="row">
        <div class="col-9 col-lg-6 sub-menu">
          <!--<router-link v-bind:to="'/sokresultat'">-->
            <!--<span class="sub-menu-item" v-bind:class="{active: page == 'search-page'}">Sökning</span>-->
          <!--</router-link>-->
          <router-link v-bind:to="'/populara'">
            <span class="sub-menu-item" v-bind:class="{active: page == 'popular-page'}">Populära namn</span>
          </router-link>
          <router-link class="d-none d-sm-inline" v-bind:to="'/mina-favoriter'">
            <span class="sub-menu-item" v-bind:class="{active: page == 'favorite-page'}">Mina favoriter</span>
          </router-link>
        </div>
        <div class="col-3 col-lg-2 offset-lg-4 right-sub">
          <a :href="boy_names_site">
            <img class="img-fluid sub-img d-none d-sm-block" src="../../assets/Logo-boy.png" alt="">
          </a>
          <a :href="boy_names_site">
            <img class="img-fluid1 sub-img d-block d-sm-none" src="../../assets/Logo-boy-mobile.png" alt="">
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sub-header',
  data () {
      return {
        page: "",
        boy_names_site: "http://pojknamn.se"
      }
  },
  mounted () {
      this.page = this.$route.name
  }
}
</script>

<style>
  .subheader{
    /*border-bottom: 1px solid #43c0ae;*/
    box-shadow: 0px 2px 5px rgba(255, 111, 114, 0.25);
    padding-top: 15px;
    padding-bottom: 5px;
  }
  .sub-menu{
    font-family: 'Quicksand-Bold';
    font-size: 20px;
    text-align: left;
    padding-top: 5px;
  }
  .sub-menu-item{
    display: inline-block;
    margin-right: 20px;
    margin-top: 5px;
    height: 100%;
  }
  .sub-menu a, .sub-menu a:hover, .sub-menu a:focus {
    text-decoration: none;
    color: #2c3e50;
  }
  .sub-menu-item.active{
    border-bottom: 2px solid #F88580;
  }
  .subheader{
    padding: 5px;
  }
  .sub-img{
    max-width: 82%;
  }
  @media (max-width: 1200px) {}

  @media (max-width: 992px) {}

  @media (max-width: 768px) {
    .sub-menu {
      font-family: 'Quicksand-Bold';
      font-size: 16px;
    }
  }

  @media (max-width: 576px) {
    /*.sub-menu-item{*/
      /*height: 100%;*/
    /*}*/
    .sub-menu-item {
      margin-right: 5px;
    }
    .right-sub{
      text-align: right;
    }
    .sub-img{
      max-width: 100%;

    }
  }

</style>
