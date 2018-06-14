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
              <div @click="namesTooltip = !namesTooltip" class="title-filter names-length-filter">
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
                  <button @click="namesLengthApply" class="btn btn-filter freq-btn">Accept</button>
                </div>
              </div>
              <small class="filter-choises">
                <span v-if="checkedNames.length == 0">All</span>
                <span class="item-check" v-for="(cName, ind) in checkedNames">
                  <i @click="removeElement(ind, 'checkedNames')" class="fa fa-times"></i> {{cName}}
                </span>
              </small>
            </td>

            <td class="freq-title-cell" style="width: 35%">
              <div @click="freqTooltip = !freqTooltip" class="title-filter freq-filter">
                Förecomst <span class="filter-sorting"></span>
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
                  <!--{{checkedFreqs}}-->
                  <button @click="frequencyApply" class="btn btn-filter freq-btn">Accept</button>
                </div>
              </div>
              <small class="filter-choises">
                <span v-if="checkedFreqs.length == 0">All</span>
                <span class="item-check" v-for="(freqName, ind) in checkedFreqs">
                  <i @click="removeElement(ind, 'checkedFreqs')" class="fa fa-times"></i> {{freqName}}
                </span>
              </small>
            </td>

            <td class="distribution-title-cell" style="width: 20%">
              <div @click="ageTooltip = !ageTooltip" class="title-filter">
                Snittalder <span class="filter-sorting"></span>
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
                  <button @click="ageDistributionApply" class="btn btn-filter freq-btn">Accept</button>
                </div>
              </div>
              <small class="filter-choises">
                <span v-if="checkedAges.length == 0">All</span>
                <span class="item-check" v-for="(checkedAge, ind) in checkedAges">
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
      namesLength: [
        {"name": "Dubbelnamn", "value": true},
        {"name": "1-3 bokstaver", "value": "1 - 3"},
        {"name": "4-5 bokstaver", "value": "4 - 5"},
        {"name": "6-7 bokstaver", "value": "6 - 7"},
        {"name": "8-9 bokstaver", "value": "8 - 9"},
        {"name": "10 > bokstaver", "value": "9 >"},
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
        {"name": "0 - 10 ar", "value": 10},
        {"name": "11 - 20 ar", "value": 20},
        {"name": "21 - 30 ar", "value": 30},
        {"name": "31 - 50 ar", "value": 50},
        {"name": "51 - 70 ar", "value": 70},
        {"name": "71 > ar", "value": 71},
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
      this.$store.commit('changeFrequency', this.checkedFreqs);
      this.freqTooltip = false;
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
    },
    removeElement: function (index, what) {
      this[what].splice(index, 1);
      this.ageDistributionApply();
      this.namesLengthApply();
      this.frequencyApply();
    }
  },
  created() {
//    console.log('qq',this.$store.state.searchObject.frequency);
//    console.log('qq',this.$store.state.searchObject.age_distribution);
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
    color: #39c8b2;
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
    box-shadow: 0px 2px 15px #8edcd1;
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
      background-color: #39c8b2;
      border-color: #39c8b2;
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
    background: #eafefc;
    border: 2px solid #39c8b4;
    color: #39c8b2;
  }
  .btn-filter:focus {
    box-shadow: none;
  }
  .freq-title-cell, .names-title-cell, .distribution-title-cell {
    position: relative;
  }
</style>
