<template>
  <div class="second-header">
    <div class="container">
      <div class="row">
        <div class="col col-lg-3 logo-wrapper">
          <router-link v-bind:to="'/'">
            <img class="sec-img img-fluid" src="../../assets/Boy.png" alt="">
          </router-link>
        </div>
        <div class="col-lg-6 offset-lg-2">
          <search-form></search-form>
        </div>
        <div class="col-lg-1">
          <!--<img src="" alt="">-->
          <router-link  v-bind:class="{'active':favoriteCount > 0}" class="popular-wrapper" to="/favorite-page">
            <span class="fav-counter">{{favoriteCount}}</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'second-header',
  data () {
    return {
      favoriteCount: 0
    }
  },
  computed: {
    ...mapGetters({
      listFav: 'getListFav'
    })
  },
  mounted() {
    this.favoriteCount = this.listFav.length;
  },
  watch: {
      listFav(o, n) {
          console.log('fav', o, n);
          this.favoriteCount = n.length;
      }
  }
}
</script>

<style>
  .second-header {
    background-image: url('http://api.thumbr.it/whitenoise-600x370.png?background=eafffcff&noise=dbdbdb&density=25&opacity=20');
    padding-top: 15px;
    padding-bottom: 20px;
  }
  .logo-wrapper {
    text-align: left;
  }
  .sec-img{
    max-width: 75%;
    text-align: left;
    margin-left: 0px;
  }
  .popular-wrapper{
    background: url("../../assets/Heart.png");
    background-repeat: no-repeat;
    background-position: -1px 1px;
    background-size: contain;
    outline-style:none;
    cursor: pointer;
    color: #38c8b2 !important;
    width: 100%;
    height: 100%;
    display: inline-block;
  }
  .popular-wrapper.active {
    background: url("../../assets/Heart-filled.png");
    background-repeat: no-repeat;
    background-position: 0px 0px;
    background-size: contain;
    outline-style: none;
    width: 100%;
    cursor: pointer;
    color: #fff !important;
    display: inline-block;
    height: 100%;
  }
  .fav-counter{
    font-family: "Quicksand";
    font-size: 22px;
    display: inline-block;
    margin-top: 10px;
    margin-left: -5px;
    outline-style:none;

  }

</style>
