<template>
  <div id="app">
    <!--<main-header></main-header>-->
    <router-view></router-view>
    <div class="common-footer footer">
      <span>© Flicknamn.se</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style>
@font-face {
  font-family: 'Quicksand';
  src: url('assets/fonts/Quicksand-Regular.ttf')
}

@font-face {
  font-family: 'Quicksand-Bold';
  src: url('assets/fonts/Quicksand-Bold.ttf')
}

body {
  background-image: url('assets/app.png')
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.common-footer {
  padding: 15px 10px 15px;
}
</style>
