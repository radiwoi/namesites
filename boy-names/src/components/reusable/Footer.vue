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
        footerTexts: [
      {"id":12,"title":"column 1","position":"1","names":'<div class=\"footer-title\">\r\nPojknamn / Killnamn\r\n</div>\r\nVi har samlat folkbokförda svenska namn och varianter av dessa som traditionellt sorteras in under pojknamn och unisexnamn. Att välja ett namn till ditt barn kan ibland kännas överväldigande. Förutom dina egna uppslag kommer du säkerligen få förslag från vänner och släktingar, oavsett om du har bett om det eller inte.\r\n\r\nDet finns ingen metod som är rätt eller fel när man väljer namn. Det viktigaste är att välja ett namn som du verkligen tycker om. Oavsett vilket namn du bestämmer dig för så växer ditt barn tids nog in i sitt namn och det kommer att kännas naturligt. Nedan är några saker som kan vara bra att tänka på innan du bestämmer dig.\r\n\r\n\r\nDet kanske viktigaste är hur namnet faktiskt låter. Säg namnet högt och många gånger så du verkligen kan höra och känna hur det låter. Tänk på hur namnet kommer att låta när du ringer ditt barn: Är det trevligt att höra? Fungerar det bra tillsammans med det planerade efternamnet? Hur ser barnets initialer ut?\r\n\r\nFundera på hur du tycker ett längre förnamn fungerar tillsammans med ett kortare efternamn och vice versa. Att kombinera ett förnamn som slutar i en vokal med ett efternamn som börjar med en vokal kan göra att de flyter ihop och blir svårare att uppfatta.\r\n\r\nTror du namnet kommer att åldras väl? Ett namn som passar en förtjusande bebis eller ett litet barn kanske inte passar lika bra i vuxen ålder. \r\n\r\nFöräldrar väljer ofta namn som ska passa ihop. Syskonen får exempelvis namn som börjar på samma bokstav; som Ellen, Edvin och Elsa.\r\n\r\nVad kan du göra om familjemedlemmar pressar dig att ge ditt barn din älskade mormors namn - vilket inte är på din topp 10 lista? En praktisk lösning kan vara att ge ditt barn det namn du vill ha som förnamn och din mormors namn som mellannamn.\r\n<div class=\"footer-title\">Gamla pojknamn</div>\r\nLetar du efter fina gamla pojknamn? Vi har gjort det enkelt att filtrera på namn som är mer frekventa i olika åldersspann.',"read_more_words":120},
      {"id":13,"title":"column 2","position":"2","names":'<div class=\"footer-title\">Vad betyder namnet?</div>\r\nMånga som namnger sina barn idag tänker inte på att namnen som gavs förr faktiskt betydde något. Vi har samlat den ursprungliga betydelsen för olika namn. Registret är inte ännu komplett men vi fortsätter efterforskningarna och lägger till mer information löpande.\r\n<div class=\"footer-title\">Populära pojknamn</div>\r\nPå bondesamhällets tid fick äldste sonen ofta sin farfars namn. Vilka namn som är populära för tillfället förändras hela tiden. Men namn från den egna generationen eller två-tre steg bakåt i tiden brukar inte klättra så högt på namnlistorna. Vi har listat de populäraste namnen de senaste åren dessa hittar du här.\r\n<div class=\"footer-title\">Fina pojknamn / Fula pojknamn</div>\r\nVad är ett fint pojknamn / killnamn? Vad är ett fult pojknamn? Det är förstås ytterst individuellt och ofta handlar det om vilken relation man har till namnet sedan tidigare. Namn på personer vi inspireras av och tycker om blir naturligt kopplade till positiva känslor. Har namnet en positiv laddning under uppväxtåren tenderar det att hålla i sig även under de vuxna åren.\r\n<div class=\"footer-title\">Ovanliga killnamn / Ovanliga pojknamn</div> \r\nEn del föräldrar vill hitta ett unikt eller annorlunda pojknamn som skiljer ut deras barn. Vi har gjort det enkelt att se hur vanligt förekommande namnet är över hela befolkningen och frekvensen i olika åldersspann.',"read_more_words":120},
      {"id":14,"title":"column 3","position":"3","names":'<div class=\"footer-title\">Söker pojknamn på S</div>\r\nSöker du pojknamn på s, pojknamn på m, pojknamn på k eller någon annan bokstav så kan du enkelt hitta dessa genom att bara söka på den första bokstaven i namnet.\r\n<div class=\"footer-title\">Internationella pojknamn</div>\r\nSöker du danska pojknamn, amerikanska pojknamn, brittiska pojknamn eller nordiska pojknamn. Vi har samlat internationella varianter till de flesta svenska namn för att ge dig vidare inspiration.\r\n<div class=\"footer-title\">Typiska / klassiska svenska pojknamn</div>\r\nPojknamn som var populära för 100 år sedan är August, Ivar, Harry, Axel, Valter och Hugo. Detta är namn som också blivit populära idag och kan därför anses vara klassiska / typiska svenska pojknamn.\r\n<div class=\"footer-title\">Korta pojknamn</div>\r\nBo, Eli, Ian, Isak. Söker du ett kort namn eller ett namn med ett visst antal bokstäver? Efter att du gjort en sökning kan du filtrera på antal bokstäver i namnet. \r\n<div class=\"footer-title\">Svenska pojknamn</div>\r\nMånga namn vi upplever som klassiskt svenska har ofta sitt ursprung i andra kulturer. Många gånger är svenska namn variationer av tyska, franska och hebreiska namn.',"read_more_words":120}]

      }
  },
  methods: {

  },
//  .get("http://names_project.devhost1.com/api/v1/footer-texts/")
  mounted() {
    axios
      .get("https://pojknamn.se/api/v1/footer-texts/")
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
