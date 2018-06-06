<template>
  <div id="app">
    <main-header></main-header>
    <start-page></start-page>
    <main-footer></main-footer>
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
  background-image: url('http://api.thumbr.it/whitenoise-600x370.png?background=ffffffff&noise=dbdbdb&density=25&opacity=20')
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
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
</style>
