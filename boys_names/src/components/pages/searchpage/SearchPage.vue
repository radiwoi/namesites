<template>
  <div class="serach-page">
    <second-header></second-header>
    <div class="search-page-wrapper">
      {{searchInput}}
    </div>
  </div>
</template>

<script>

export default {
  props: ['searchInput'],
  data () {
    return {

    }
  },
  mounted () {

  }
}
</script>

<style>
  .search-page-wrapper{
    min-height: 200px;
  }
</style>
