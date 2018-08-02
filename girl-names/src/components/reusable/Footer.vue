<template>
  <div class="footer">
    <div class="container">
      <div class="row">
        <div v-for="text in footerTexts" class="footer-text-col col-12 col-lg-4">
          <!--<div class="footer-title">-->
            <!--{{text.title}}-->
          <!--</div>-->
          <div class="col-text-wrapper" v-html="text.names">
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
        footerTexts: [{"id":16,"title":"column 1","position":"1","names":'<div class=\"footer-title\">Flicknamn / Tjejnamn</div>\r\nVi har samlat folkbokförda svenska namn och varianter av dessa som traditionellt sorteras in under flicknamn och unisexnamn. Vi vill hjälpa föräldrar eller blivande föräldrar som är i processen att hitta ett namn till sitt barn. \r\n\r\nNamnet blir en av de första sakerna andra kommer att lära sig om ditt barn. Men även om det kan kännas överväldigande så brukar det också vara en rolig process. Är namnet enkelt att stava och uttala? Vad är dess smeknamn? Hur låter det med ditt efternamn? Vilka namntrender är heta i år? \r\n\r\nVissa diskuterar och argumenterar under en lång tid innan de bestämmer sig för ett namn. Andra bestämmer sig fort eller kanske alltid har vetat vad deras barn ska få för ett namn. Det finns ungefär lika många sätt att välja namn på som det finns olika namn. Ett tips är att hålla de olika namnförslagen hemliga, eller bara berätta för de närmaste tills det är bestämt. Inget namn kommer att glädja alla och andras åsikter bör inte vara en del av processen för något så personligt.\r\n\r\n<div class=\"footer-title\">Svenska flicknamn / Svenska tjejnamn</div>\r\nAssociationerna som görs till namn är väldigt bundna till tid och kultur. Följande tio kriterier är vanligt att ha i åtanke när man väljer namn. 1. Estetiskt tilltalande 2. Lagom vanligt 3. Lätt att stava 4. Lätt att uttala 5. Passar med efternamnet 6. Passar med syskonens namn 7. Passar barnets personlighet 8. Internationellt gångbart 9. Inte betyda något konstigt 10. Inte gå att komma på öknamn på.\r\n<div class=\"footer-title\">Ovanliga flicknamn / Ovanliga tjejnamn</div>\r\n\r\nAtt ge din dotter ett unikt namn eller udda flicknamn kan vara lite av en utmaning. Vanligt är att vilja ha ett namn som sticker ut men som du inte riskerar att ogilla efter ett par år. Vi har gjort det enkelt att söka på ovanliga namn. I filter funktionen kan du ställa in att du endast vill se namn som är mindre vanliga. Ett tips är att göra detta och sedan söka på en bokstav i taget och gå igenom samtliga namn på varje bokstav. Det är tidskrävande men ger dig en lång lista med namnförslag.\r\n<div class=\"footer-title\">Amerikanska flicknamn</div>\r\nMånga populära amerikanska namn har rötter i andra länder. Många från England tack vare det gemensamma språket, men också franska, spanska, hebreiska, latinska, grekiska och tyska. Flicknamn som ursprungligen är amerikanska är oftast nyare namn som inte används i konservativa England. Indianska namn och även namn för platser som exempelvis Alaska och Alabama är typiskt amerikanska.',"read_more_words":120},
          {"id":17,"title":"column 2","position":"2","names":'<div class=\"footer-title\">Tjejnamn på A </div>\r\nSöker du flicknamn på m, flicknamn på e, flicknamn på l, flicknamn på s, tjejnamn på e, flicknamn på o, flicknamn på b, flicknamn på j, flicknamn på c, flicknamn på t, flicknamn på n flicknamn på v, tjejnamn på d, tjejnamn på r eller på annan bokstav? I vår sökfunktion är det möjligt att söka på endast en bokstav för att lista alla namnen som börjar på den bokstaven.\r\n\r\n<div class=\"footer-title\">Nordiska flicknamn</div>\r\nPopulära flicknamn bland de nordiska länderna brukar skilja sig åt. Men Emma återkommer i alla de nordiska länderna. Gemensamt för nordiska flicknamn är också att de är enkla och korta och ofta slutar på -a. Namn från nordisk mytologi och med fornnordiskt ursprung har blivit mer trendiga de senaste åren. Bland de riktigt populära fornnordiska namnen finns bland andra Astrid, Saga och Freja.\r\n\r\n<div class=\"footer-title\">Franska flicknamn / Franska tjejnamn</div>\r\n\r\nMånga av oss tycker att franska ord rullar av tungan så vältaligt och vackert. Vi listar franska varianter av de svenska namnen för att ge dig inspiration. Franska barnnamn är traditionellt heliga namn. Ofta med en liten twist med hjälp av bindestreck som exempelvis Marie-Élise.\r\n<div class=\"footer-title\">Internationella flicknamn</div>\r\n\r\nNamn har en särskild betydelse i varje kultur. Varje land och folkgrupp har sina egna historiska namn med vackra betydelser och budskap. Det är inte alltid klarlagt vart namnen kommer ifrån. Men många internationella flicknamn härstammar från engelsktalande kulturer. Det finns så många olika källor till internationella flicknamn som gör det svårt att berätta exakt var de kommer ifrån eller vad deras betydelse är. I många fall kommer främmande namn från heliga religiösa texter och berättelser. Katolska namn i sina olika former sprids runt om i Europa, USA och Latinamerika medan hinduiska namn finns i Indien och östra Asien och islamiska namn härrör från Mellanöstern. Till många av namnen i vår databas har vi lagt till information kring relaterade namn från andra länder.\r\n<div class=\"footer-title\">Populära tjejnamn / Populära flicknamn</div>\r\nVi har samlat listor på de mest populära namnen bland nyfödda flickor. Topp 100-listor för varje år tillbaks i tiden. Vi har också gjort det möjligt att filtrera på mer eller mindre vanliga namn. Vi visar hur vanligt namnet är i antal personer och hur frekvent det är olika åldersspann.',"read_more_words":120},
          {"id":18,"title":"column 3","position":"3","names":'<div class=\"footer-title\">Korta flicknamn / Korta tjejnamn</div>\r\nVissa gillar långa namn och andra gillar korta namn. Om barnet har ett långt efternamn kan det vara fint med ett kort förnamn. Oavsett vad du föredrar så har vi gjort det enkelt för dig. I sökresultatet finns en filtreringsfunktion du kan använda för att filtrera på antal bokstäver i namnet.\r\n\r\n<div class=\"footer-title\">Könsneutrala namn</div>\r\nUnisexnamn eller könsneutrala namn passar till både flickor och pojkar. Intresset för unisexnamn har tagit fart de senaste åren och blivit allt mer populära. Exempel på unisexnamn är Robin, Charlie, Alex, Mio, Kim, Mika, lo och Andrea. På filcknamn.se har vi samlat både namn som traditionellt sorteras in under flicknamn och unisexnamn. \r\n\r\n<div class=\"footer-title\">Fina flicknamn / Fina tjejnamn</div>\r\nVad som är ett fint flicknamn, vackert flicknamn eller coola namn är förstås individuellt. Samma namn upplevs många gånger helt annorlunda för olika personer. Ofta handlar det om tidigare relation till namnet. Det är vanligt att leta efter bebisnamn, söta flicknamn till sitt nyfödda barn. Just när barnet är nyfött kan det vara svårt att föreställa sig att det en dag kommer vara en vuxen kvinna. Men man behöver förstås välja ett namn som man tycker passar både för ett litet barn och en vuxen person.\r\n<div class=\"footer-title\">Utländska ovanliga flicknamn</div>\r\nJuanita, Natasha eller Angelina? Söker du ett ovanligt namn från utlandet? Vi har samlat utländska varianter av de svenska namnen. Klicka på info symbolen intill namnet i sökresultatet för mer information.\r\n<div class=\"footer-title\">Bibliska namn</div>\r\nMånga av de mest kända ”svenska” namnen kommer från bibeln. Det är många som inte reflekterat över att de faktiskt bär ett bibliskt namn som exempelvis Anna, Sara, Eva eller Susanna. Bibeln är en källa till några av de trendigaste namnen bland flickor.\r\n<div class=\"footer-title\">Gamla flicknamn / Gamla tjejnamn</div>\r\nGamla flicknamn är mycket populära igen. Det har visat sig att namn som var populära för 100 år sedan ofta brukar bli trendiga igen. Vi har gjort det enkelt att filtrera på namn som bärs av personer i olika åldersspann.',"read_more_words":120}]
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
