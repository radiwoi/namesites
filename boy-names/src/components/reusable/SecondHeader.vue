<template>
  <div class="second-header">
    <div class="container">
      <div style="position:relative" class="row">
        <div class="col-6 col-lg-3 col-md-3 logo-wrapper">
          <router-link v-bind:to="'/'">
            <img class="sec-img img-fluid" src="../../assets/Boy.png" alt="Pojknamn / Killnamn" title="Pojknamn.se Logo">
          </router-link>
        </div>
        <div v-if="!mobileDevice" class="col-lg-6 col-md-8 offset-lg-2 d-none d-sm-block">
          <search-form></search-form>
        </div>
        <div v-if="mobileDevice && mobileFormActive" class="search-header-wrapper">
          <search-form v-on:closeMobileSearch="closeMobileSearch"></search-form>
        </div>
        <div @click="mobileSearchFormActions()" class="col-3 d-block d-xs-block d-sm-block d-md-none search-mobile">
          <img v-if="mobileDevice && !mobileFormActive" class="img-fluid" src="../../assets/Search-mobile.png" alt="">
          <img v-if="mobileDevice && mobileFormActive" class="img-fluid" src="../../assets/green-cross.png" alt="">
        </div>
        <div class="col-3 col-md-1 col-lg-1 right-heart-wrapper">
          <!--<img src="" alt="">-->
          <router-link  v-bind:class="{'active':favoriteCount > 0}" class="popular-wrapper" to="/mina-favoriter">
            <span class="fav-counter">{{favoriteCount}}</span>
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="mobileDevice && mobileFormActive" class="overlay"></div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'second-header',
  data () {
    return {
      favoriteCount: 0,
      mobileFormActive: false,
      mobileDevice: false,
      currentPage: "",
    }
  },
  methods: {
    mobileSearchFormActions: function() {
    this.mobileFormActive = !this.mobileFormActive;

      const el = document.body;

      if (this.mobileFormActive) {
        el.classList.add('overflow');
      } else {
        el.classList.remove('overflow');
      }
    },
    closeMobileSearch: function(){
      this.mobileFormActive = !this.mobileFormActive;
    },
    checkMobileDevice: function() {
      let check = false;
      (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
      return check;
    }
  },
  computed: {
    ...mapGetters({
      listFav: 'getListFav'
    })
  },
  created(){
        this.currentPage = this.$route.name;
  },
  beforeMount() {
    this.mobileDevice = this.checkMobileDevice();
  },
  mounted() {
    this.favoriteCount = this.listFav.length;
  },
  watch: {
    listFav(o, n) {
      this.favoriteCount = n.length;
    },
    currentPage: function (o, n) {
      if (o != 'search-page' && this.checkMobileDevice()) {
        this.$store.commit('test', '');
        this.$store.commit('changeDoSearch', true);
      }
    }
  }
}
</script>

<style>
  .second-header {
    background-image: url('../../assets/second-header.png');
    padding-top: 15px;
    padding-bottom: 20px;
  }
  .logo-wrapper {
    text-align: left;
  }
  .sec-img{
    max-width: 75%;
    text-align: left;
    margin-left: 0px;
  }
  .popular-wrapper{
    background: url("../../assets/Heart.png");
    background-repeat: no-repeat;
    background-position: -1px 1px;
    background-size: contain;
    outline-style:none;
    cursor: pointer;
    color: #38c8b2 !important;
    width: 100%;
    height: 100%;
    display: inline-block;
  }
  .popular-wrapper.active {
    background: url("../../assets/Heart-filled.png");
    background-repeat: no-repeat;
    background-position: 0px 0px;
    background-size: contain;
    outline-style: none;
    width: 100%;
    cursor: pointer;
    color: #fff !important;
    display: inline-block;
    height: 100%;
  }
  .fav-counter{
    font-family: "Quicksand";
    font-size: 22px;
    display: inline-block;
    margin-top: 10px;
    margin-left: -5px;
    outline-style:none;
  }
  .right-heart-wrapper{
     text-align: center;
     position: relative;
  }

  @media (min-width: 768px) {
    .sec-img {
      max-width: 100%;
    }
    .right-heart-wrapper {
      padding: 0;
    }
  }

  @media (min-width: 992px) {
    .right-heart-wrapper {
      padding-right: 15px;
      padding-left: 15px;
    }
  }

  @media (max-width: 1200px) {}

  @media (max-width: 992px) {}

  @media (max-width: 768px) {}

  @media (max-width: 576px) {
    .sec-img{
      max-width: 100%;
    }
    .popular-wrapper, .popular-wrapper.active{
      /*width: 50%;*/
    }
    /*.search-mobile:hover + .search-header-wrapper,*/
    /*.search-mobile:active + .search-header-wrapper,*/
    /*.search-mobile:focus + .search-header-wrapper {*/
      /*display: block !important;*/
    /*}*/
    .search-header-wrapper{
      position: absolute;
      top:65px;
      background: #fff;
      width: 100%;
      z-index: 100;
      padding-top: 20px;
      padding-bottom: 40px;
    }
    .second-header{
      /*margin-bottom: 10px;*/
    }
    .overlay {
      position: fixed;
      width: 100%;
      height: 100%;
      z-index: 99;
      top: 80px;
      background: rgba(0,0,0,0.3);
      overflow: hidden;
    }
  }

</style>
