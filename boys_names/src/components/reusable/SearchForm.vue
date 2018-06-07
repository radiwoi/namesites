<template>
  <div class="search-form">

    <div class="input-group">
      <input type="text" class="form-control main-search-control" placeholder="Sok" v-model="searchObject.search_phrase">
      <span class="input-group-btn main-page-search">
      <router-link v-bind:to="{name: 'search-page'}">
        <button class="btn btn-default main-page-search-btn" @click="handleClick" type="submit">
            <i class="fa fa-search"></i>
        </button>
      </router-link>
    </span>
    </div>
    <small id="emailHelp" class="form-text text-muted under-search">
      Visa Namn Som
      <span class="search-criteria" @click="chooseCriteriaWindow">{{search_criteria.name}} <i class="fas fa-angle-down"></i>
        <div v-if="seen" class="criterias-list">
          <div v-for="criteria, index in criterias" @click="chooseCriteria(index)" v-if="!criteria.chosen">{{criteria.name}}</div>
        </div>
      </span>
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
        criterias: [
            {name: "innehar sokstrangen", action: "middle", chosen: false},
            {name: "borjar med sokstrangen ", action: "start", chosen: true},
            {name: "slutar med sokstrangen", action: "end", chosen: false},
        ],
        new_criterias: {
            start: {},
            middle: {},
            end: {}
        }
      }
    },
  methods: {
    search () {
        alert('G!!@');
    },
    chooseCriteriaWindow () {
        this.seen = !this.seen
    },
    chooseCriteria (index) {
      this.criterias.map(criteria => { return criteria.chosen = false });
      this.criterias[index]['chosen'] = true;
      this.$store.commit('changeCriteria', this.criterias[index]['action']);
      this.search_criteria = this.criterias[index];
    },
    handleClick () {
//      this.$store.commit('test', 'mooooooo')
    }
  },
  computed: {
      searchObject: {
          get() {
              return this.$store.state.searchObject
          },
//          set(value) {
//              this.$store.commit('test', value)
//          }
      }
  },
  created() {
    console.log(this.$store.state.searchObject.search_criteria);
    this.criterias.map(criteria => {
        if (criteria.action == this.$store.state.searchObject.search_criteria) {
            criteria.chosen = true;
            this.search_criteria = criteria
        } else {
            criteria.chosen = false
        }
    });
  }
}
</script>

<style>
  .search-form{
    padding-left: 20px;
    padding-right: 20px;
  }
  .input-group{

    border-color: #38c8b2;
  }
  .input-group{
    position: relative;
  }
  .main-page-search{
    position: absolute;
    right: 0;
    z-index: 4;
  }
  .main-page-search-btn{
    background: #38c8b2;
    color: #fff;
    height:52px;
    width: 53px;
    border: 2px solid #38c8b2;
  }
  .main-search-control{
    border: 2px solid #38c8b2;
    height: 52px;
  }
  .main-search-control:focus{
    background-color: #fff;
    border-color: #38c8b2;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(29, 255, 92, 0.25);
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
    border:1px solid #38c8b2;
    height: 70px;
    width: 210px;
    right:-15px;
    background: #ffffff;
    z-index: 5;
    line-height: 25px;
  }
</style>
