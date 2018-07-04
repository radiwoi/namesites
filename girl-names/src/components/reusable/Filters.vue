<template>
  <div class="filters">
    <div class="container">
      <table class="table filters-table">
        <tbody>
          <tr>
            <td class="fav" style="width: 10%">
              <i style="visibility: hidden" class="fa fa-heart"></i>
            </td>
            <td class="names-title-cell" style="width:35%">
              <div @click="freqTooltip = false, ageTooltip = false, namesTooltip = !namesTooltip, checkedNames.length == 6 ? checkedNames = [] : checkedNames=checkedNames" class="title-filter names-length-filter">
                Namn <span class="filter-sorting"></span>
              </div>
              <div v-if="namesTooltip" class="tooltip freq-filter-tooltip">
                <div v-for="nameItem in namesLength">
                  <div class="filter-item search-freq-item">
                    <label class="checkbox-container"> {{nameItem.name}}
                      <input type="checkbox" :value="nameItem.name" v-model="checkedNames">
                      <span class="checkmark"></span>
                    </label>
                  </div>
                </div>
                <div class="footer-filter">
                  <!--{{checkedFreqs}}-->
                  <button @click="namesLengthApply" class="btn btn-filter freq-btn">Ok</button>
                </div>
              </div>
              <small class="filter-choises">
                <!--<span v-if="checkedNames.length == 0">None</span>-->
                <span v-if="checkedNames.length == 6 || checkedNames.length == 0">Alla</span>
                <span v-if="checkedNames.length > 0 && checkedNames.length < 6 && !namesTooltip" class="item-check" v-for="(cName, ind) in checkedNames">
                  <i @click="removeElement(ind, 'checkedNames')" class="fa fa-times"></i> {{cName}}
                </span>
              </small>
            </td>

            <td class="freq-title-cell" style="width: 35%">
              <div @click="namesTooltip = false, ageTooltip = false, freqTooltip = !freqTooltip, checkedFreqs.length == 6 ? checkedFreqs = [] : checkedFreqs=checkedFreqs" class="title-filter freq-filter">
                Förekomst <span class="filter-sorting"></span>
              </div>
              <div v-if="freqTooltip" class="tooltip freq-filter-tooltip">
                <div v-for="freq in frequency">
                  <div class="filter-item search-freq-item">
                    <label class="checkbox-container"> {{freq.name}}
                      <input type="checkbox" :value="freq.name" v-model="checkedFreqs" checked="checked">
                      <span class="checkmark"></span>
                    </label>
                  </div>
                </div>
                <div class="footer-filter">
                  <!--&lt;!&ndash;{{checkedFreqs}}&ndash;&gt;{{z}}-->
                  <button @click="frequencyApply" class="btn btn-filter freq-btn">Ok</button>
                </div>
              </div>
              <small class="filter-choises">
                <!--<span v-if="checkedFreqs.length == 0">None</span>-->
                <span v-if="checkedFreqs.length == 6 || checkedFreqs.length == 0">Alla</span>
                <span v-if="checkedFreqs.length > 0 && checkedFreqs.length < 6 && !freqTooltip" class="item-check" v-for="(freqName, ind) in checkedFreqs">
                  <i @click="removeElement(ind, 'checkedFreqs')" class="fa fa-times"></i> {{freqName}}
                </span>
              </small>
            </td>

            <td class="distribution-title-cell d-none d-sm-table-cell" style="width: 20%">
              <div @click="namesTooltip = false, freqTooltip = false, ageTooltip = !ageTooltip, checkedAges.length == 6 ? checkedAges = [] : checkedAges=checkedAges" class="title-filter">
                Snittålder <span class="filter-sorting"></span>
              </div>
              <div v-if="ageTooltip" class="tooltip freq-filter-tooltip">
                <div v-for="age in ageDistribution">
                  <div class="filter-item search-freq-item">
                    <label class="checkbox-container"> {{age.name}}
                      <input type="checkbox" :value="age.name" v-model="checkedAges">
                      <span class="checkmark"></span>
                    </label>
                  </div>
                </div>
                <div class="footer-filter">
                  <!--{{checkedFreqs}}-->
                  <button @click="ageDistributionApply" class="btn btn-filter freq-btn">Ok</button>
                </div>
              </div>
              <small class="filter-choises">
                <!--<span v-if="checkedAges.length == 0">None</span>-->
                <span v-if="checkedAges.length == 6 || checkedAges.length == 0">Alla</span>
                <span v-if="checkedAges.length > 0 && checkedAges.length < 6 && !ageTooltip" class="item-check" v-for="(checkedAge, ind) in checkedAges">
                  <i @click="removeElement(ind, 'checkedAges')" class="fa fa-times"></i> {{checkedAge}}
                </span>
              </small>
            </td>

          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import {mapState, mapMutations} from 'vuex'
export default {
  name: 'filters',
  data () {
    return {
//      z: 1,
      showNameFilters: true,
      showFreqFilters: true,
      showAgeFilters: true,
      namesLength: [
        {"name": "Dubbelnamn", "value": true},
        {"name": "1-3 bokstaver", "value": "1 - 3"},
        {"name": "4-5 bokstaver", "value": "4 - 5"},
        {"name": "6-7 bokstaver", "value": "6 - 7"},
        {"name": "8-9 bokstaver", "value": "8 - 9"},
        {"name": "9 > bokstäver", "value": "9 >"},
      ],
      frequency: [
        {"name": "Mycket vanligt", "value": ""},
        {"name": "Vanligt", "value": ""},
        {"name": "Ganska vanligt", "value": ""},
        {"name": "Mindre vanligt", "value": ""},
        {"name": "Ovanligt", "value": ""},
        {"name": "Mycket ovanligt", "value": ""},
      ],
      ageDistribution: [
        {"name": "0 - 10 år", "value": 10},
        {"name": "11 - 20 år", "value": 20},
        {"name": "21 - 30 år", "value": 30},
        {"name": "31 - 50 år", "value": 50},
        {"name": "51 - 70 år", "value": 70},
        {"name": "71 > år", "value": 71},
      ],
      checkedFreqs: [],
      checkedNames: [],
      checkedAges: [],
      freqTooltip: false,
      namesTooltip: false,
      ageTooltip: false,
    }
  },
  methods: {
    frequencyApply() {
//      this.z=0;
      this.$store.commit('changeFrequency', this.checkedFreqs);
      this.freqTooltip = false;
      this.showFreqFilters = true;
      this.$store.commit('changeDoSearch', true);
    },
    namesLengthApply() {
      let tmp = [];
      this.namesLength.map(n => {
        if(this.checkedNames.includes(n.name)) {
            tmp.push(n.value)
        }
      });
      this.$store.commit('changeLettersRange', tmp);
      this.namesTooltip = false;
      this.showNameFilters = true;
      this.$store.commit('changeDoSearch', true);
    },
    ageDistributionApply() {
      let tmp = [];
      this.ageDistribution.map(n => {
        if(this.checkedAges.includes(n.name)) {
            tmp.push(n.value)
        }
      });
      this.$store.commit('changeAgeDistribution', tmp);
      this.ageTooltip = false;
      this.showAgeFilters = true;
      this.$store.commit('changeDoSearch', true);
    },
    removeElement: function (index, what) {
      this[what].splice(index, 1);
      this.ageDistributionApply();
      this.namesLengthApply();
      this.frequencyApply();
    }
  },
  created() {
    this.$store.state.searchObject.frequency.map(f => {
        this.checkedFreqs.push(f)
    });
    this.ageDistribution.map(a => {
      if(this.$store.state.searchObject.age_distribution.includes(a.value)) {
          this.checkedAges.push(a.name)
      }
    });
    this.namesLength.map(n => {
      if(this.$store.state.searchObject.letters_range.includes(n.value)) {
          this.checkedNames.push(n.name)
      }
    });

    let self = this;

    window.addEventListener('click', function(e){
      if (!self.$el.contains(e.target)){
        self.freqTooltip = false
        self.namesTooltip = false
        self.ageTooltip = false
      }
    })
  }
}
</script>

<style>
  .filters {
    font-family: 'Quicksand-Bold';
    font-size: 17px;
  }

  .filters-table{
    text-align: left;
    margin-top: 10px;
    margin-bottom: 0rem;
  }
  .table td{
    padding: 0.65 rem;
    border: none;
  }
  .filter-choises{
    font-family: 'Quicksand';
    font-size: 13px;
  }

  .filter-choises {
    height: 40px;
    display: inline-block;
  }
  .item-check:first-of-type {
    margin-left: 0px;
  }
  .item-check {
    display: inline-block;
    margin-left: 1px;
    /*width: 100px;*/
  }

  .item-check .fa {
    color: #F88580;
    cursor: pointer;
  }
  .title-filter{
    position: relative;
    cursor: pointer;
  }
  .filter-sorting{
    background-image: url("../../assets/Sorting.png");
    position: absolute;
    width: 18px;
    height: 17px;
    top: 6px;
    /*right:1px;*/
  }
  .freq-filter-tooltip {
    font-family: 'Quicksand';
    display: block;
    top: 40%;
    opacity: 1;
    background: #fff;
    padding-top: 3px;
    padding-bottom: 10px;
    padding-left: 13px;
    padding-right: 15px;
    box-shadow: 0px 2px 15px #dc8796;
  }
  .filter-item{
    margin-top: 7px;
    font-size: 17px;
  }
  .checkbox-container {
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
  .checkbox-container input {
      position: absolute;
      opacity: 0;
      cursor: pointer;
  }

  /* Create a custom checkbox */
  .checkmark {
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
  .checkbox-container:hover input ~ .checkmark {
      background-color: #fff;
  }

  /* When the checkbox is checked, add a blue background */
  .checkbox-container input:checked ~ .checkmark {
      background-color: #F88580;
      border-color: #F88580;
  }

  /* Create the checkmark/indicator (hidden when not checked) */
  .checkmark:after {
      content: "";
      position: absolute;
      display: none;
  }

  /* Show the checkmark when checked */
  .checkbox-container input:checked ~ .checkmark:after {
      display: block;
  }

  /* Style the checkmark/indicator */
  .checkbox-container .checkmark:after {
      left: 6px;
      top: 2px;
      width: 5px;
      height: 10px;
      border: solid white;
      border-width: 0 3px 3px 0;
      -webkit-transform: rotate(45deg);
      -ms-transform: rotate(45deg);
      transform: rotate(45deg);
  }
  .footer-filter{
    text-align: center;
    margin-top: 15px;
    margin-bottom: 8px;
  }
  .btn-filter{
    font-family: 'Quicksand-Bold';
    padding: .215rem 1.9rem;
    background: #fde6e4;
    border: 2px solid #F88580;
    color: #F88580;
  }
  .btn-filter:focus {
    box-shadow: none;
  }
  .freq-title-cell, .names-title-cell, .distribution-title-cell {
    position: relative;
  }
  @media (max-width: 1200px) {}

  @media (max-width: 992px) {}

  @media (max-width: 768px) {}

  @media (max-width: 576px) {
    .freq-filter-tooltip{
      left: -30px;
    }
     .freq-title-cell {
      width: 35%;
      opacity: 1;
      display: table-cell;
      transition: 1s;
    }
    .freq-title-cell.fade {
      width: 35%;
      opacity: 0;
      display: none;
      /*transition: 1s;*/
    }
    .distribution-title-cell {
      width: 35%!important;
      opacity: 1;
      display: table-cell;
      transition: 1s;
    }
    .distribution-title-cell.fade {
      width: 35%!important;
      opacity: 0;
      display: none;
      /*transition: 1s;*/
    }
    .filters > .container{
      padding: 0;
    }
  }
</style>
