<template>
  <div class="serach-page">
    <second-header></second-header>
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
        console.log(value)
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
