"use strict";(self.webpackChunkFrontend_Juegos_2022=self.webpackChunkFrontend_Juegos_2022||[]).push([[610],{3610:(yt,S,c)=>{c.r(S),c.d(S,{JuegoModule:()=>_t});var d=c(6895),t=c(4650),h=c(1390);let Z=(()=>{class n{constructor(e){this.router=e}canActivate(e,i){return!!sessionStorage.getItem(e.data.Validate_game)||(this.router.navigate(["/juego"]),!1)}}return n.\u0275fac=function(e){return new(e||n)(t.LFG(h.F0))},n.\u0275prov=t.Yz7({token:n,factory:n.\u0275fac,providedIn:"root"}),n})();var u=c(5861),b=c(3276),v=c(529),P=c(9406),x=c(9661);let k=(()=>{class n{constructor(e,i,o){this.http=e,this.puente=i,this.publicityGame=o,this.publicityGameList=[],this.columna2=[5,6,7,8,9,10,1,2,3,4],this.columna3=[3,4,5,6,7,8,9,10,1,2],this.publicityGameListCol2=[],this.publicityGameListCol3=[],this.url=this.puente.geturl(),this.publicityGame.getAllPublicityGame().subscribe(a=>{this.publicityGameList=a,this.columna2.map(s=>{a.forEach(l=>{l.id==s&&this.publicityGameListCol2.push(l)})}),this.columna3.map(s=>{a.forEach(l=>{l.id==s&&this.publicityGameListCol3.push(l)})})})}getDesignInformation(){return this.http.get(`${this.url}api/design/`)}}return n.\u0275fac=function(e){return new(e||n)(t.LFG(v.eN),t.LFG(P.Q),t.LFG(x.D))},n.\u0275prov=t.Yz7({token:n,factory:n.\u0275fac,providedIn:"root"}),n})();var w=c(4870),A=c(7637),F=c(1782),L=c(3021),M=c(990),m=c(9808),Y=c(1172),z=c(9760),G=c(3867),U=c(8041),V=c(1131),Q=c(3398);let f=(()=>{class n{constructor(e,i,o,a,s,l,g){this.ticketService=e,this.matchService=i,this.gameDataSrv=o,this.awardConditionSrv=a,this.awardSrv=s,this.game=l,this.probabilityService=g,this.match={},this.attempts=0,this.winnersLimit=0,this.winProb=0,this.winner=!1,this.winFirstTime=!1}verifyTicket(e){var i=this;return(0,u.Z)(function*(){console.log("Dentro de verifyTicket",e);const o=yield(0,m.n)(i.ticketService.getFilter("?&state=Disponible&qr_code_digits="+e));if(console.log("Dentro de verifyTicket",o),o.length>0){let a,s,l;i.ticket=o[0];const g=yield(0,m.n)(i.game.getById(1));return a=new Date(i.ticket.date_created_nf),console.log(a),s=new Date(g.start_date_nf),l=new Date(g.end_date_nf),s<=a&&l>=a}return!1})()}playGame(){var e=this;return(0,u.Z)(function*(){if(yield e.deleteAwardConditionPast(),yield e.checkLimitWinners())e.changeStateTicket(e.ticket.id),e.createMatch("false","false",e.ticket.id,null),e.setWinnerState(!1);else{let i=yield e.getAwardConditionToday();if(i&&i.length>0){let o=i[0],a=e.winnedAward(o);e.winCase(a.id,o.id,!0),console.log(e.winner)}else{let o=yield e.getPrize();o?e.winCase(o[0].id,null,!1):(e.changeStateTicket(e.ticket.id),e.createMatch("false","false",e.ticket.id,null),e.setWinnerState(!1))}}})()}winCase(e,i,o){this.createMatch("true","false",this.ticket.id,e),this.changeStateTicket(this.ticket.id),this.setWinnerState(!0),o?this.wonAwardCondition(e,i):this.wonAward(e)}getAwardConditionToday(){var e=this;return(0,u.Z)(function*(){let i=new Date,o=e.gameDataSrv.DateFormat(i),a="?is_approved=false&start_date__lte="+o+"&end_date__gte="+o;return yield(0,m.n)(e.awardConditionSrv.getAwardConditionFilter(a))})()}winnedAward(e){return(0,u.Z)(function*(){})()}wonAward(e){var i=this;return(0,u.Z)(function*(){let o=new FormData;o.append("won_award","true"),yield(0,m.n)(i.awardSrv.winAward(e,o))})()}wonAwardCondition(e,i){var o=this;return(0,u.Z)(function*(){let a=new FormData;a.append("won_award","true"),yield(0,m.n)(o.awardSrv.winAwardCondition(e,a));let s=new FormData;s.append("state","true"),yield(0,m.n)(o.awardConditionSrv.changeState(i,s))})()}changeStateTicket(e){var i=this;return(0,u.Z)(function*(){let o=new FormData;o.append("state","true"),yield(0,m.n)(i.ticketService.changeStateTicket(e,o))})()}deleteAwardConditionPast(){var e=this;return(0,u.Z)(function*(){let o=yield(0,m.n)(e.awardConditionSrv.getAwardConditionFilter("?is_approved=false")),a=new Date;for(let s in o)new Date(o[s].end_date_nf)<a&&(yield(0,m.n)(e.awardConditionSrv.deleteAwardCondition(o[s].id)))})()}getPrize(){var e=this;return(0,u.Z)(function*(){let a=Math.floor(1001*Math.random())+0,s="";if(a<=10*e.winProb){a=Math.floor(1001*Math.random())+0,a<=800?s="Com\xfan":a<=900?s="Rara":a<=990?s="\xc9pica":a<=1e3&&(s="Legendaria");let l=yield e.getAwardsCategory(s);return l.length>0?l:null}return null})()}getAwardsCategory(e){var i=this;return(0,u.Z)(function*(){return(yield(0,m.n)(i.awardSrv.getFilterAward("?is_active=true"))).filter(s=>s.category==e)})()}checkLimitWinners(){var e=this;return(0,u.Z)(function*(){let i=yield(0,m.n)(e.probabilityService.getProbabilites());e.winProb=i.percent_win,e.attempts=i.attempts_limit,e.winnersLimit=i.winners_limit;let o=new Date,a=e.gameDataSrv.DateFormat(o).split("T")[0];return(yield e.getWinnMatchesToday(a)).length>=e.winnersLimit&&(e.setWinnerState(!1),!0)})()}getWinnMatchesToday(e){var i=this;return(0,u.Z)(function*(){let o="?win_match=true&start_date__date__range="+e+"%2C"+e;return yield(0,m.n)(i.matchService.getMatchFilter(o))})()}createMatch(e,i,o,a){let s={ticket:o,award:a,win_match:e,delivered:i};this.match=s,this.matchService.postMatch(s)}setWinnerState(e){this.winner=e}decreaseAttemptCount(){this.attempts--}}return n.\u0275fac=function(e){return new(e||n)(t.LFG(Y.w),t.LFG(z.Q),t.LFG(G.V),t.LFG(U.r),t.LFG(V.q),t.LFG(L.h),t.LFG(Q.g))},n.\u0275prov=t.Yz7({token:n,factory:n.\u0275fac,providedIn:"root"}),n})(),I=(()=>{class n{constructor(e,i){this.http=e,this.puente=i,this.url=this.puente.geturl()}setAudioFile(e){this.audioFile=e}getAudioFile(e){return this.audioFile}getAll(){return this.http.get(this.url+"api/audio/")}getById(e){return this.http.get(this.url+"api/audio/"+e+"/")}post(e){return this.http.post(this.url+"api/audio/",e)}put(e,i){return this.http.put(this.url+"api/audio/"+e+"/",i)}delete(e){return this.http.delete(this.url+"api/audio/"+e+"/")}}return n.\u0275fac=function(e){return new(e||n)(t.LFG(v.eN),t.LFG(P.Q))},n.\u0275prov=t.Yz7({token:n,factory:n.\u0275fac,providedIn:"root"}),n})(),C=(()=>{class n{constructor(){this.title="Empezar",this.fontSize="1.6rem",this.styledPadding="1rem 1.5rem",this.color="white",this.color_background="red",this.disabled=!1}ngOnInit(){}}return n.\u0275fac=function(e){return new(e||n)},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-generic-button"]],inputs:{title:"title",fontSize:"fontSize",styledPadding:"styledPadding",color:"color",color_background:"color_background",disabled:"disabled"},decls:2,vars:10,consts:[[1,"generic-btn",3,"disabled"]],template:function(e,i){1&e&&(t.TgZ(0,"button",0),t._uU(1),t.qZA()),2&e&&(t.Udp("font-size",i.fontSize)("padding",i.styledPadding)("color",i.color)("background",i.color_background),t.Q6J("disabled",i.disabled),t.xp6(1),t.hij(" ",i.title,"\n"))},styles:[".generic-btn[_ngcontent-%COMP%]{padding:1rem 1.5rem;font-size:1.2rem;margin:0;text-align:center;border-radius:35px;outline:none;border:none}"]}),n})();const D=["scrollContainer"];function B(n,r){if(1&n&&(t.TgZ(0,"figure",6),t._UZ(1,"img",7),t.qZA()),2&n){const e=r.$implicit;t.xp6(1),t.Q6J("src",e.image,t.LSH)}}let T=(()=>{class n{constructor(e){this.publicity=e,this.publicityList=[],this.animationCount=0,this.isTop=!0,this.timeIntervalTop=1e3,this.timeIntervalBottom=1e3}ngOnInit(){this.publicity.getPublicityConfigTop().subscribe(e=>{this.timeIntervalTop=1e3*e.time_display,this.publicity.getPublicityConfigBottom().subscribe(i=>{this.timeIntervalBottom=1e3*i.time_display,this.createInterval(this.isTop?this.timeIntervalTop:this.timeIntervalBottom)})})}createInterval(e){let i;i=setInterval(()=>{this.scrollContainer.nativeElement.style.transform=`translateX(${-100*this.animationCount}%)`,this.scrollContainer.nativeElement.style.transition="transform .3s cubic-bezier(0.61, 1, 0.88, 1)",this.animationCount==this.publicityList.length?setTimeout(()=>{this.scrollContainer.nativeElement.style.transform="translateX(0px)",this.scrollContainer.nativeElement.style.transition="transform 0.3s",this.animationCount=0}):this.animationCount<this.publicityList.length&&this.animationCount++},e)}}return n.\u0275fac=function(e){return new(e||n)(t.Y36(A.U))},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-publicity"]],viewQuery:function(e,i){if(1&e&&t.Gf(D,5),2&e){let o;t.iGM(o=t.CRH())&&(i.scrollContainer=o.first)}},inputs:{publicityList:"publicityList",isTop:"isTop"},decls:6,vars:1,consts:[[1,"container-fluid","publicity_container","p-0"],[1,"scroll-container"],["scrollContainer",""],["class","publicity_img-container",4,"ngFor","ngForOf"],["controls","None","loop","","hidden",""],["src","./assets/audio/idle_music.mp3","type","audio/mp3"],[1,"publicity_img-container"],["alt","publicity-img",1,"publicity_img",3,"src"]],template:function(e,i){1&e&&(t.TgZ(0,"div",0)(1,"div",1,2),t.YNc(3,B,2,1,"figure",3),t.qZA(),t.TgZ(4,"audio",4),t._UZ(5,"source",5),t.qZA()()),2&e&&(t.xp6(3),t.Q6J("ngForOf",i.publicityList))},dependencies:[d.sg],styles:[".publicity_container[_ngcontent-%COMP%]{background-color:#0ff;position:relative;height:15vh;display:flex;overflow:hidden;scroll-behavior:smooth}.scroll-container[_ngcontent-%COMP%]{display:flex;width:100%;scroll-behavior:smooth;align-items:center}.publicity_img-container[_ngcontent-%COMP%], img[_ngcontent-%COMP%]{padding:0;margin:0}.publicity_img-container[_ngcontent-%COMP%]{min-width:100%;height:100%}.publicity_img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),n})(),N=(()=>{class n{constructor(e,i,o,a,s,l,g,p,_,ft){this.dashPublicity=e,this.themeService=i,this.styles=o,this.publicity=a,this.router=s,this.AuthSrv=l,this.GameSrv=g,this.confirmDialog=p,this.Gamelogic=_,this.audioService=ft,this.backgroundImgUrl="",this.buttonTitle="",this.logoImage="",this.videoUrl="",this.boxes_images=0,this.design_images=0,this.audio=new Audio,this.audioArray=[]}ngOnInit(){var e=this;return(0,u.Z)(function*(){yield e.auth(),e.validateSlot(),sessionStorage.removeItem("juego_scan"),sessionStorage.removeItem("juego_play"),e.publicity.getPublicityTopList().subscribe(i=>{i.length>0&&(e.dashPublicity.loadTopData(i),e.publicity.getPublicityBottomList().subscribe(o=>{e.dashPublicity.loadBottomData(o)})),e.themeService.getDesignInformation().subscribe(o=>{e.styles.loadData(o[0]),e.buttonTitle=e.styles.get_title_button_screensaver(),e.logoImage=e.styles.get_image_logo_game(),e.videoUrl=e.styles.get_video_screensaver()})})})()}goScan(){var e=this;return(0,u.Z)(function*(){yield e.validateSlot(),10==e.boxes_images&&3==e.design_images?(e.router.navigate(["/juego/scan"]),sessionStorage.setItem("juego_scan","juego_scan")):e.confirmDialog.error(["Revise que esten todas las im\xe1genes de las casillas","Revise que este el contenedor del juego","Revise que este el logo del juego","Revise que este la imagen al ganar"])})()}auth(){var e=this;return(0,u.Z)(function*(){let i=new FormData;i.append("username","admin"),i.append("password","admin"),e.AuthSrv.auth_token(i).subscribe(o=>{sessionStorage.setItem("token",o.access),sessionStorage.setItem("refresh",o.refresh)})})()}validateSlot(){var e=this;return(0,u.Z)(function*(){e.GameSrv.getPublicityGame().subscribe(i=>{for(let o of i)o.image&&(e.boxes_images+=1)}),e.GameSrv.getDesign().subscribe(i=>{for(let o of i)o.image_machine_game&&(e.design_images+=1),o.image_logo_game&&(e.design_images+=1),o.image_winner&&(e.design_images+=1)})})()}}return n.\u0275fac=function(e){return new(e||n)(t.Y36(b.E),t.Y36(k),t.Y36(w.T),t.Y36(A.U),t.Y36(h.F0),t.Y36(F.e),t.Y36(L.h),t.Y36(M.D),t.Y36(f),t.Y36(I))},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-juego"]],decls:7,vars:10,consts:[[3,"publicityList"],[1,"container-fluid","home_container","p-0","m-0"],[1,"home-image_container",3,"autoplay","muted","loop","src"],[1,"home-btn_container"],[1,"home_btn",3,"title","fontSize","styledPadding","click"],[3,"publicityList","isTop"]],template:function(e,i){1&e&&(t.TgZ(0,"div"),t._UZ(1,"app-publicity",0),t.TgZ(2,"div",1),t._UZ(3,"video",2),t.TgZ(4,"div",3)(5,"app-generic-button",4),t.NdJ("click",function(){return i.goScan()}),t.qZA()()(),t._UZ(6,"app-publicity",5),t.qZA()),2&e&&(t.xp6(1),t.Q6J("publicityList",i.dashPublicity.getTopPublicityList()),t.xp6(2),t.Q6J("autoplay",!0)("muted","muted")("loop",!0)("src",i.videoUrl,t.LSH),t.xp6(2),t.Q6J("title",i.buttonTitle)("fontSize","2.8rem")("styledPadding","3.4rem 6.6rem"),t.xp6(1),t.Q6J("publicityList",i.dashPublicity.getBottomPublicityList())("isTop",!1))},dependencies:[C,T],styles:[".home_container[_ngcontent-%COMP%]{position:relative;width:100%;height:70vh;overflow-y:hidden;overflow-x:hidden}.home-image_container[_ngcontent-%COMP%]{position:relative;height:100%;width:100%;background-color:#3b3b3b}.home-logo__container[_ngcontent-%COMP%]{position:absolute;min-width:20rem;height:15rem;left:calc(50% - 203px);z-index:2}img[_ngcontent-%COMP%]{width:100%;height:100%}.home_background[_ngcontent-%COMP%]{width:100%;height:100%;max-height:77.1rem}.home-shadow[_ngcontent-%COMP%]{background:#000000a1;height:100%;width:100%;position:absolute;top:0}.home-btn_container[_ngcontent-%COMP%]{width:100%;position:absolute;display:flex;justify-content:center;bottom:calc(10% + 10px)}"]}),n})(),J=(()=>{class n{constructor(){this.code=""}getCode(){return this.code}setCode(e){this.code=this.code+e}deleteLastValue(){this.code=this.code.substring(0,this.code.length-1)}}return n.\u0275fac=function(e){return new(e||n)},n.\u0275prov=t.Yz7({token:n,factory:n.\u0275fac,providedIn:"root"}),n})();var y=c(4006),j=c(7392);const q=function(){return{"font-size":"56px",height:"43px",width:"68px"}};let K=(()=>{class n{constructor(e){this.KeyControllerService=e}ngOnInit(){}getButtonValue(e){let i=e.target;i.textContent&&this.KeyControllerService.setCode(i.textContent.trim()),console.log(i.textContent)}deleteValue(){this.KeyControllerService.deleteLastValue()}}return n.\u0275fac=function(e){return new(e||n)(t.Y36(J))},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-keyboard"]],decls:29,vars:2,consts:[[1,"container-fluid","text-center"],[1,"keyboard-container"],[1,"row","keyboard-row"],[1,"col","btn",3,"click"],[1,"col-7","btn",3,"click"],["value","delete",1,"col-4","btn",3,"click"],[3,"ngStyle"]],template:function(e,i){1&e&&(t.TgZ(0,"div",0)(1,"div",1)(2,"div",2)(3,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(4," 1 "),t.qZA(),t.TgZ(5,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(6," 2 "),t.qZA(),t.TgZ(7,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(8," 3 "),t.qZA()(),t.TgZ(9,"div",2)(10,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(11," 4 "),t.qZA(),t.TgZ(12,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(13," 5 "),t.qZA(),t.TgZ(14,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(15," 6 "),t.qZA()(),t.TgZ(16,"div",2)(17,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(18," 7 "),t.qZA(),t.TgZ(19,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(20," 8 "),t.qZA(),t.TgZ(21,"button",3),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(22," 9 "),t.qZA()(),t.TgZ(23,"div",2)(24,"button",4),t.NdJ("click",function(a){return i.getButtonValue(a)}),t._uU(25," 0 "),t.qZA(),t.TgZ(26,"button",5),t.NdJ("click",function(){return i.deleteValue()}),t.TgZ(27,"mat-icon",6),t._uU(28,"keyboard_backspace"),t.qZA()()()()()),2&e&&(t.xp6(27),t.Q6J("ngStyle",t.DdM(1,q)))},dependencies:[d.PC,j.Hw],styles:[".btn[_ngcontent-%COMP%]{background-color:#fff;border-radius:45px;padding:1.3rem .2rem;font-size:2.8rem}.keyboard-container[_ngcontent-%COMP%]{display:flex;flex-direction:column;gap:1.5rem;width:34rem;height:32rem;font-size:1.6rem}.keyboard-row[_ngcontent-%COMP%]{gap:1.6rem}"]}),n})();const H=function(n,r,e){return{"home-logo__container":n,logo__container:r,"logo__container-background":e}};let O=(()=>{class n{constructor(){this.height="15rem",this.isHome=!0,this.isBackground=!1,this.urlImage=""}ngOnInit(){}}return n.\u0275fac=function(e){return new(e||n)},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-logo"]],inputs:{height:"height",isHome:"isHome",isBackground:"isBackground",urlImage:"urlImage"},decls:2,vars:8,consts:[[1,"p-0","m-0",3,"ngClass"],["alt","home-logo",1,"p-0","m-0",3,"src"]],template:function(e,i){1&e&&(t.TgZ(0,"figure",0),t._UZ(1,"img",1),t.qZA()),2&e&&(t.Udp("height",i.height),t.Q6J("ngClass",t.kEZ(4,H,i.isHome,!i.isHome,i.isBackground)),t.xp6(1),t.Q6J("src",i.urlImage,t.LSH))},dependencies:[d.mk],styles:[".home-logo__container[_ngcontent-%COMP%]{position:absolute;height:15rem;width:47rem;left:calc(50% - 205px);top:calc(0% + 20px);z-index:2}.logo__container[_ngcontent-%COMP%]{position:absolute;height:15rem;top:2px;z-index:2}.logo__container-background[_ngcontent-%COMP%]{position:absolute;height:15rem;top:calc(40% + 20px);left:calc(50% - 364px);z-index:2}img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),n})();function E(n,r){if(1&n&&(t.TgZ(0,"div",16)(1,"h2",17),t._uU(2),t.qZA(),t.TgZ(3,"p",18),t._uU(4),t.qZA()()),2&n){const e=t.oxw();t.xp6(2),t.Oqu(e.styles.get_scan_code_title()),t.xp6(2),t.hij(" ",e.styles.get_scan_code_description()," ")}}function $(n,r){1&n&&(t.TgZ(0,"div",16)(1,"h2",17),t._uU(2,"Ingrese el c\xf3digo"),t.qZA()())}function R(n,r){1&n&&(t.TgZ(0,"figure",19),t._UZ(1,"img",20),t.qZA())}function W(n,r){1&n&&t._UZ(0,"app-keyboard")}let X=(()=>{class n{constructor(e,i,o,a,s,l){this.router=e,this.publicity=i,this.styles=o,this.keyController=a,this.gameLogic=s,this.confirmDialog=l,this.selectedInputCode=!1,this.scanState=!0,this.explication="Puedes escanear el c\xf3digo QR de tu ticket",this.code=this.keyController.getCode()}ngOnInit(){}changeView(){this.scanState=!1,this.keyController.setCode("")}continueToGame(){var e=this;return(0,u.Z)(function*(){if(""!=e.keyController.getCode()){let i=e.gameLogic.verifyTicket(e.keyController.getCode());console.log("Codigo ingresado",e.code),(yield i)?(console.log("dentro del if"+i),e.router.navigate(["/juego/play"]),sessionStorage.setItem("juego_play","juego_play"),e.gameLogic.playGame()):e.confirmDialog.error(["El ticket que ingres\xf3 no existe o ya fu\xe9 reclamado, revise si la informacion ingresada es correcta","\xd3","La fecha disponible del ticket est\xe1 fuera del rango de disponibilidad del juego"])}})()}doSomething(){sessionStorage.removeItem("juego_scan")}}return n.\u0275fac=function(e){return new(e||n)(t.Y36(h.F0),t.Y36(b.E),t.Y36(w.T),t.Y36(J),t.Y36(f),t.Y36(M.D))},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-scan-view"]],decls:17,vars:15,consts:[["contenteditable","true",1,"scan_container","p-0","m-0",3,"beforeunload"],[3,"publicityList"],[1,"container-menu"],["height","25rem",3,"isBackground","urlImage"],[1,"scan-shadow"],[1,"scan_menu-container"],[1,"menu-container_img-container"],["height","22rem",3,"urlImage","isHome"],["class","menu-info",4,"ngIf"],["class","menu-container_scan-img-container",4,"ngIf"],[4,"ngIf"],["type","text","onkeypress","return event.charCode >= 48 && event.charCode <= 57",1,"btn","menu__input",3,"ngModel","click","ngModelChange"],["codeInput","ngModel"],["title","Continuar",1,"mb-2",3,"fontSize","styledPadding","click"],["autoplay","","loop","","controls","None","hidden","","src","./assets/audio/playing_music.mp3",3,"volume"],[3,"publicityList","isTop"],[1,"menu-info"],[1,"scan_title"],[1,"explication-text"],[1,"menu-container_scan-img-container"],["src","../../../assets/img/codigoQR.png","alt","scan-logo",1,"menu-container_scan-img"]],template:function(e,i){1&e&&(t.TgZ(0,"div",0),t.NdJ("beforeunload",function(){return i.doSomething()},!1,t.Jf7),t._UZ(1,"app-publicity",1),t.TgZ(2,"div",2),t._UZ(3,"app-logo",3)(4,"div",4),t.TgZ(5,"div",5)(6,"div",6),t._UZ(7,"app-logo",7),t.qZA(),t.YNc(8,E,5,2,"div",8),t.YNc(9,$,3,0,"div",8),t.YNc(10,R,2,0,"figure",9),t.YNc(11,W,1,0,"app-keyboard",10),t.TgZ(12,"input",11,12),t.NdJ("click",function(){return i.changeView()})("ngModelChange",function(a){return i.keyController.code=a}),t.qZA(),t.TgZ(14,"app-generic-button",13),t.NdJ("click",function(){return i.continueToGame()}),t.qZA()()(),t._UZ(15,"audio",14)(16,"app-publicity",15),t.qZA()),2&e&&(t.xp6(1),t.Q6J("publicityList",i.publicity.getTopPublicityList()),t.xp6(2),t.Q6J("isBackground",!0)("urlImage",i.styles.get_image_logo_game()),t.xp6(4),t.Q6J("urlImage",i.styles.get_image_logo_game())("isHome",!1),t.xp6(1),t.Q6J("ngIf",i.scanState),t.xp6(1),t.Q6J("ngIf",!i.scanState),t.xp6(1),t.Q6J("ngIf",i.scanState),t.xp6(1),t.Q6J("ngIf",!i.scanState),t.xp6(1),t.Q6J("ngModel",i.keyController.code),t.xp6(2),t.Q6J("fontSize","2.8rem")("styledPadding","2.4rem 6.6rem"),t.xp6(1),t.Q6J("volume",.05),t.xp6(1),t.Q6J("publicityList",i.publicity.getBottomPublicityList())("isTop",!1))},dependencies:[d.O5,y.Fj,y.JJ,y.On,C,K,T,O],styles:[".scan_container[_ngcontent-%COMP%]{position:relative;background-color:gray;width:100%}.container-menu[_ngcontent-%COMP%]{position:relative;height:71%;width:100%;background-color:#000}.scan-shadow[_ngcontent-%COMP%]{height:71%;width:100%;position:absolute;background-color:#000000d4;z-index:2}.scan_menu-container[_ngcontent-%COMP%]{position:relative;height:70vh;width:100%;display:flex;flex-direction:column;align-items:center;gap:3rem;z-index:3}.scan_title[_ngcontent-%COMP%]{margin:0;font-size:3.8rem}.menu-container_img-container[_ngcontent-%COMP%]{width:39rem;height:19rem;min-height:4rem;margin:0 1rem 1rem 0}.menu-info[_ngcontent-%COMP%]{display:flex;flex-direction:column;align-items:center;color:#fff;font-size:3.8rem;gap:2.4rem;margin-top:25px}.menu-container_img[_ngcontent-%COMP%]{border-radius:25px}.explication-text[_ngcontent-%COMP%]{padding:0 2rem;line-height:initial;text-align:center;width:83%}.menu-container_scan-img-container[_ngcontent-%COMP%]{min-height:16rem;width:19rem}.menu__input[_ngcontent-%COMP%]{border:5px solid red;outline:none;border-radius:33px;background-color:#000;color:#fff;padding:1rem .5rem;width:37rem;font-size:2.8rem}p[_ngcontent-%COMP%], figure[_ngcontent-%COMP%]{margin:0}img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),n})(),tt=(()=>{class n{constructor(e){this.gameLogicService=e,this.columna1=[1,2,3,4,5,6,7,8,9,10],this.columna2=[5,6,7,8,9,10,1,2,3,4],this.columna3=[3,4,5,6,7,8,9,10,1,2],this.widthImage=270,this.animationCountCol1=5,this.disabledPlayButton=!1}startGame(e,i,o){if(this.gameLogicService.winFirstTime=!1,this.gameLogicService.attempts>0){if(this.disabledPlayButton=!0,this.gameLogicService.winner){const a=Math.floor(9*Math.random())+1;console.log("Indice a ganar: "+a);const s=setInterval(()=>{let l=-9*this.widthImage;if(console.log("ejecucion setTimeout"),console.log(this.animationCountCol1),console.log(`numero ganador: ${a}`),this.animationCountCol1>0)this.animationCountCol1-=1,console.log(e),e.style.transform=`translateY(${l}px)`,e.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",i.style.transform=`translateY(${l}px)`,i.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",o.style.transform=`translateY(${l}px)`,o.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",setTimeout(()=>{e.style.transform="translateY(0px)",e.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",i.style.transform="translateY(0px)",i.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",o.style.transform="translateY(0px)",o.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)"},1e3);else{let p,_,g=(a-1)*this.widthImage*-1;p=a>=5?(a-5)*this.widthImage*-1:(a+5)*this.widthImage*-1,_=a>=3?(a-3)*this.widthImage*-1:(a+7)*this.widthImage*-1,console.log("MOVIMIENTOS COL2: ",p),e.style.transform="translateY(0px)",e.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",i.style.transform="translateY(0px)",i.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",o.style.transform="translateY(0px)",o.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",e.style.transform=`translateY(${g}px)`,e.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",i.style.transform=`translateY(${p}px)`,i.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",o.style.transform=`translateY(${_}px)`,o.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",this.animationCountCol1=5,this.disabledPlayButton=!1,this.gameLogicService.winFirstTime=!0,clearInterval(s)}},1030)}else{const a=setInterval(()=>{let s=-9*this.widthImage;console.log("ejecucion setTimeout"),console.log(this.animationCountCol1),this.animationCountCol1>0?(this.animationCountCol1-=1,console.log(e),e.style.transform=`translateY(${s}px)`,e.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",i.style.transform=`translateY(${s}px)`,i.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",o.style.transform=`translateY(${s}px)`,o.style.transition="transform 1s cubic-bezier(.17,.67,.83,.67)",setTimeout(()=>{e.style.transform="translateY(0px)",e.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",i.style.transform="translateY(0px)",i.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)",o.style.transform="translateY(0px)",o.style.transition="transform 0s cubic-bezier(.17,.67,.83,.67)"},1e3)):(this.animationCountCol1=5,this.disabledPlayButton=!1,clearInterval(a))},1030)}this.gameLogicService.setWinnerState(!1),this.gameLogicService.decreaseAttemptCount()}else window.location.reload()}}return n.\u0275fac=function(e){return new(e||n)(t.LFG(f))},n.\u0275prov=t.Yz7({token:n,factory:n.\u0275fac,providedIn:"root"}),n})();function et(n,r){1&n&&(t.TgZ(0,"p",27),t._uU(1,"No te quedan m\xe1s Giros!"),t.qZA())}function it(n,r){1&n&&(t.TgZ(0,"p",27),t._uU(1,"Disponible 1 Giro m\xe1s!"),t.qZA())}function nt(n,r){if(1&n&&(t.TgZ(0,"p",27),t._uU(1),t.qZA()),2&n){const e=t.oxw(2);t.xp6(1),t.hij(" Disponible ",e.gameLogicService.attempts," Giros m\xe1s! ")}}function ot(n,r){1&n&&(t.TgZ(0,"p",27),t._uU(1,"HAS GANADO!!!"),t.qZA(),t.TgZ(2,"audio",30),t._UZ(3,"source",31),t.qZA())}function at(n,r){if(1&n&&(t.YNc(0,nt,2,1,"p",28),t.YNc(1,ot,4,0,"ng-template",null,29,t.W1O)),2&n){const e=t.MAs(2),i=t.oxw();t.Q6J("ngIf",0==i.gameLogicService.winFirstTime)("ngIfElse",e)}}function rt(n,r){if(1&n&&(t.TgZ(0,"figure",32),t._UZ(1,"img",33),t.qZA()),2&n){const e=t.oxw();t.xp6(1),t.Q6J("src",e.styles.get_image_winner(),t.LSH)}}function st(n,r){if(1&n&&(t.TgZ(0,"figure",34),t._UZ(1,"img",35),t.qZA()),2&n){const e=r.$implicit;t.xp6(1),t.Q6J("src",e.image,t.LSH)}}function lt(n,r){if(1&n&&(t.TgZ(0,"figure",34),t._UZ(1,"img",35),t.qZA()),2&n){const e=r.$implicit;t.xp6(1),t.Q6J("src",e.image,t.LSH)}}function ct(n,r){if(1&n&&(t.TgZ(0,"figure",34),t._UZ(1,"img",35),t.qZA()),2&n){const e=r.$implicit;t.xp6(1),t.Q6J("src",e.image,t.LSH)}}function ut(n,r){1&n&&(t.TgZ(0,"div")(1,"audio",30),t._UZ(2,"source",36),t.qZA()())}const mt=function(){return{color:"styles.color_text"}},gt=function(){return{color:"styles.get_color_text()"}},dt=[{path:"",component:N},{path:"scan",component:X,canActivate:[Z],data:{Validate_game:"juego_scan"}},{path:"play",component:(()=>{class n{constructor(e,i,o,a,s,l,g){this.publicity=e,this.styles=i,this.animation=o,this.theme=a,this.publicityGame=s,this.gameLogicService=l,this.audioService=g,this.informationText="A JUGAR!",this.slot_music=!1,this.probability={}}doSomething(){sessionStorage.removeItem("juego_play")}music(){this.gameLogicService.attempts>=0&&(console.log("Intentos:",this.gameLogicService.attempts),this.slot_music=!0,setTimeout(()=>{this.slot_music=!1},6e3))}}return n.\u0275fac=function(e){return new(e||n)(t.Y36(b.E),t.Y36(w.T),t.Y36(tt),t.Y36(k),t.Y36(x.D),t.Y36(f),t.Y36(I))},n.\u0275cmp=t.Xpm({type:n,selectors:[["app-play-view"]],decls:32,vars:22,consts:[["contenteditable","true",1,"container-fullscreen","p-0","m-0",3,"beforeunload"],[3,"publicityList"],[1,"container-menu"],["height","25rem",3,"urlImage","isBackground"],[1,"scan-shadow"],[1,"scan_menu-container"],[1,"menu-container_img-container"],["height","22rem",3,"urlImage","isHome"],[1,"info-game__text",3,"ngStyle"],[1,"information-game-container",3,"ngPlural","ngStyle"],["ngPluralCase","=0"],["class","info-game__text","ngPluralCase","=1"],["class","info-game__text","ngPluralCase","other"],[1,"spinner__container"],["class","winner-container",4,"ngIf"],[1,"award-box-container"],["alt","cajon-premios",1,"awards-box",3,"src"],[1,"awards-container"],[1,"awards-column"],["col1",""],["class","award-image-container",4,"ngFor","ngForOf"],["col2",""],["col3",""],["title","Girar",1,"mb-2","container_play-btn",3,"disabled","fontSize","styledPadding","click"],[4,"ngIf"],["autoplay","","loop","","controls","None","hidden","","src","./assets/audio/playing_music.mp3",3,"volume"],[3,"publicityList","isTop"],[1,"info-game__text"],["class","info-game__text",4,"ngIf","ngIfElse"],["winText",""],["controls","None","hidden","","autoplay",""],["src","./assets/audio/win.mp3","type","audio/mp3"],[1,"winner-container"],["alt"," winner-img",3,"src"],[1,"award-image-container"],["alt","publicityLogo",3,"src"],["src","./assets/audio/tragaperras.mp3","type","audio/mp3"]],template:function(e,i){if(1&e){const o=t.EpF();t.TgZ(0,"div",0),t.NdJ("beforeunload",function(){return i.doSomething()},!1,t.Jf7),t._UZ(1,"app-publicity",1),t.TgZ(2,"div",2),t._UZ(3,"app-logo",3)(4,"div",4),t.TgZ(5,"div",5)(6,"div",6),t._UZ(7,"app-logo",7),t.qZA(),t.TgZ(8,"p",8),t._uU(9," A JUGAR!!! "),t.qZA(),t.TgZ(10,"div",9),t.YNc(11,et,2,0,"ng-template",10),t.YNc(12,it,2,0,"ng-template",11),t.YNc(13,at,3,2,"ng-template",12),t.qZA(),t.TgZ(14,"div",13),t.YNc(15,rt,2,1,"figure",14),t.TgZ(16,"figure",15),t._UZ(17,"img",16),t.qZA(),t.TgZ(18,"div",17)(19,"div",18,19),t.YNc(21,st,2,1,"figure",20),t.qZA(),t.TgZ(22,"div",18,21),t.YNc(24,lt,2,1,"figure",20),t.qZA(),t.TgZ(25,"div",18,22),t.YNc(27,ct,2,1,"figure",20),t.qZA()()(),t.TgZ(28,"app-generic-button",23),t.NdJ("click",function(){t.CHM(o);const s=t.MAs(20),l=t.MAs(23),g=t.MAs(26);return i.animation.startGame(s,l,g),t.KtG(i.music())}),t.YNc(29,ut,3,0,"div",24),t.qZA()()(),t._UZ(30,"audio",25)(31,"app-publicity",26),t.qZA()}2&e&&(t.xp6(1),t.Q6J("publicityList",i.publicity.getTopPublicityList()),t.xp6(2),t.Q6J("urlImage",i.styles.get_image_logo_game())("isBackground",!0),t.xp6(4),t.Q6J("urlImage",i.styles.get_image_logo_game())("isHome",!1),t.xp6(1),t.Q6J("ngStyle",t.DdM(20,mt)),t.xp6(2),t.Q6J("ngPlural",i.gameLogicService.attempts)("ngStyle",t.DdM(21,gt)),t.xp6(5),t.Q6J("ngIf",1==i.gameLogicService.winFirstTime),t.xp6(2),t.Q6J("src",i.styles.get_image_machine_game(),t.LSH),t.xp6(4),t.Q6J("ngForOf",i.theme.publicityGameList),t.xp6(3),t.Q6J("ngForOf",i.theme.publicityGameListCol2),t.xp6(3),t.Q6J("ngForOf",i.theme.publicityGameListCol3),t.xp6(1),t.Q6J("disabled",i.animation.disabledPlayButton)("fontSize","2.8rem")("styledPadding","2.4rem 6.6rem"),t.xp6(1),t.Q6J("ngIf",i.slot_music),t.xp6(1),t.Q6J("volume",.05),t.xp6(1),t.Q6J("publicityList",i.publicity.getBottomPublicityList())("isTop",!1))},dependencies:[d.sg,d.O5,d.PC,d.iq,d.zE,C,T,O],styles:[".scan_menu-container[_ngcontent-%COMP%]{position:relative;height:100%;width:100%;display:flex;flex-direction:column;align-items:center;gap:4.5rem;z-index:3}.container-menu[_ngcontent-%COMP%]{position:relative;height:70vh;width:100%;background-color:#000}.scan-shadow[_ngcontent-%COMP%]{height:70vh;width:100%;position:absolute;background-color:#000000d4;z-index:2}.menu-container_img-container[_ngcontent-%COMP%]{width:39rem;height:19rem;min-height:4rem;margin:0 1rem 1rem 0}.info-game__text[_ngcontent-%COMP%]{color:#fff;font-size:4rem}.information-game-container[_ngcontent-%COMP%]{background-color:#ffaf00;width:100%;display:flex;justify-content:center;height:4rem;align-items:center}.spinner__container[_ngcontent-%COMP%]{position:relative;display:flex;justify-content:center;height:47%;width:100%;max-height:484px}.awards-container[_ngcontent-%COMP%]{position:absolute;top:80px;height:338px;left:calc(50% - 374px);display:flex;justify-content:center;align-items:center;gap:6.5rem;z-index:4;overflow:hidden}.awards-column[_ngcontent-%COMP%]{display:flex;flex-direction:column;gap:110px;height:160px;animation-duration:4s;animation-name:slidevertical;animation-iteration-count:infinite}@keyframes slidevertical{}.award-image-container[_ngcontent-%COMP%]{min-height:160px;width:187px}.award-box-container[_ngcontent-%COMP%]{position:relative;width:100%;height:100%;max-width:1309px}.winner-container[_ngcontent-%COMP%]{position:absolute;z-index:5;top:-240px;width:950px;height:900px}.container_play-btn[_ngcontent-%COMP%]{z-index:6}p[_ngcontent-%COMP%], figure[_ngcontent-%COMP%]{margin:0}img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),n})(),canActivate:[Z],data:{Validate_game:"juego_play"}}];let pt=(()=>{class n{}return n.\u0275fac=function(e){return new(e||n)},n.\u0275mod=t.oAB({type:n}),n.\u0275inj=t.cJS({imports:[h.Bz.forChild(dt),h.Bz]}),n})();var ht=c(5906);let _t=(()=>{class n{}return n.\u0275fac=function(e){return new(e||n)},n.\u0275mod=t.oAB({type:n}),n.\u0275inj=t.cJS({imports:[d.ez,pt,ht.m,v.JF,y.u5]}),n})()}}]);