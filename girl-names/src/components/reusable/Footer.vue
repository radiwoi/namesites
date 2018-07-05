<template>
  <div class="footer">
    <div class="container">
      <div class="row">
        <div v-for="text in footerTexts" class="footer-text-col col-12 col-lg-4">
          <div class="footer-title">
            {{text.girl_title}}
          </div>
          <div class="col-text-wrapper">
            {{text.girl_names}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default{
  name: 'main-footer',
  data() {
      return {
        backend_url: "",
        footerTexts: []
      }
  },
  methods: {

  },
//  .get("http://names_project.devhost1.com/api/v1/footer-texts/")
  mounted() {
    axios
      .get("https://flicknamn.se/api/v1/footer-texts/")
      .then(response => (this.footerTexts = response.data));
  }
}
</script>

<style>
  .footer {
    background-image: url('../../assets/footer.png');
    padding: 15px 10px 40px 10px;
    font-family: 'Quicksand';
  }
  .footer-text-col{
    font-size: 12px;
    text-align: left;
  }
  .footer-title{
    font-family: 'Quicksand-Bold';
    margin-bottom: 15px;
    margin-top: 15px;
    font-size: 15px;
  }
</style>
