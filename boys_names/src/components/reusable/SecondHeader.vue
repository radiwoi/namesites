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
        <div class="col-lg-1 popular-wrapper" @click="">
          <!--<img src="" alt="">-->
          <span class="fav-counter">0</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'second-header',
}
</script>

<style>
  .second-header{
    background-image: url('http://api.thumbr.it/whitenoise-600x370.png?background=eafffcff&noise=dbdbdb&density=25&opacity=20');
    padding-top: 15px;
    padding-bottom: 20px;
  }
  .logo-wrapper{
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
    background-position: 10px 0px;
    outline-style:none;
    cursor: pointer;
  }
  .fav-counter{
    font-family: "Quicksand";
    font-size: 22px;
    display: inline-block;
    margin-top: 10px;
    margin-left: -5px;
    outline-style:none;
    color: #38c8b2;
  }
</style>
