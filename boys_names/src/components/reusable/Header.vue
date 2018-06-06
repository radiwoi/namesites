<template>
  <div class="header">
    <div class="container">
      <div class="row">
        <div class="col col-lg-2">
          <img class="img-fluid" src="../../assets/Boy.png" alt="">
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

</style>
