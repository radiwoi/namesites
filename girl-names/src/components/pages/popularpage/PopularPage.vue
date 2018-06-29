<template>
  <div class="popular">
    <second-header></second-header>
    <sub-header></sub-header>
    <div class="popular-name-wrapper">
      <years-filter></years-filter>
      <filters></filters>
      <names-list></names-list>
    </div>
  </div>
</template>

<script>
export default {
  name: 'popular-page',
  created: function() {
    window.document.title = "Popular page"
  }
}
</script>

<style>
  .popular{
    font-family: 'Quicksand';
  }
  .popular-name-wrapper {
    min-height: 320px;
  }

  /* Hide the browser's default checkbox */
  .checkbox-container-radio input {
      position: absolute;
      opacity: 0;
      cursor: pointer;
  }

  /* On mouse-over, add a grey background color */
  .checkbox-container-radio:hover input ~ .checkmark-radio {
      background-color: #fff;
  }

  /* When the checkbox is checked, add a blue background */
  .checkbox-container-radio input:checked ~ .checkmark-radio {
      background-color: #F88580;
      border-color: #F88580;
  }

  /* Show the checkmark when checked */
  .checkbox-container-radio input:checked ~ .checkmark-radio:after {
      display: block;
  }
  .checkbox-container-radio input:checked ~ .checkmark-radio:after {
    display: block;
    top: 3px;
    left: 4px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: white;
  }
</style>
