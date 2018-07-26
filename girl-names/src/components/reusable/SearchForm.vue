<template>
  <div class="search-form">
    <div class="input-group">
      <a href="" class="alphabet" v-on:click="handleLetter()">Alla</a>
      <a href="" class="alphabet" v-for="letter in alphabet" v-on:click="handleLetter(letter)">{{letter}}</a>
    </div>
    <div class="input-group">
      <input type="text" class="form-control main-search-control" placeholder="Sök på namn, del av namn eller enstaka bokstäver" v-on:keyup.enter="handleEnter" v-model="localSearchPhrase">
      <span class="input-group-btn main-page-search">
        <span v-if="localSearchPhrase.length > 0" @click="resetFilters" class="reset-filters"></span>
        <router-link class="triggered" v-bind:to="{name: redirectTo}">
          <button class="btn btn-default main-page-search-btn" @click="handleClick" type="submit">
              <i class="fa fa-search"></i>
          </button>
        </router-link>
      </span>
    </div>
    <small id="emailHelp" class="form-text text-muted under-search">
      Visa namn som
      <span class="search-criteria" @click="chooseCriteriaWindow">{{search_criteria.name}} <i class="fas fa-angle-down"></i>
        <div v-if="seen" class="criterias-list">
          <div v-for="criteria, index in criterias" @click="chooseCriteria(index)" v-if="!criteria.chosen">{{criteria.name}}</div>
        </div>
      </span>
      <span class="error-msg" v-if="errorMsg.length > 0">{{errorMsg}}</span>
    </small>
  </div>
</template>


<script>
import {mapState, mapMutations} from 'vuex'
export default {
    name: 'search-form',
    data () {
      return {
        seen: false,
        search_criteria: {},
        localSearchPhrase: "",
        currentPage: "",
        redirectTo: "search-page",
        errorMsg: "",
        criterias: [
            {name: "börjar med sökfrasen", action: "start", chosen: true},
            {name: "innehåller sökfrasen", action: "middle", chosen: false},
            {name: "slutar med sökfrasen", action: "end", chosen: false},
        ],
        alphabet: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö']
      }
    },
  methods: {
    chooseCriteriaWindow () {
        this.seen = !this.seen
    },
    chooseCriteria (index) {
      this.criterias.map(criteria => { return criteria.chosen = false });
      this.criterias[index]['chosen'] = true;
      this.$store.commit('changeCriteria', this.criterias[index]['action']);
      this.search_criteria = this.criterias[index];
    },
    handleEnter () {
      document.getElementsByClassName('triggered')[0].click();
      this.handleClick();
    },
    handleLetter (letter){
      event.preventDefault();
      if (letter){
        this.localSearchPhrase = letter;
      } else {
        this.localSearchPhrase = "";
      }
      document.getElementsByClassName('triggered')[0].click();
      this.handleClick();
    },
    handleClick () {
      this.$emit("closeMobileSearch");
      this.errorMsg = "";
      let valid = this.checkInput();
      if (!valid) {
          this.errorMsg = 'incorrect value';
          return false;
      }
      this.$store.state.searchObject.frequency = ["Ovanligt", "Mindre vanligt", "Mycket vanligt", "Mycket ovanligt", "Ganska vanligt", "Vanligt"];
      this.$store.state.searchObject.age_distribution = [10,20,30,50,70,71];
      this.$store.commit('changeDoSearch', true);
      this.$store.commit('changeDoResetFilters', true);
      this.$store.commit('test', this.localSearchPhrase);
    },
    resetFilters() {
      this.chooseCriteria(0);
      this.localSearchPhrase = "";
      this.$store.commit('test', this.localSearchPhrase);
      this.$store.commit('changeDoSearch', true);
    },
    checkInput () {
      let validRegEx = /^[a-zA-Z() ÅÄÖ]*$/;
      let validator = false;
      if(validRegEx.test(this.localSearchPhrase)){
          validator = true;
      }
      return validator;
    }
  },
  computed: {
      searchObject: {
          get() {
              return this.$store.state.searchObject
          },
      }
  },
  created() {
    this.currentPage = this.$route.name;
    this.localSearchPhrase = this.$store.state.searchObject.search_phrase;
//    if (this.currentPage != "start-page") {
//        this.redirectTo = this.currentPage
//    }

    let self = this;

    window.addEventListener('click', function(e){
      if (!self.$el.contains(e.target)){
        self.seen = false
      }
    })

    this.criterias.map(criteria => {
        if (criteria.action == this.$store.state.searchObject.search_criteria) {
            criteria.chosen = true;
            this.search_criteria = criteria
        } else {
            criteria.chosen = false
        }
    });
  },
  watch: {
    currentPage: function (from, to) {
      // console.log(from);
      // console.log(to);
      if (from != 'search-page'){
        this.resetFilters();
      }
    }
  }
}
</script>

<style>
  .search-form {
    padding-left: 20px;
    padding-right: 20px;
  }
  .input-group {
    border-color: #F88580;
  }
  .input-group {
    position: relative;
  }
  .main-page-search {
    position: absolute;
    border-radius: 5px;
    right: 0;
    z-index: 4;
  }
  .main-page-search-btn, .main-page-search-btn:hover, .main-page-search-btn:active, .main-page-search-btn:focus {
    background: #F88580;
    color: #fff;
    height:52px;
    width: 53px;
    border: 2px solid #F88580;
    border-radius: 5px;
    box-shadow: none;
  }
  .main-search-control {
    border: 2px solid #F88580;
    height: 52px;
    box-shadow: 0px 2px 5px #dc8796;
    font-family: 'Quicksand';
    border-radius: 5px;
  }
  /*input::-webkit-input-placeholder {*/
    /*!*color: #d7d7d7;*!*/
    /*color: red;*/
  /*}*/
  input::-webkit-input-placeholder {
     color: #d7d7d7 !important;
  }

  input::-moz-placeholder {
     color: #d7d7d7 !important;
  }

  input:-ms-input-placeholder {
     color: #d7d7d7 !important;
  }
  .input-group>.custom-select:not(:last-child), .input-group>.form-control:not(:last-child){
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
  }
  .main-search-control:focus {
    background-color: #fff;
    border-color: #F88580;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(255, 111, 114, 0.25);
  }
  .under-search{
    color: #424242;
    font-family: 'Quicksand';
    font-size: 14px;
    text-align: left;

  }
  .search-criteria{
    font-family: 'Quicksand-Bold';
    cursor: pointer;
    position: relative;
  }
  .criterias-list{
    position: absolute;
    padding-left: 15px;
    padding-top: 10px;
    border:1px solid #F88580;
    height: 70px;
    width: 210px;
    right:-15px;
    background: #ffffff;
    z-index: 5;
    line-height: 25px;
  }
  .error-msg{
    color: #ff6f72;
  }
  .reset-filters{
    background: url("../../assets/Close.png");
    display: inline-block;
    width: 22px;
    height: 22px;
    top: 28%;
    left:-25px;
    z-index: 100;
    cursor: pointer;
    position: absolute;
  }
  a.alphabet {
    padding: 2px;
    color: #42b983;
  }
  @media (max-width: 1024px) {
    a.alphabet {
      padding: 1px;
    }
  }
  @media (max-width: 767px) {
    a.alphabet {
      padding: 8px;
    }
  }
</style>
