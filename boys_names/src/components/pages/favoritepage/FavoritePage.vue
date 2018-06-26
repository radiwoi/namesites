<template>
  <div class="favorite-page">
    <second-header></second-header>
    <sub-header></sub-header>
    <div class="fav-subheader">
      <div class="container">
        <div class="row">
          <div class="col-12 col-lg-4 email-send-wrapper">
            <span class="fav-label">Send this favorite list to</span>
            <div class="input-group">
              <input type="email" class="form-control main-search-control" v-model="userEmail" placeholder="Ex. namn@gmail.com">
              <span class="input-group-btn main-page-search">
                <button class="btn btn-default fav-page-send-btn" @click="sendEmail" type="submit">
                  Send
                </button>
              </span>
            </div>
          </div>
          <div class="col col-lg-2 offset-lg-6 girl-logo-wrapper">
            <!--<img class="img-fluid sub-fav-img" src="../../../assets/Logo-girl.png" alt="">-->
          </div>
        </div>
      </div>
    </div>
    <filters></filters>
    <names-list></names-list>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default{
  name: 'favorite-page',
  data(){
    return {
      userEmail: "",
      backend_url: "http://34.254.119.140/api/v1/",
//      backend_url: "http://names_project.devhost1.com/api/v1/"
    }
  },
  methods: {
    sendEmail(){
      console.log(this.searchObject);
      console.log(this.listFav);
      console.log(this.userEmail);

      let obj = this.searchObject;
      obj["ids"] = this.listFav;
      obj["user_email"] = this.userEmail;

      axios.post(this.backend_url + 'send/email/', obj)
        .then(r => {})
        .catch(e => {})
//      alert('not implemented yet');
//      send/email/
    }
  },
  computed: {
    ...mapGetters({
      listFav: 'getListFav',
      searchObject: "getSearchObject"
    })
  },
}
</script>

<style>
.fav-subheader {
  font-family: 'Quicksand';
  /*box-shadow: 0px 2px 5px rgba(142, 220, 206, .55);*/
  padding-top: 15px;
  /*padding-bottom: 5px;*/
  padding-bottom: 20px;
}
.email-send-wrapper{
  text-align: left;
}
.fav-label{
  margin-bottom: 5px;
  display: inline-block;
}
.fav-page-send-btn, .fav-page-send-btn:hover, .fav-page-send-btn:active, .fav-page-send-btn:focus {
  font-family: 'Quicksand-Bold';
  font-size: 18px;
  background: #38c8b2;
  color: #fff;
  height:52px;
  min-width: 95px;
  border: 2px solid #38c8b2;
  border-radius: 5px;
  box-shadow: none;
}
.sub-fav-img {
  width: 90%;
  margin-top: 20px;
}
</style>
