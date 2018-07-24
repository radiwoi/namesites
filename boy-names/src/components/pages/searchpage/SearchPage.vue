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

  metaInfo: {
    title: 'Pojknamn.se - Sökresultat med pojknamn',
     meta: [
      { name: 'description', content: 'Sökresultat  på svenska pojknamn. Du har möjlighet att filtrera listan på namn, förekomst och snittålder. Hur många personer bär namnet och i vilka åldrar.' }
    ]
  },

  data () {
    return {

    }
  },
  methods: {
    onClickChild (value) {

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
