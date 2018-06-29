<template>
  <div class="serach-page">
    <second-header></second-header>
    <sub-header></sub-header>
    <filters></filters>
    <div class="search-page-wrapper">
      <names-list></names-list>
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
  methods: {
    onClickChild (value) {

    }
  },
  mounted () {

  },
  created: function() {
    window.document.title = "Search page"
  }
}
</script>

<style>
  .search-page-wrapper{
    min-height: 200px;
  }
</style>
