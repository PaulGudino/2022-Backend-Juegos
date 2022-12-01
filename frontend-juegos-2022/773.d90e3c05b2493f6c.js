"use strict";(self.webpackChunkFrontend_Juegos_2022=self.webpackChunkFrontend_Juegos_2022||[]).push([[773],{2773:(B,_,a)=>{a.r(_),a.d(_,{JuegoModule:()=>V});var l=a(6895),s=a(1390),t=a(4650);let g=(()=>{class e{constructor(){this.listPublicity=[],this.top_publicity="",this.bottom_publicity=""}loadData(n){this.listPublicity=n,this.top_publicity=this.listPublicity[0].image,this.bottom_publicity=this.listPublicity[1].image}getTopPublicity(){return this.top_publicity}getBottomPublicity(){return this.bottom_publicity}}return e.\u0275fac=function(n){return new(n||e)},e.\u0275prov=t.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})();var h=a(529),f=a(9406);let C=(()=>{class e{constructor(n,i){this.http=n,this.puente=i,this.url=this.puente.geturl()}getDesignInformation(){return this.http.get(`${this.url}api/design/`)}getPublicityList(){return this.http.get(`${this.url}api/publicity/`)}getThemeImages(){return this.http.get("https://juegos.pythonanywhere.com/api/imagenesjuegos/")}}return e.\u0275fac=function(n){return new(n||e)(t.LFG(h.eN),t.LFG(f.Q))},e.\u0275prov=t.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})();var p=a(4870);let m=(()=>{class e{constructor(){this.title="Empezar",this.fontSize="1.6rem",this.styledPadding="1rem 1.5rem",this.color="white",this.color_background="red"}ngOnInit(){}}return e.\u0275fac=function(n){return new(n||e)},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-generic-button"]],inputs:{title:"title",fontSize:"fontSize",styledPadding:"styledPadding",color:"color",color_background:"color_background"},decls:2,vars:9,consts:[[1,"generic-btn"]],template:function(n,i){1&n&&(t.TgZ(0,"button",0),t._uU(1),t.qZA()),2&n&&(t.Udp("font-size",i.fontSize)("padding",i.styledPadding)("color",i.color)("background",i.color_background),t.xp6(1),t.hij(" ",i.title,"\n"))},styles:[".generic-btn[_ngcontent-%COMP%]{padding:1rem 1.5rem;font-size:1.2rem;margin:0;text-align:center;border-radius:15px;outline:none;border:none}"]}),e})(),d=(()=>{class e{constructor(){this.urlPublicity="../../../assets/publicity.png"}ngOnInit(){}}return e.\u0275fac=function(n){return new(n||e)},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-publicity"]],inputs:{urlPublicity:"urlPublicity"},decls:3,vars:1,consts:[[1,"container-fluid","publicity_container","p-0"],[1,"publicity_img-container"],["alt","publicity-img",1,"publicity_img",3,"src"]],template:function(n,i){1&n&&(t.TgZ(0,"div",0)(1,"figure",1),t._UZ(2,"img",2),t.qZA()()),2&n&&(t.xp6(2),t.Q6J("src",i.urlPublicity,t.LSH))},styles:[".publicity_container[_ngcontent-%COMP%]{background-color:#0ff;width:100%;height:15vh}.publicity_img-container[_ngcontent-%COMP%], img[_ngcontent-%COMP%]{padding:0;margin:0}.publicity_img-container[_ngcontent-%COMP%], .publicity_img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),e})(),Z=(()=>{class e{constructor(n,i,c){this.publicity=n,this.themeService=i,this.styles=c,this.backgroundImgUrl="",this.top_publicity="../../../assets/img/bannerpublicidad.png",this.bottom_publicity="../../../assets/img/bannerpublicidad.png",this.buttonTitle="",this.logoImage="",this.videoUrl=""}ngOnInit(){this.themeService.getPublicityList().subscribe(n=>{n.length>0&&(this.publicity.loadData(n),this.top_publicity=this.publicity.getTopPublicity(),this.bottom_publicity=this.publicity.getBottomPublicity()),this.themeService.getDesignInformation().subscribe(i=>{console.log(i),this.styles.loadData(i[0]),this.buttonTitle=this.styles.get_title_button_screensaver(),this.logoImage=this.styles.get_image_logo_game(),this.videoUrl=this.styles.get_video_screensaver()})})}}return e.\u0275fac=function(n){return new(n||e)(t.Y36(g),t.Y36(C),t.Y36(p.T))},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-juego"]],decls:6,vars:7,consts:[[3,"urlPublicity"],[1,"container-fluid","home_container","p-0","m-0"],["muted","true",1,"home-image_container",3,"autoplay","loop","src"],[1,"home-btn_container"],["routerLink","/juego/scan",1,"home_btn",3,"title","fontSize"]],template:function(n,i){1&n&&(t._UZ(0,"app-publicity",0),t.TgZ(1,"div",1),t._UZ(2,"video",2),t.TgZ(3,"div",3),t._UZ(4,"app-generic-button",4),t.qZA()(),t._UZ(5,"app-publicity",0)),2&n&&(t.Q6J("urlPublicity",i.top_publicity),t.xp6(2),t.Q6J("autoplay",!0)("loop",!0)("src",i.videoUrl,t.LSH),t.xp6(2),t.Q6J("title",i.buttonTitle)("fontSize","1.2rem"),t.xp6(1),t.Q6J("urlPublicity",i.bottom_publicity))},dependencies:[s.rH,m,d],styles:[".home_container[_ngcontent-%COMP%]{position:relative;width:100%;height:70vh}.home-image_container[_ngcontent-%COMP%]{position:relative;height:100%;width:100%;background-color:#3b3b3b}.home-logo__container[_ngcontent-%COMP%]{position:absolute;min-width:20rem;height:15rem;left:calc(50% - 203px);z-index:2}img[_ngcontent-%COMP%]{width:100%;height:100%}.home_background[_ngcontent-%COMP%]{width:100%;height:100%;max-height:77.1rem}.home-shadow[_ngcontent-%COMP%]{background:#000000a1;height:100%;width:100%;position:absolute;top:0}.home-btn_container[_ngcontent-%COMP%]{max-width:14rem;position:absolute;bottom:calc(10% + 10px);left:calc(50% - 90px)}"]}),e})(),b=(()=>{class e{constructor(){this.code="Ingresa tu codigo aqui..."}getCode(){return this.code}setCode(n){this.code=n}}return e.\u0275fac=function(n){return new(n||e)},e.\u0275prov=t.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})();var u=a(4006);let v=(()=>{class e{constructor(n){this.KeyControllerService=n}ngOnInit(){}getButtonValue(n){let i=n.target;i.textContent&&this.KeyControllerService.setCode(this.KeyControllerService.getCode()+i.textContent),console.log(i.textContent)}}return e.\u0275fac=function(n){return new(n||e)(t.Y36(b))},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-keyboard"]],decls:26,vars:0,consts:[[1,"container-fluid","text-center"],[1,"keyboard-container"],[1,"row","keyboard-row"],[1,"col","btn",3,"click"],[1,"rowkeyboard-row"],[1,"col-12","btn",3,"click"]],template:function(n,i){1&n&&(t.TgZ(0,"div",0)(1,"div",1)(2,"div",2)(3,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(4,"1"),t.qZA(),t.TgZ(5,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(6,"2"),t.qZA(),t.TgZ(7,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(8,"3"),t.qZA()(),t.TgZ(9,"div",2)(10,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(11,"4"),t.qZA(),t.TgZ(12,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(13,"5"),t.qZA(),t.TgZ(14,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(15,"6"),t.qZA()(),t.TgZ(16,"div",2)(17,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(18,"7"),t.qZA(),t.TgZ(19,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(20,"8"),t.qZA(),t.TgZ(21,"button",3),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(22,"9"),t.qZA()(),t.TgZ(23,"div",4)(24,"button",5),t.NdJ("click",function(r){return i.getButtonValue(r)}),t._uU(25,"0"),t.qZA()()()())},styles:[".btn[_ngcontent-%COMP%]{background-color:gray;border-radius:15px;padding:.3rem .4rem}.keyboard-container[_ngcontent-%COMP%]{display:flex;flex-direction:column;gap:.8rem;width:11rem}.keyboard-row[_ngcontent-%COMP%]{gap:.5rem}"]}),e})();const P=function(e,o,n){return{"home-logo__container":e,logo__container:o,"logo__container-background":n}};let y=(()=>{class e{constructor(){this.height="15rem",this.isHome=!0,this.isBackground=!1,this.urlImage=""}ngOnInit(){}}return e.\u0275fac=function(n){return new(n||e)},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-logo"]],inputs:{height:"height",isHome:"isHome",isBackground:"isBackground",urlImage:"urlImage"},decls:2,vars:8,consts:[[1,"p-0","m-0",3,"ngClass"],["alt","home-logo",1,"p-0","m-0",3,"src"]],template:function(n,i){1&n&&(t.TgZ(0,"figure",0),t._UZ(1,"img",1),t.qZA()),2&n&&(t.Udp("height",i.height),t.Q6J("ngClass",t.kEZ(4,P,i.isHome,!i.isHome,i.isBackground)),t.xp6(1),t.Q6J("src",i.urlImage,t.LSH))},dependencies:[l.mk],styles:[".home-logo__container[_ngcontent-%COMP%]{position:absolute;max-width:426px;height:15rem;left:calc(50% - 205px);top:calc(0% + 20px);z-index:2}.logo__container[_ngcontent-%COMP%]{position:absolute;height:15rem;top:2px;z-index:2}.logo__container-background[_ngcontent-%COMP%]{position:absolute;height:15rem;top:calc(0% + 20px);left:calc(50% - 210px);z-index:2}img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),e})();function T(e,o){if(1&e&&(t.TgZ(0,"div",14)(1,"h2",15),t._uU(2),t.qZA(),t.TgZ(3,"p",16),t._uU(4),t.qZA()()),2&e){const n=t.oxw();t.xp6(2),t.Oqu(n.styles.get_scan_code_title()),t.xp6(2),t.hij(" ",n.styles.get_scan_code_description()," ")}}function w(e,o){1&e&&(t.TgZ(0,"div",14)(1,"h2",15),t._uU(2,"Ingrese el codigo"),t.qZA()())}function k(e,o){1&e&&(t.TgZ(0,"figure",17),t._UZ(1,"img",18),t.qZA())}function x(e,o){1&e&&t._UZ(0,"app-keyboard")}let M=(()=>{class e{constructor(n,i,c,r){this.router=n,this.publicity=i,this.styles=c,this.keyController=r,this.selectedInputCode=!1,this.scanState=!0,this.explication="Puedes escanear el codigo QR de tu ticket",this.code=this.keyController.getCode()}ngOnInit(){}changeView(){this.scanState=!1,this.keyController.setCode("")}continueToGame(){this.router.navigate(["/juego/play"])}}return e.\u0275fac=function(n){return new(n||e)(t.Y36(s.F0),t.Y36(g),t.Y36(p.T),t.Y36(b))},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-scan-view"]],decls:16,vars:10,consts:[[1,"scan_container","p-0","m-0"],[3,"urlPublicity"],[1,"container-menu"],["height","12rem",3,"isBackground"],[1,"scan-shadow"],[1,"scan_menu-container"],[1,"menu-container_img-container"],["height","6rem",3,"urlImage","isHome"],["class","menu-info",4,"ngIf"],["class","menu-container_scan-img-container",4,"ngIf"],[4,"ngIf"],["type","text",1,"btn","menu__input",3,"ngModel","click","ngModelChange"],["codeInput","ngModel"],["title","Continuar","fontSize","1rem","styledPadding","0.5rem 2rem",1,"mb-2",3,"click"],[1,"menu-info"],[1,"scan_title"],[1,"explication-text"],[1,"menu-container_scan-img-container"],["src","../../../assets/img/codigoQR.png","alt","scan-logo",1,"menu-container_scan-img"]],template:function(n,i){1&n&&(t.TgZ(0,"div",0),t._UZ(1,"app-publicity",1),t.TgZ(2,"div",2),t._UZ(3,"app-logo",3)(4,"div",4),t.TgZ(5,"div",5)(6,"div",6),t._UZ(7,"app-logo",7),t.qZA(),t.YNc(8,T,5,2,"div",8),t.YNc(9,w,3,0,"div",8),t.YNc(10,k,2,0,"figure",9),t.YNc(11,x,1,0,"app-keyboard",10),t.TgZ(12,"input",11,12),t.NdJ("click",function(){return i.changeView()})("ngModelChange",function(r){return i.keyController.code=r}),t.qZA(),t.TgZ(14,"app-generic-button",13),t.NdJ("click",function(){return i.continueToGame()}),t.qZA()()(),t._UZ(15,"app-publicity",1),t.qZA()),2&n&&(t.xp6(1),t.Q6J("urlPublicity",i.publicity.getTopPublicity()),t.xp6(2),t.Q6J("isBackground",!0),t.xp6(4),t.Q6J("urlImage",i.styles.get_image_logo_game())("isHome",!1),t.xp6(1),t.Q6J("ngIf",i.scanState),t.xp6(1),t.Q6J("ngIf",!i.scanState),t.xp6(1),t.Q6J("ngIf",i.scanState),t.xp6(1),t.Q6J("ngIf",!i.scanState),t.xp6(1),t.Q6J("ngModel",i.keyController.code),t.xp6(3),t.Q6J("urlPublicity",i.publicity.getBottomPublicity()))},dependencies:[l.O5,u.Fj,u.JJ,u.On,m,v,d,y],styles:[".scan_container[_ngcontent-%COMP%]{position:relative;background-color:gray;width:100%}.container-menu[_ngcontent-%COMP%]{position:relative;height:71%;width:100%;background-color:#000}.scan-shadow[_ngcontent-%COMP%]{height:71%;width:100%;position:absolute;background-color:#000000d4;z-index:2}.scan_menu-container[_ngcontent-%COMP%]{position:relative;height:70vh;width:100%;display:flex;flex-direction:column;align-items:center;gap:1rem;z-index:3}.scan_title[_ngcontent-%COMP%]{margin:0}.menu-container_img-container[_ngcontent-%COMP%]{width:10rem;max-width:10rem;min-height:4rem;margin:0 1rem 1rem 0}.menu-info[_ngcontent-%COMP%]{display:flex;flex-direction:column;align-items:center;color:#fff}.menu-container_img[_ngcontent-%COMP%]{border-radius:25px}.explication-text[_ngcontent-%COMP%]{padding:0 2rem}.menu-container_scan-img-container[_ngcontent-%COMP%]{min-height:7rem;width:7rem}.menu__input[_ngcontent-%COMP%]{border:3px solid red;outline:none;border-radius:13px;background-color:#000;color:#fff;padding:.2rem .5rem}p[_ngcontent-%COMP%], figure[_ngcontent-%COMP%]{margin:0}img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),e})();var O=a(3398);function U(e,o){1&e&&(t.TgZ(0,"p",8),t._uU(1," No te quedan m\xe1s Giros! "),t.qZA())}function J(e,o){1&e&&(t.TgZ(0,"p",8),t._uU(1," Disponible 1 Giro m\xe1s! "),t.qZA())}function S(e,o){if(1&e&&(t.TgZ(0,"p",8),t._uU(1),t.qZA()),2&e){const n=t.oxw();t.xp6(1),t.hij(" Disponible ",n.availableSpin," Giros m\xe1s! ")}}const A=[{path:"",component:Z},{path:"scan",component:M},{path:"play",component:(()=>{class e{constructor(n,i,c){this.publicity=n,this.styles=i,this.probabilityService=c,this.informationText="A JUGAR!",this.availableSpin=0,this.informationTextGame=`Disponnible ${this.availableSpin} Giro mas`,this.top_publicity=this.publicity.getTopPublicity(),this.bottom_publicity=this.publicity.getTopPublicity(),this.probability={}}ngOnInit(){this.probabilityService.getProbabilites().subscribe(n=>{console.log(n),this.probability=n[n.length-1],this.availableSpin=this.probability.attempts_limit})}}return e.\u0275fac=function(n){return new(n||e)(t.Y36(g),t.Y36(p.T),t.Y36(O.g))},e.\u0275cmp=t.Xpm({type:e,selectors:[["app-play-view"]],decls:51,vars:9,consts:[[1,"container-fullscreen","p-0","m-0"],[3,"urlPublicity"],[1,"container-menu"],["height","12rem",3,"urlImage","isBackground"],[1,"scan-shadow"],[1,"scan_menu-container"],[1,"menu-container_img-container"],["height","6rem",3,"urlImage","isHome"],[1,"info-game__text"],[1,"information-game-container",3,"ngPlural"],["ngPluralCase","=0"],["class","info-game__text","ngPluralCase","=1"],["class","info-game__text","ngPluralCase","other"],[1,"spinner__container"],[1,"award-box-container"],["alt","cajon-premios",1,"awards-box",3,"src"],[1,"awards-container"],[1,"awards-column"],[1,"award-image-container"],["src","../../../../../assets/img/logoejemplo.png","alt",""],["title","Girar","fontSize","1rem","styledPadding","0.5rem 2rem",1,"mb-2"]],template:function(n,i){1&n&&(t.TgZ(0,"div",0),t._UZ(1,"app-publicity",1),t.TgZ(2,"div",2),t._UZ(3,"app-logo",3)(4,"div",4),t.TgZ(5,"div",5)(6,"div",6),t._UZ(7,"app-logo",7),t.qZA(),t.TgZ(8,"p",8),t._uU(9),t.qZA(),t.TgZ(10,"div",9),t.YNc(11,U,2,0,"ng-template",10),t.YNc(12,J,2,0,"ng-template",11),t.YNc(13,S,2,1,"ng-template",12),t.qZA(),t.TgZ(14,"div",13)(15,"figure",14),t._UZ(16,"img",15),t.qZA(),t.TgZ(17,"div",16)(18,"div",17)(19,"figure",18),t._UZ(20,"img",19),t.qZA(),t.TgZ(21,"figure",18),t._UZ(22,"img",19),t.qZA(),t.TgZ(23,"figure",18),t._UZ(24,"img",19),t.qZA(),t.TgZ(25,"figure",18),t._UZ(26,"img",19),t.qZA(),t.TgZ(27,"figure",18),t._UZ(28,"img",19),t.qZA(),t.TgZ(29,"figure",18),t._UZ(30,"img",19),t.qZA(),t.TgZ(31,"figure",18),t._UZ(32,"img",19),t.qZA(),t.TgZ(33,"figure",18),t._UZ(34,"img",19),t.qZA(),t.TgZ(35,"figure",18),t._UZ(36,"img",19),t.qZA(),t.TgZ(37,"figure",18),t._UZ(38,"img",19),t.qZA()(),t.TgZ(39,"div",17)(40,"figure",18),t._UZ(41,"img",19),t.qZA(),t.TgZ(42,"figure",18),t._UZ(43,"img",19),t.qZA()(),t.TgZ(44,"div",17)(45,"figure",18),t._UZ(46,"img",19),t.qZA(),t.TgZ(47,"figure",18),t._UZ(48,"img",19),t.qZA()()()(),t._UZ(49,"app-generic-button",20),t.qZA()(),t._UZ(50,"app-publicity",1),t.qZA()),2&n&&(t.xp6(1),t.Q6J("urlPublicity",i.publicity.getTopPublicity()),t.xp6(2),t.Q6J("urlImage",i.styles.get_image_logo_game())("isBackground",!0),t.xp6(4),t.Q6J("urlImage",i.styles.get_image_logo_game())("isHome",!1),t.xp6(2),t.Oqu(i.styles.get_title_winner()),t.xp6(1),t.Q6J("ngPlural",i.availableSpin),t.xp6(6),t.Q6J("src",i.styles.get_image_machine_game(),t.LSH),t.xp6(34),t.Q6J("urlPublicity",i.publicity.getTopPublicity()))},dependencies:[l.iq,l.zE,m,d,y],styles:[".scan_menu-container[_ngcontent-%COMP%]{position:relative;height:100%;width:100%;display:flex;flex-direction:column;align-items:center;gap:.5rem;z-index:3}.container-menu[_ngcontent-%COMP%]{position:relative;height:70vh;width:100%;background-color:#000}.scan-shadow[_ngcontent-%COMP%]{height:70vh;width:100%;position:absolute;background-color:#000000d4;z-index:2}.menu-container_img-container[_ngcontent-%COMP%]{width:10rem;max-width:10rem;min-height:4rem;margin:0 1rem 1rem 0}.info-game__text[_ngcontent-%COMP%]{color:#fff;font-size:1.2rem}.information-game-container[_ngcontent-%COMP%]{background-color:#ffaf00;width:100%;display:flex;justify-content:center;height:2rem;align-items:center}.spinner__container[_ngcontent-%COMP%]{position:relative;display:flex;justify-content:center;height:47%;width:100%;max-height:202px}.awards-container[_ngcontent-%COMP%]{position:absolute;top:66px;left:calc(50% - 272px);display:flex;justify-content:center;gap:4rem;z-index:4;overflow:hidden}.awards-column[_ngcontent-%COMP%]{display:flex;flex-direction:column;gap:1rem;height:6rem;animation-duration:4s;animation-name:slidevertical;animation-iteration-count:infinite}@keyframes slidevertical{}.award-image-container[_ngcontent-%COMP%]{height:9rem;width:9rem}.award-box-container[_ngcontent-%COMP%]{position:relative;width:100%;height:100%;max-width:766px}p[_ngcontent-%COMP%]{margin:0}img[_ngcontent-%COMP%]{width:100%;height:100%}"]}),e})()}];let q=(()=>{class e{}return e.\u0275fac=function(n){return new(n||e)},e.\u0275mod=t.oAB({type:e}),e.\u0275inj=t.cJS({imports:[s.Bz.forChild(A),s.Bz]}),e})();var I=a(3832);let V=(()=>{class e{}return e.\u0275fac=function(n){return new(n||e)},e.\u0275mod=t.oAB({type:e}),e.\u0275inj=t.cJS({imports:[l.ez,q,I.m,h.JF,u.u5]}),e})()}}]);