<template>
  <div class="popular">
    <second-header></second-header>
    <sub-header></sub-header>
    <div class="popular-name-wrapper">
      <div class="container popular-container">
        <div class="year-filter">
          Populara namn ar <span class="filter-year-bold">2016 <i class="fa fa-angle-down"></i></span>
        </div>
      </div>
      <filters></filters>
      <names-list></names-list>
    </div>
  </div>
</template>

<script>

</script>

<style>
  .popular{
    font-family: 'Quicksand';
  }
  .popular-name-wrapper {
    min-height: 320px;
  }
  .year-filter{
    padding-top: 15px;
    padding-bottom: 15px;
    text-align: left;
    font-size: 18px;
    border-bottom: 1px solid rgba(239, 239, 240, 1);
    margin-bottom: 10px;
  }
  .filter-year-bold{
    font-family: 'Quicksand-Bold';
  }
</style>
