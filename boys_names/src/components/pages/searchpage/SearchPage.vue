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
                <div class="title-filter">
                  Namn <span class="filter-sorting"></span>
                </div>
                <small class="filter-choises">All</small>
              </td>
              <td style="width: 474px;">
                <div class="title-filter">
                  Forecomst <span class="filter-sorting"></span>
                </div>
                <small class="filter-choises">All</small>
              </td>
              <td>
                <div class="title-filter">
                  Snittalder <span class="filter-sorting"></span>
                </div>
                <small class="filter-choises">All</small>
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
    font-size: 17px;
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
  .filter-choises{
    font-family: 'Quicksand';
    font-size: 13px;
  }
  .title-filter{
    position: relative;
  }
  .filter-sorting{
    background-image: url("../../../assets/Sorting.png");
    position: absolute;
    width: 18px;
    height: 17px;
    top: 6px;
    /*right:;*/
  }
</style>
