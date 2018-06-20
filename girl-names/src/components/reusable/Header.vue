<template>
  <div class="header">
    <div class="container">
      <div class="row">
        <div class="col col-lg-3 logo-wrapper">
          <router-link v-bind:to="'/'">
            <img class="img-fluid" src="../../assets/Girl.png" alt="">
          </router-link>
        </div>
      </div>
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
    padding-top: 15px;
  }
  .header .img-fluid{
    width: 75%;
  }
</style>
