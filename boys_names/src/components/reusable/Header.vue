<template>
  <div class="header">
    <div class="container">
      <div class="row">
        <div class="col col-lg-2">
          <router-link v-bind:to="'/'">
            <img class="img-fluid" src="../../assets/Boy.png" alt="">
          </router-link>
        </div>
      </div>
      <!--{{msg}}-->
      <!--<div class="subheader" @click="test">subheader</div>-->
      <!--<button>button</button>-->
    </div>
  </div>
</template>

<script>
export default {
  name: 'main-header',
  data () {
    return {
      msg: 'header hgavdjhadvjadvjlavd'
    }
  },
  methods: {
      test () {
          alert('G!!@')
      }
  }
}
</script>

<style>
  .header {
    margin-bottom: 40px;
  }
</style>
