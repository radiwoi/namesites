<template>
  <div class="favorite-page">
    <second-header></second-header>
    <sub-header></sub-header>
    <div v-if="this.listFav.length > 0">
      <div class="fav-subheader">
        <div class="container">
          <div class="row">
            <div class="col-12 col-lg-4 email-send-wrapper">
              <span class="fav-label">Skicka listan med mina favoritnamn till:</span>
              <div class="input-group">
                <input type="email" class="form-control main-search-control" v-on:keyup.enter="sendEmail" v-model="userEmail" placeholder="Ex. namn@gmail.com">
                <span class="input-group-btn main-page-search">
                  <button class="btn btn-default fav-page-send-btn" @click="sendEmail" type="submit">
                    Skicka
                  </button>
                </span>
              </div>
              <div v-show="send_success" class="alert alert-success" role="alert">
                <button type="button" aria-label="Close" @click="send_success=false" class="close">×</button>
                E-post har skickats
              </div>
              <div v-show="send_error" class="alert alert-danger" role="alert">
                <button type="button" aria-label="Close" @click="send_error=false" class="close">×</button>
                Ogiltig mejladress
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
    <div v-else="this.listFav.length > 0" class="solo-capt">
      Det finns inga sparade favoriter.
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default{
  name: 'favorite-page',

  metaInfo: {
    title: 'Pojknamn.se - Mina favoriter',
     meta: [
      { name: 'description', content: 'Här listas de favoriter du sparat bland pojknamn och unisexnamn. Du har möjlighet att skicka listan via e-post till dig själv eller någon annan.' }
    ],
    link: [
      { rel: 'canonical', href: 'https://pojknamn.se/mina-favoriter' }
    ]

  },

  data(){
    return {
      userEmail: "",
      backend_url: "https://pojknamn.se/api/v1/",
      send_success: false,
      send_error: false,
//      backend_url: "http://names_project.devhost1.com/api/v1/"
    }
  },
  methods: {
    sendEmail() {
      let obj = this.searchObject;
      obj["ids"] = this.listFav;
      obj["user_email"] = this.userEmail;

      let valid = this.checkInput();
      if (!valid) {
        this.send_error = true;
        this.send_success = false;
        return false;
      }

      axios.post(this.backend_url + 'sendemail/', obj, {
        validateStatus: function (status) {
          return ([404, 500].indexOf(status) == -1);
        }
      })
        .then(r => {
          this.userEmail = '';
          this.send_success = true;
          this.send_error = false;
        })
        .catch(e => {
          this.send_error = true;
          this.send_success = false;
        })
    },
    checkInput() {
      let validRegEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      let validator = false;
      if (validRegEx.test(this.userEmail)) {
        validator = true;
      }
      return validator;
//      return true
    }

  },
  computed: {
    ...mapGetters({
      listFav: 'getListFav',
      searchObject: "getSearchObject"
    })
  }
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
.solo-capt {
    font-family: 'Quicksand-Bold';
    font-size: 17px;
    padding: 30px 0px;
}
.sub-fav-img {
  width: 90%;
  margin-top: 20px;
}
</style>
