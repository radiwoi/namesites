<template>
  <div class="container popular-container">
    <div class="row">
      <div class="col col-lg-3 year-filter">
        Populäraste namnen bland nyfödda år <span @click="chooseYearDropbox" class="filter-year-bold">{{selectedYear}} <i class="fa fa-angle-down"></i></span>
        <div v-if="yearTooltip" class="tooltip year-tooltip">
        <div v-for="y in yearsRange">
          <label class="checkbox-container-radio"> {{y}}
            <input v-on:change="changeYear(y)" type="radio" :value="y" v-model="selectedYear">
            <span class="checkmark-radio"></span>
          </label>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'years-filter',
  data () {
    return {
      yearTooltip: false,
      years: [1999, 2017],
      yearsRange: [],
      selectedYear: 2017,
    }
  },
  methods: {
      chooseYearDropbox () {
          this.yearTooltip = !this.yearTooltip
      },

      changeYear(year){
          this.yearTooltip = false;
          this.$store.commit("changePopularYear", year);
          this.$store.commit("changeDoSearch", true);
      }
  },
  mounted(){
      for(let i=this.years[1]; i > this.years[0]; i--){
          this.yearsRange.push(i);
      }
      this.selectedYear = this.searchObject.popular_year
  },
  created() {
    let self = this;

    window.addEventListener('click', function(e){
      if (!self.$el.contains(e.target)){
        self.yearTooltip = false
      }
    })
  },
  computed: {
  ...mapGetters({
      doSearch: 'getDoSearch',
      searchObject: "getSearchObject"
    })
  }
}
</script>

<style>
  .year-filter{
    padding-top: 15px;
    padding-bottom: 15px;
    text-align: left;
    font-size: 18px;
    border-bottom: 1px solid rgba(239, 239, 240, 1);
    margin-bottom: 10px;
  }
  .filter-year-bold{
    font-family: 'Quicksand-Bold';
    cursor: pointer;
  }
  .year-filter{
    position: relative;
  }
  .year-tooltip {
    font-family: 'Quicksand';
    display: block;
    /*top: 70%;*/
    /*right:40px;*/
    opacity: 1;
    background: #fff;
    padding-top: 3px;
    padding-bottom: 10px;
    padding-left: 13px;
    padding-right: 15px;
    box-shadow: 0px 2px 15px #8edcd1;
    width: 150px;
    height: 288px;
    overflow: auto;
    text-align: left;
    font-size: 16px;
  }
    .checkbox-container-radio {
    display: block;
    position: relative;
    padding-left: 25px;
    margin-bottom: 12px;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  /* Hide the browser's default checkbox */
  .checkbox-container-radio input {
      position: absolute;
      opacity: 0;
      cursor: pointer;
  }

  /* Create a custom checkbox */
  .checkmark-radio {
      position: absolute;
      top: 6px;
      left: 1px;
      height: 17px;
      width: 17px;
      background-color: #fff;
      border:1px solid #ccc;
      border-radius: 2px;
  }

  /* On mouse-over, add a grey background color */
  .checkbox-container-radio:hover input ~ .checkmark-radio {
      background-color: #fff;
  }

  /* When the checkbox is checked, add a blue background */
  .checkbox-container-radio input:checked ~ .checkmark-radio {
      background-color: #39c8b2;
      border-color: #39c8b2;
  }

  /* Create the checkmark/indicator (hidden when not checked) */
  .checkmark-radio:after {
      content: "";
      position: absolute;
      display: none;
  }

  /* Show the checkmark when checked */
  .checkbox-container-radio input:checked ~ .checkmark-radio:after {
      display: block;
  }
  .checkbox-container-radio input:checked ~ .checkmark-radio:after {
    display: block;
    top: 3px;
    left: 4px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: white;
  }
  .checkmark-radio {
    position: absolute;
    top: 6px;
    left: 1px;
    height: 17px;
    width: 17px;
    border: 1px solid #ccc;
    border-radius: 50%;
  }
</style>
