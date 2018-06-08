<template>
  <div class="subheader">
    <div class="container">
      <div class="row">
        <div class="col col-lg-4 sub-menu">
          <router-link v-bind:to="'/search-page'">
            <span class="sub-menu-item active">Sokning</span>
          </router-link>
          <router-link v-bind:to="'/popular-page'">
            <span class="sub-menu-item">Populara namn</span>
          </router-link>
        </div>
        <div class="col-lg-2 offset-lg-6">
          <img class="img-fluid sub-img" src="../../assets/Logo-girl.png" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sub-header',
}
</script>

<style>
  .subheader{
    /*border-bottom: 1px solid #43c0ae;*/
    box-shadow: 0px 2px 5px #8edcd1;
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
    border-bottom: 2px solid #38c7b2;
  }
  .subheader{
    padding: 5px;
  }
  .sub-img{
    max-width: 90%;
  }
</style>
