"use strict";(self.webpackChunkFrontend_Juegos_2022=self.webpackChunkFrontend_Juegos_2022||[]).push([[918],{8041:(h,l,i)=>{i.d(l,{r:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getAwardConditionFilter(t){return this.http.get(this.url+"api/awardconditionfilter/"+t)}getAward(){return this.http.get(this.url+"api/awardfilter/?is_active=true")}getAwardConditionbyId(t){return this.http.get(this.url+"api/awardcondition/"+t+"/")}postAwardCondition(t){return this.http.post(this.url+"api/awardcondition/",t)}putAwardCondition(t,o){return this.http.put(this.url+"api/awardcondition/"+t+"/",o)}deleteAwardCondition(t){return this.http.delete(this.url+"api/awardcondition/"+t+"/")}getAwardEdit(){return this.http.get(this.url+"api/awardlist/")}changeState(t,o){return this.http.post(this.url+"api/awardcondition/"+t+"/change_state/",o)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},1131:(h,l,i)=>{i.d(l,{q:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getAward(){return this.http.get(this.url+"api/awardlist/")}getAwardbyId(t){return this.http.get(this.url+"api/award/"+t+"/")}getAwardbyIdVisualizer(t){return this.http.get(this.url+"api/awardlist/"+t+"/")}postAward(t){return this.http.post(this.url+"api/award/",t)}putAward(t,o){return this.http.put(this.url+"api/award/"+t+"/",o)}deleteAward(t){return this.http.delete(this.url+"api/award/"+t+"/")}getFilterAward(t){return this.http.get(this.url+"api/awardfilter/"+t)}winAward(t,o){return this.http.post(this.url+"api/award/"+t+"/won_award/",o)}winAwardCondition(t,o){return this.http.post(this.url+"api/award/"+t+"/won_award_condition/",o)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},990:(h,l,i)=>{i.d(l,{D:()=>o});var n=i(5412),r=i(4650),a=i(4859);let s=(()=>{class _{constructor(u,d){this.data=u,this.mdDialogRef=d}ngOnInit(){}cancel(){this.close(!1)}close(u){this.mdDialogRef.close(u)}confirm(){this.close(!0)}onEsc(){this.close(!1)}}return _.\u0275fac=function(u){return new(u||_)(r.Y36(n.WI),r.Y36(n.so))},_.\u0275cmp=r.Xpm({type:_,selectors:[["app-confirm-dialog"]],hostBindings:function(u,d){1&u&&r.NdJ("keydown.esc",function(){return d.onEsc()})},decls:12,vars:4,consts:[[1,"container_dialog"],[1,"header"],["mat-dialog-title",""],["mat-dialog-content",""],[1,"dialog-message"],["mat-dialog-actions",""],["mat-button","",3,"click"]],template:function(u,d){1&u&&(r.TgZ(0,"div",0)(1,"div",1)(2,"h1",2),r._uU(3),r.qZA()(),r.TgZ(4,"div",3)(5,"p",4),r._uU(6),r.qZA()(),r.TgZ(7,"div",5)(8,"button",6),r.NdJ("click",function(){return d.cancel()}),r._uU(9),r.qZA(),r.TgZ(10,"button",6),r.NdJ("click",function(){return d.confirm()}),r._uU(11),r.qZA()()()),2&u&&(r.xp6(3),r.Oqu(d.data.title),r.xp6(3),r.Oqu(d.data.message),r.xp6(3),r.Oqu(d.data.cancelText),r.xp6(2),r.Oqu(d.data.confirmText))},dependencies:[a.lW,n.uh,n.xY,n.H8],styles:["header[_ngcontent-%COMP%], .dialog-message[_ngcontent-%COMP%]{text-transform:lowercase;text-align:center}.header[_ngcontent-%COMP%]:first-letter, .dialog-message[_ngcontent-%COMP%]:first-letter{text-transform:uppercase}.container_dialog[_ngcontent-%COMP%]{display:flex;flex-direction:column;justify-content:center;align-items:center;width:500px}h1[_ngcontent-%COMP%], p[_ngcontent-%COMP%]{color:#fff;text-align:center}button[_ngcontent-%COMP%]{background:#3f3f43;color:#fff}button[_ngcontent-%COMP%]:hover{background:#00ffc5;color:#002130}"]}),_})();var e=i(5698),c=i(4004),t=i(5659);let o=(()=>{class _{constructor(u){this.dialog=u}open(u){this.dialogRef=this.dialog.open(s,{data:{title:u.title,message:u.message,cancelText:u.cancelText,confirmText:u.confirmText}})}confirmed(){return this.dialogRef.afterClosed().pipe((0,e.q)(1),(0,c.U)(u=>u))}error(u){let d=[];for(let m in u)d.push(u[m]);this.dialog.open(t.o,{data:d})}}return _.\u0275fac=function(u){return new(u||_)(r.LFG(n.uw))},_.\u0275prov=r.Yz7({token:_,factory:_.\u0275fac,providedIn:"root"}),_})()},3867:(h,l,i)=>{i.d(l,{V:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}postGameDate(t){return this.http.post(this.url+"api/gamedate/",t)}DateFormat(t){let o=t.getTime(),_="";if(t.getTimezoneOffset()<=0){let p=o+Math.abs(6e4*t.getTimezoneOffset());_=new Date(p).toISOString()}else{let p=o+-Math.abs(6e4*t.getTimezoneOffset());_=new Date(p).toISOString()}return _.split(".")[0]}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},3021:(h,l,i)=>{i.d(l,{h:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}postGame(t){return this.http.post(`${this.url}/game`,t)}getAll(){return this.http.get(this.url+"api/game/")}getById(t){return this.http.get(this.url+"api/game/"+t+"/")}put(t,o){return this.http.put(this.url+"api/game/"+t+"/",o)}putGame(t,o){return this.http.put(this.url+"api/game/"+t+"/",o)}getPublicityGame(){return this.http.get(this.url+"api/Publicity_game/")}getDesign(){return this.http.get(this.url+"api/design/")}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},9760:(h,l,i)=>{i.d(l,{Q:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}postMatch(t){return this.http.post(this.url+"api/match/",t).subscribe(o=>{console.log("data")})}getMatchFilter(t){return this.http.get(this.url+"api/matchfilter/"+t)}getAllMatch(){return this.http.get(this.url+"api/match/")}getMatchFilterClientHistory(t){return this.http.get(this.url+"api/matchfilterhistory/"+t)}changeDelivered(t,o){return this.http.post(this.url+"api/match/"+t+"/award_delivered/",o)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},3398:(h,l,i)=>{i.d(l,{g:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getAwardsListGame(){return this.http.get(this.url+"api/awardGame/")}getProbabilites(){return this.http.get(this.url+"api/probabilidad/1")}postItemToCategory(t){return this.http.post(this.url+"api/awardGame/",t)}putProbabilityConfig(t){return this.http.put(this.url+"api/probabilidad/1/",t)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},9661:(h,l,i)=>{i.d(l,{D:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getAllPublicityGame(){return this.http.get(this.url+"api/Publicity_game/")}getPublicityGame(t){return this.http.get(this.url+"api/Publicity_game/"+t+"/")}updatePublicityGame(t,o){return this.http.put(this.url+"api/Publicity_game/"+t+"/",o)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},3276:(h,l,i)=>{i.d(l,{E:()=>r});var n=i(4650);let r=(()=>{class a{constructor(){this.topPublicityList=[],this.bottomPublicityList=[],this.secondsShowTopPublicity=3,this.secondsShowBottomPublicity=3,this.previewTopImage="",this.previewBottomImage=""}loadTopData(e){this.topPublicityList=e}loadBottomData(e){this.bottomPublicityList=e}getTopPublicityList(){return this.topPublicityList}getBottomPublicityList(){return this.bottomPublicityList}getTopImageFileToUpload(){return this.topImageFileToUpload}getBottomImageFileToUpload(){return this.bottomImageFileToUpload}setTopImageFileToUpload(e){this.topImageFileToUpload=e}setBottomImageFileToUpload(e){this.bottomImageFileToUpload=e}setPreviewTopImage(e){this.previewTopImage=e}setPreviewBottomImage(e){this.previewBottomImage=e}setSecondsShowTop(e){this.secondsShowTopPublicity=e}setSecondsShowBottom(e){this.secondsShowBottomPublicity=e}}return a.\u0275fac=function(e){return new(e||a)},a.\u0275prov=n.Yz7({token:a,factory:a.\u0275fac,providedIn:"root"}),a})()},7637:(h,l,i)=>{i.d(l,{U:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getPublicityTopList(){return this.http.get(this.url+"api/Publicity_top/")}getPublicityBottomList(){return this.http.get(this.url+"api/Publicity_bottom/")}postTopPublicity(t){return this.http.post(this.url+"api/Publicity_top/",t)}postBottomPublicity(t){return this.http.post(this.url+"api/Publicity_bottom/",t)}deleteTopPublicity(t){return this.http.delete(this.url+"api/Publicity_top/"+t+"/")}deleteBottomPublicity(t){return this.http.delete(this.url+"api/Publicity_bottom/"+t+"/")}getPublicityConfigTop(){return this.http.get(this.url+"api/publicity/1/")}updatePublicityConfigTop(t,o){return this.http.put(this.url+"api/publicity/1/",o)}getPublicityConfigBottom(){return this.http.get(this.url+"api/publicity/2/")}updatePublicityConfigBottom(t){return this.http.put(this.url+"api/publicity/2/",t)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},4870:(h,l,i)=>{i.d(l,{T:()=>r});var n=i(4650);let r=(()=>{class a{constructor(){this.previewFontLetter="",this.style={id:1,game_id:1,color_text:"",font_letter:"",image_machine_game:"",image_background_game:"",image_logo_game:"../../../assets/img/logoejemplo.png",color_background_game:"",video_screensaver:"",video_autoplay:!0,video_loop:!0,title_button_screensaver:"",scan_code_title:"",scan_code_description:"",title_winner:"",description_winner:"",image_winner:"",date_created:new Date,date_modified:new Date,is_active:!0}}loadData(e){this.style=e}getTitleButtonScreensaver(){return this.style.title_button_screensaver}getLogoUrl(){return null!=this.style.image_logo_game?this.style.image_logo_game:""}getStyles(){return this.style}getImageBackgroundGameFile(){return this.imageBackgroundGameFile}setImageBackgroundGameFile(e){this.imageBackgroundGameFile=e}getImageWinnerGameFile(){return this.imageWinnerGameFile}setImageWinnerGameFile(e){this.imageWinnerGameFile=e}getImageLogoFile(){return this.imageLogoGameFile}setImageLogoFile(e){this.imageLogoGameFile=e}getVideoScreensaverFile(){return this.videoScreensaverFile}setVideoScreensaverFile(e){this.videoScreensaverFile=e}getImageMachineGameFile(){return this.imageMachineGameFile}setImageMchineGameFile(e){this.imageMachineGameFile=e}getPreviewFontLetter(){return this.previewFontLetter}setPreviewFontLetter(e){this.previewFontLetter=e}get_video_screensaver(){return this.style.video_screensaver}set_video_screensaver(e){this.style.video_screensaver=e}get_title_button_screensaver(){return this.style.title_button_screensaver}set_title_button_screensaver(e){this.style.title_button_screensaver=e}get_image_background_game(){return this.style.image_background_game}get_image_logo_game(){return null!=this.style.image_logo_game?this.style.image_logo_game:""}get_color_background_game(){return this.style.color_background_game}set_color_background_game(e){this.style.color_background_game=e}get_color_text(){return this.style.color_text}set_color_text(e){this.style.color_text=e}get_title_winner(){return this.style.title_winner}set_title_winner(e){this.style.title_winner=e}get_scan_code_title(){return this.style.scan_code_title}set_scan_code_title(e){this.style.scan_code_title=e}get_scan_code_description(){return this.style.scan_code_description}set_scan_code_description(e){this.style.scan_code_description=e}get_description_winner(){return this.style.description_winner}get_image_machine_game(){return this.style.image_machine_game}set_description_winner(e){this.style.description_winner=e}get_date_created(){return this.style.date_created}get_image_winner(){return this.style.image_winner}get_font_letter(){return this.style.font_letter}set_modified_date(e){this.style.date_modified=e}get_is_active(){return this.style.is_active}}return a.\u0275fac=function(e){return new(e||a)},a.\u0275prov=n.Yz7({token:a,factory:a.\u0275fac,providedIn:"root"}),a})()},2990:(h,l,i)=>{i.d(l,{f:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getDesignInformation(){return this.http.get(`${this.url}api/design/`)}updateDesgin(t,o){return this.http.put(this.url+"api/design/"+t+"/",o).subscribe(_=>{console.log("data")})}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},1172:(h,l,i)=>{i.d(l,{w:()=>s});var n=i(4650),r=i(529),a=i(9406);let s=(()=>{class e{constructor(t,o){this.http=t,this.puente=o,this.url=this.puente.geturl()}getAll(){return this.http.get(this.url+"api/ticket/")}getById(t){return this.http.get(this.url+"api/ticket/"+t+"/")}getByIdQrNumber(t){return this.http.get(this.url+"api/ticket/"+t+"/")}post(t){return this.http.post(this.url+"api/ticket/",t)}put(t,o){return this.http.put(this.url+"api/ticket/"+t+"/",o)}delete(t){return this.http.delete(this.url+"api/ticket/"+t+"/")}getFilter(t){return this.http.get(this.url+"api/ticketfilter/"+t)}changeStateTicket(t,o){return this.http.post(this.url+"api/ticket/"+t+"/change_state/",o)}}return e.\u0275fac=function(t){return new(t||e)(n.LFG(r.eN),n.LFG(a.Q))},e.\u0275prov=n.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e})()},9808:(h,l,i)=>{i.d(l,{n:()=>r});var n=i(6805);function r(a,s){const e="object"==typeof s;return new Promise((c,t)=>{let _,o=!1;a.subscribe({next:p=>{_=p,o=!0},error:t,complete:()=>{o?c(_):e?c(s.defaultValue):t(new n.K)}})})}}}]);