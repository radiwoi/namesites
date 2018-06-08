<template>
  <div class="serach-page">
    <second-header></second-header>
    <sub-header></sub-header>
    <div class="filters">
      <div class="container">
        <table class="table filters-table">
          <tbody>
            <tr>
              <td class="fav" style="width: 118px;">
                <i style="visibility: hidden" class="fa fa-heart"></i>
              </td>
              <td style="width:297px;">
                Namn
              </td>
              <td style="width: 474px;">
                Forecomst
              </td>
              <td>
                Snittalder
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
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
  .filters {
    font-family: 'Quicksand-Bold';
    font-size: 18px;
  }
  .search-page-wrapper{
    min-height: 200px;
  }
  .filters-table{
    text-align: left;
  }
  .table td{
    padding: 0.65 rem;
  }

</style>
