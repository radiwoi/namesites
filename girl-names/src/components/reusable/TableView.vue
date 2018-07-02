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
            {{nameObj.average_age}} år <i class="fa fa-info-circle"></i>
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
  </div>
</template>

<script>
    export default {
        name: "table-view",
        props: ['namesList', 'currentPage', 'listFav'],
        methods: {
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
            style (width) {
              if(width == 100) {
                  return 70;
              } if(width == 0) {
                  return 5;
              } else {
                return width + 10
              }
            },
            checkIfFavorite(id){
              if(this.listFav.includes(id)){
                return true;
              }
            },
        }
    }
</script>

<style scoped>
  .tooltip-list {
    pointer-events: none;
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
    box-shadow: 0px 2px 15px #dc8796;
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
    box-shadow: 0px 2px 15px #dc8796;
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
    box-shadow: 0px 2px 15px #dc8796;
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
    background: #F88580;
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
    color: #F88580;
  }
  .fav{
    text-align: center;
    color: #F88580;

  }
  .fav i{
    cursor: pointer;
  }
  .make-fav{
    background: url("../../assets/Heart-red.png");
    background-repeat: no-repeat;
    background-position: 1px 2px;
    width: 25px;
    height: 25px;
    background-size: contain;
    margin: 0 auto;
    cursor: pointer;
  }
  .make-fav.active {
    background: url("../../assets/Heart-red-filled.png");
    background-repeat: no-repeat;
    background-position: 1px 2px;
    width: 25px;
    height: 25px;
    background-size: contain;
    margin: 0 auto;
    cursor: pointer;
  }
  .names-table {
    text-align: left;
    font-size: 15px;
    border-color: #fafafa;
  }
</style>
