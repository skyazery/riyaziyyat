const SECTIONS=BOOK.sections;
const ICON=BOOK.icons;
const TP=n=>D&&D.topics[n-BOOK.first];
const app=document.getElementById('app'),bar=document.getElementById('bar'),barIn=document.getElementById('barIn');
let D=null,AUD={};
const KEY=BOOK.key;
let P=load(); function load(){try{return JSON.parse(localStorage.getItem(KEY))||{sound:true,t:{}}}catch(e){return{sound:true,t:{}}}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(P))}catch(e){}}
function h(tag,attrs={},...kids){const e=document.createElement(tag);for(const[k,v]of Object.entries(attrs)){if(k==='class')e.className=v;else if(k.startsWith('on'))e.addEventListener(k.slice(2),v);else if(v!==false&&v!=null)e.setAttribute(k,v===true?'':v)}for(const k of kids.flat()){if(k==null||k===false)continue;e.append(k.nodeType?k:document.createTextNode(k))}return e}

/* sound */
let player=null,foxEl=null,vEl=null;
function talking(on){if(foxEl)foxEl.classList.toggle('talk',on);if(vEl){vEl.classList.toggle('stop',on);vEl.textContent=on?'⏸ Dayandır':'🔊 Dinlə'}}
function audioUrl(id){return AUD[id]?'audio/'+id+'.mp3':null}
function play(id){const u=audioUrl(id);if(!u)return;try{stop();player=new Audio(u);player.onended=player.onpause=()=>talking(false);talking(true);const p=player.play();if(p&&p.catch)p.catch(()=>talking(false))}catch(e){}}
/* tərif səsi: cavab yoxlananda (səhifə yenidən çəkiləndən sonra) oxunur */
let PRAISE=null;
function praise(ok){PRAISE=ok}
function playPraise(){if(PRAISE===null||!P.sound){PRAISE=null;return}const f=PRAISE?'p_ok'+(1+Math.random()*4|0):'p_no'+(1+Math.random()*2|0);PRAISE=null;setTimeout(()=>{try{stop();player=new Audio((BOOK.praise||'audio/')+f+'.mp3');player.play().catch(()=>{})}catch(e){}},450)}
function stop(){try{if(player){player.onpause=null;player.pause()}}catch(e){}talking(false)}
let ac=null;function chime(ok){try{ac=ac||new(window.AudioContext||window.webkitAudioContext)();const t=ac.currentTime;(ok?[523,659,784]:[392,330]).forEach((f,k)=>{const o=ac.createOscillator(),g=ac.createGain();o.type='triangle';o.frequency.value=f;g.gain.setValueAtTime(.0001,t+k*.12);g.gain.exponentialRampToValueAtTime(.18,t+k*.12+.02);g.gain.exponentialRampToValueAtTime(.0001,t+k*.12+.3);o.connect(g).connect(ac.destination);o.start(t+k*.12);o.stop(t+k*.12+.32)})}catch(e){}}
function confetti(){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const c=document.getElementById('cf'),x=c.getContext('2d');c.width=innerWidth;c.height=innerHeight;const cols=['#F6C343','#5145E6','#38C172','#E35D7F','#3BA6F5'];const Q=Array.from({length:60},()=>({x:innerWidth/2+(Math.random()-.5)*120,y:innerHeight*.45,vx:(Math.random()-.5)*9,vy:-Math.random()*11-4,s:6+Math.random()*6,c:cols[Math.random()*5|0],r:Math.random()*6}));let n=0;(function f(){x.clearRect(0,0,c.width,c.height);Q.forEach(p=>{p.vy+=.35;p.x+=p.vx;p.y+=p.vy;p.r+=.2;x.save();x.translate(p.x,p.y);x.rotate(p.r);x.fillStyle=p.c;x.fillRect(-p.s/2,-p.s/2,p.s,p.s*.6);x.restore()});if(++n<70)requestAnimationFrame(f);else x.clearRect(0,0,c.width,c.height)})()}

function brand(stars){return h('div',{class:'card hdr bk bk-'+BOOK.id},h('div',{class:'part','aria-hidden':'true'},h('b',{},BOOK.part),h('span',{},'hissə')),h('div',{class:'brand'},h('b',{},BOOK.title),h('i',{},BOOK.partName),h('span',{},BOOK.sub)),stars!=null?h('span',{class:'pill star'},'⭐ '+stars):null)}
const totalStars=()=>Object.values(P.t).reduce((s,v)=>s+(v.stars||0),0);

/* ---------- home ---------- */
function home(){
  app.append(brand(totalStars()));
  if(SAGIRD&&SAGIRD.name)app.append(h('div',{class:'card hello'},'👋 Salam, '+SAGIRD.name+'!'));
  app.append(levelCard());
  const s=lvStart();
  SECTIONS.forEach(([name,a,b],si)=>{
    app.append(h('p',{class:'sec-title'},(si+1)+'. '+name));
    const g=h('div',{class:'topics'});
    for(let n=a;n<=b;n++){const t=TP(n),pr=P.t[n],done=isDone(n),gt=gate(n);
      const pass=!done&&s!=null&&n<s, here=!done&&(KOD?gt==='new':s===n);
      if(gt==='tomorrow'||gt==='later'||gt==='level'){
        g.append(h('div',{class:'tcard lock'+(gt==='tomorrow'?' soon':''),'aria-disabled':'true'},h('span',{class:'num'},'🔒'),h('b',{},ICON[n]+' '+t.title),h('small',{},gt==='tomorrow'?'🌙 Sabah açılacaq':gt==='level'?'🧭 Əvvəl səviyyə testi':'Bağlıdır')));continue}
      g.append(h('a',{class:'tcard'+(done?' done':pass?' pass':here?' here':''),href:'#t'+n},h('span',{class:'num'},done||pass?'✓':String(n)),h('b',{},ICON[n]+' '+t.title),h('small',{},pr?('⭐ '+(pr.stars||0)+' / '+autoCount(t)):done?'✓ Bitib · təkrar et':pass?'Keçildi · təkrar et':here?(KOD?'👉 Bugünkü mövzu':'👉 Buradan başla'):'Başla →')))}
    app.append(g)});
  app.append(h('p',{class:'sec-title'},'🏆 Sonda'),testCard());
  if(BOOK.other)app.append(otherCard());
  app.append(h('footer',{},BOOK.footer));
}
function testCard(){
  if(!KOD)return h('div',{class:'testcard lock'},h('span',{class:'ic'},'🔒'),h('div',{},h('b',{},'Yoxlama testi'),h('span',{},'Test yalnız müəllimin göndərdiyi şəxsi linklə açılır.')));
  if(SAGIRD&&SAGIRD.done)return h('a',{class:'testcard done',href:'test.html?s='+KOD},h('span',{class:'ic'},'📋'),h('div',{},h('b',{},'Testin nəticəsi'),h('span',{},'Valideyn hesabatına bax')));
  return h('a',{class:'testcard',href:'test.html?s='+KOD},h('span',{class:'ic'},'🏆'),h('div',{},h('b',{},'Yoxlama testi'),h('span',{},'Bütün mövzulardan sonra · yalnız 1 dəfə · 20 tapşırıq')));
}
function otherCard(){const o=BOOK.other;return h('a',{class:'tcard other bk-'+o.id,href:o.href+(KOD?'?s='+KOD:'')},h('b',{},o.label),h('small',{},o.text))}
const autoCount=t=>t.problems.filter(p=>p.check||p.web).length;

/* ---------- səviyyə testi ----------
   Hər bölmədən (SECTIONS ilə eyni ardıcıllıq) 2 tapşırıq: [mövzu, tapşırığın sırası (0-dan)].
   Bölmənin hər 2 tapşırığı düzdürsə növbəti bölməyə keçir; səhv olan kimi test bitir
   və uşaq həmin bölmənin ilk mövzusundan başlayır. Hamısı düzdürsə start = 29. */
const LV_Q=BOOK.lvq;
const LV_ALL=BOOK.last+1;
let LVM=false,LT=null;
/* başlanğıc mövzu: şəxsi linki olanda müəllim cədvəli əsasdır (müəllim dəyişə bilər) */
function lvStart(){
  if(KOD&&SAGIRD&&SAGIRD.loaded){const L=SAGIRD.level;if(L&&L.done)return L.start;return P.lv&&!P.lv.sent?P.lv.start:null}
  return P.lv?P.lv.start:null;
}
function lvCanRetake(){return !KOD||!!(SAGIRD&&SAGIRD.level&&SAGIRD.level.retry)}

/* ---------- gündəlik limit ----------
   Yalnız şəxsi linklə: yeni mövzu gündə LIMIT dənə açılır (geri qalan uşaq gündə 2×LIMIT-ə qədər çata bilər).
   Bitmiş mövzular və səviyyə testinə görə keçilmiş mövzular həmişə açıqdır (təkrar).
   LIMIT müəllim cədvəlindən gəlir (Ayarlar → GUNDELIK_LIMIT, 0 = limitsiz). Gün Tbilisi vaxtı ilə dəyişir. */
const dayStr=()=>{try{return new Date().toLocaleDateString('en-CA',{timeZone:'Asia/Tbilisi'})}catch(e){const d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}};
const dKey=()=>'riyaziyyat-gundelik-'+KOD;
function dLocal(){try{return JSON.parse(localStorage.getItem(dKey()))||[]}catch(e){return[]}}
function dSaveLocal(a){try{localStorage.setItem(dKey(),JSON.stringify(a))}catch(e){}}
function dLimit(){const d=SAGIRD&&SAGIRD.daily;return d&&typeof d.limit==='number'?d.limit:1}
/* yeni bitirilmiş mövzular (bütün kitablar): serverdəki + hələ göndərilməyənlər */
function dNews(){
  const m=new Map(),add=(d,b,n)=>{const k=b+':'+n;if(!m.has(k))m.set(k,{d,b,n:+n})};
  ((SAGIRD&&SAGIRD.daily&&SAGIRD.daily.news)||[]).forEach(([d,b,n])=>add(d,b,n));
  dLocal().forEach(e=>add(e.d,e.b,e.n));
  return [...m.values()];
}
const dDiff=(a,b)=>Math.round((Date.parse(b)-Date.parse(a))/864e5);
/* bu gün neçə yeni mövzu açmaq olar */
function dLeft(){
  const L=dLimit();if(!L)return Infinity;
  const ns=dNews(),t=dayStr();if(!ns.length)return L;
  const first=ns.reduce((m,x)=>x.d<m?x.d:m,ns[0].d);
  const earned=(Math.max(0,dDiff(first,t))+1)*L;
  return Math.max(0,Math.min(2*L-ns.filter(x=>x.d===t).length,earned-ns.length));
}
const isDone=n=>!!(P.t[n]&&P.t[n].done)||(!!KOD&&dNews().some(x=>x.b===BOOK.id&&x.n===n));
function nextNew(){const s=lvStart();if(s==null)return null;for(let n=Math.max(s,BOOK.first);n<=BOOK.last;n++)if(!isDone(n))return n;return null}
/* open – açıq (təkrar), new – bugünkü yeni mövzu, tomorrow – sabah açılacaq, later – sonra, level – əvvəl səviyyə testi */
function gate(n){
  if(!KOD||isDone(n)||!dLimit())return 'open';
  const s=lvStart();if(s==null)return 'level';
  if(n<s)return 'open';
  if(n!==nextNew())return 'later';
  return dLeft()>0?'new':'tomorrow';
}
/* mövzu bitəndə müəllim cədvəlinə yazılır; yeni mövzu göndərilənə qədər telefonda da saxlanır */
function dRecord(n,stars,total,isNew,x){
  if(!KOD)return;
  const e={d:dayStr(),b:BOOK.id,n,s:stars,t:total,x};
  if(isNew){const a=dLocal();if(!a.some(x=>x.b===e.b&&x.n===e.n)){a.push(e);dSaveLocal(a)}}
  dPost(e,isNew);
}
function dPost(e,isNew){
  if(!API_URL)return Promise.resolve();
  return movzuGonder(KOD,e.n,e.s,e.t,e.d,e.x).then(r=>{
    if(!r||!r.ok)throw 0;
    if(SAGIRD&&r.daily)SAGIRD.daily=r.daily;
    if(isNew)dSaveLocal(dLocal().filter(x=>!(x.b===e.b&&x.n===e.n)));
  }).catch(()=>{});
}
/* əvvəl internet olmayanda göndərilməyənlər */
function dResend(){
  const srv=(SAGIRD&&SAGIRD.daily&&SAGIRD.daily.news)||[];
  const a=dLocal(),keep=a.filter(e=>!srv.some(([,b,n])=>b===e.b&&+n===e.n));
  if(keep.length!==a.length)dSaveLocal(keep);
  keep.filter(e=>e.b===BOOK.id).reduce((p,e)=>p.then(()=>dPost(e,true)),Promise.resolve());
}
/* mövzunun ətraflı nəticəsi: ilk cəhd, ikinci cəhd, cavabı göstərilən, səhv nömrələri, dəftər özünüqiyməti, vaxt */
function topicStats(){
  const ps=T.problems,auto=[],note=[];ps.forEach((p,k)=>(p.check||p.web?auto:note).push(k));
  const first=auto.filter(k=>st.first[k]===true).length;
  const second=auto.filter(k=>st.first[k]===false&&!st.shown[k]).length;
  const shown=auto.filter(k=>st.shown[k]).length;
  const wrong=auto.filter(k=>st.first[k]!==undefined&&st.first[k]!==true||st.shown[k]&&st.first[k]!==true).map(k=>k+1);
  const self=[note.filter(k=>st.self[k]===true).length,note.filter(k=>st.self[k]===false).length,note.filter(k=>st.self[k]===undefined).length];
  const done=ps.filter((p,k)=>st.first[k]!==undefined||st.shown[k]||st.self[k]!==undefined).length;
  tick();
  return {first,total:auto.length,x:{second,shown,wrong:[...new Set(wrong)],self,min:Math.round(st.act/6000)/10,done,count:ps.length}};
}
/* fəal vaxt: hər addımda ən çox 3 dəqiqə sayılır (uşaq telefonu buraxıb gedəndə vaxt şişməsin) */
function tick(){if(!st||!st.last)return;const now=Date.now();st.act+=Math.min(now-st.last,180000);st.last=now}
function dStart(n){
  if(!KOD||!API_URL||!st||st.started)return;st.started=true;
  movzuGonder(KOD,n,0,autoCount(T),dayStr(),{count:T.problems.length},'start').catch(()=>{});
}
function dLeave(){
  if(!KOD||!API_URL||!st||!st.started||st.logged||typeof st.n!=='number'||!T)return;
  const r=topicStats();movzuYarimciq(KOD,st.n,r.first,r.total,dayStr(),r.x);
}
addEventListener('pagehide',dLeave);
function todayCard(){
  const nx=nextNew();if(nx==null)return null;
  const left=dLeft();
  if(left<=0)return h('div',{class:'lvcard rest'},h('span',{class:'ic'},'🌙'),h('div',{},h('b',{},'Bugünlük bitdi! Afərin!'),h('span',{},'Sabah yeni mövzu açılacaq. İstəsən, keçdiyin mövzuları təkrar et.')));
  return h('a',{class:'lvcard today',href:'#t'+nx},h('span',{class:'ic'},'🎯'),h('div',{},h('b',{},'Bugünkü mövzu: Mövzu '+nx),h('span',{},ICON[nx]+' '+TP(nx).title+(left>1&&left!==Infinity?' · bu gün '+left+' mövzu aça bilərsən':''))));
}
const today=()=>{const d=new Date();return String(d.getDate()).padStart(2,'0')+'.'+String(d.getMonth()+1).padStart(2,'0')+'.'+d.getFullYear()};
function levelCard(){
  const s=lvStart();
  if(s==null)return h('a',{class:'lvcard',href:'#seviyye'},h('span',{class:'ic'},'🧭'),h('div',{},h('b',{},'Səviyyə testi – əvvəlcə bunu et'),h('span',{},'Haradan başlamalı olduğunu tapır · 2–12 sual')));
  const again=lvCanRetake()?h('button',{class:'lvagain',onclick(){LT={phase:'intro'};if(location.hash==='#seviyye')go();else location.hash='#seviyye'}},'🔄 Səviyyə testini yenidən et'):null;
  if(KOD&&s<LV_ALL&&nextNew()!=null)return h('div',{},todayCard(),again);
  const card=s>=LV_ALL
    ?h('a',{class:'lvcard done',href:'#seviyye'},h('span',{class:'ic'},'🏆'),h('div',{},h('b',{},'Səviyyə: bütün mövzular keçildi'),h('span',{},'Mövzuları təkrar et, sonra yoxlama testini et')))
    :h('a',{class:'lvcard done',href:'#t'+s},h('span',{class:'ic'},'🧭'),h('div',{},h('b',{},'Buradan başla: Mövzu '+s),h('span',{},ICON[s]+' '+TP(s).title+' · səviyyə testinə görə')));
  return h('div',{},card,again);
}
function levelPage(){
  if(!LT)LT={phase:lvStart()!=null&&!lvCanRetake()?'done':'intro'};
  if(LT.phase==='intro')lvIntro();else if(LT.phase==='q')lvQuestion();else lvResult();
}
function lvIntro(){
  const prev=lvStart();
  app.append(h('a',{class:'backlink',href:'#'},'← Bütün mövzular'),brand(null),
    h('div',{class:'card lvbox pop'},h('div',{class:'ic'},'🧭'),h('h2',{},'Səviyyə testi'),
      h('p',{style:'margin:0;text-align:center;font-weight:700'},'Bu qısa test uşağın hansı mövzudan başlamalı olduğunu göstərir.'),
      h('ul',{},h('li',{},'Hər bölmədən 2 sual, ən çox 12 sual (5–10 dəqiqə).'),h('li',{},'Suallar səslidir – valideyn uşağın yanında olsun.'),h('li',{},'Cavabın düz və ya səhv olduğu göstərilmir, sakitcə növbəti suala keçir.'),h('li',{},'Uşaq bilmədiyi sual gələndə test özü bitir – bu normaldır.'),KOD?h('li',{},'Nəticə müəllimə göndərilir.'):null),
      prev!=null?h('p',{class:'muted',style:'margin:0;text-align:center'},'Əvvəlki nəticə: '+(prev>=LV_ALL?'bütün mövzular':'Mövzu '+prev)):null,
      h('button',{class:'big',onclick(){LT={phase:'q',i:0,j:0,n:0,log:[]};st=null;go()}},'Başla →'),
      h('a',{class:'backlink',href:'#',style:'align-self:center'},'İndi yox')));
}
function lvQuestion(){
  const [tn,pi]=LV_Q[LT.i][LT.j],p=TP(tn).problems[pi];
  T=TP(tn);step=LT.n+1;
  if(!st||st.n!=='lv'+LT.n)st={n:'lv'+LT.n,ans:{},tries:{},first:{},shown:{},self:{}};
  app.append(h('div',{class:'prog'},h('div',{class:'lbl'},h('span',{},'🧭 Səviyyə testi'),h('span',{},'Bölmə '+(LT.i+1)+' / '+LV_Q.length)),h('div',{class:'track'},h('i',{style:'width:'+Math.max(4,(LT.i*2+LT.j)/(LV_Q.length*2)*100)+'%'}))));
  LVM=true;problemView(p,LT.n);
}
function lvAnswer(ok){
  const [tn,pi]=LV_Q[LT.i][LT.j];
  LT.log.push([tn,pi,ok?1:0]);LT.n++;st=null;
  if(!ok)return lvFinish(SECTIONS[LT.i][1]);
  if(++LT.j<2)return go();
  LT.i++;LT.j=0;
  if(LT.i>=LV_Q.length)return lvFinish(LV_ALL);
  go();
}
function lvFinish(start){
  P.lv={start,date:today(),log:LT.log,sent:false};save();
  if(SAGIRD&&SAGIRD.level)SAGIRD.level=null;
  LT={phase:'done',sending:!!KOD};go();
  if(start>=SECTIONS[1][1])setTimeout(confetti,250);
  lvSend();
}
function lvSend(){
  if(!KOD||!API_URL||!P.lv||P.lv.sent)return;
  seviyyeGonder(KOD,P.lv.start,P.lv.log||[]).then(r=>{
    if(!r||!r.ok)throw 0;
    P.lv.sent=true;save();
    if(SAGIRD){SAGIRD.level=r.level||null;SAGIRD.loaded=true}
    if(LT&&LT.phase==='done'){LT.sending=false;LT.sent=true}
    if(location.hash==='#seviyye'||!location.hash)render();
  }).catch(()=>{if(LT&&LT.phase==='done'){LT.sending=false;LT.failed=true;if(location.hash==='#seviyye')render()}});
}
function lvResult(){
  const s=lvStart()??(P.lv&&P.lv.start);
  if(s==null){LT={phase:'intro'};return lvIntro()}
  const cur=s>=LV_ALL?SECTIONS.length:SECTIONS.findIndex(([,a,b])=>s>=a&&s<=b);
  const list=h('div',{class:'lvsec'},SECTIONS.map(([name],i)=>h('div',{class:i<cur?'':i===cur?'cur':'later'},i<cur?'✅':i===cur?'👉':'⬜',(i+1)+'. '+name)));
  const status=!KOD?null:LT.sending?'⏳ Nəticə müəllimə göndərilir...':LT.failed?'⚠️ Nəticə göndərilmədi. İnternet olanda səhifəni yeniləyin – yenidən göndəriləcək.':'✅ Nəticə müəllimə göndərildi.';
  app.append(brand(null),h('div',{class:'card lvbox pop'},h('div',{class:'ic'},s>=LV_ALL?'🏆':'🧭'),
    h('h2',{},s>=LV_ALL?'Əla! Bütün bölmələri bilir!':'Səviyyə testi bitdi!'),
    s>=LV_ALL
      ?h('div',{style:'display:flex;flex-direction:column;gap:10px'},h('p',{style:'margin:0;text-align:center;font-weight:700'},BOOK.allText),BOOK.other&&BOOK.other.next?h('a',{class:'big',href:BOOK.other.href+(KOD?'?s='+KOD:''),style:'text-decoration:none;display:block;text-align:center;box-sizing:border-box'},BOOK.other.label):null)
      :h('a',{class:'big',href:'#t'+s,style:'text-decoration:none;display:block;text-align:center;box-sizing:border-box'},'Buradan başla: Mövzu '+s+' →',h('br'),h('span',{style:'font-size:16px;opacity:.9'},ICON[s]+' '+TP(s).title)),
    list,
    h('p',{class:'muted',style:'margin:0'},'Əvvəlki mövzular da açıqdır – təkrar üçün istifadə edə bilərsiniz.'),
    status?h('p',{style:'margin:0;font-weight:800'},status):null,
    h('a',{class:'backlink',href:'#',style:'align-self:center'},'← Bütün mövzular')));
}
function maybeAutoLevel(){
  if(!D||location.hash||lvStart()!=null)return;
  if(KOD&&!(SAGIRD&&SAGIRD.loaded))return;
  try{if(sessionStorage.getItem('riyaziyyat-lv-auto-'+BOOK.id))return;sessionStorage.setItem('riyaziyyat-lv-auto-'+BOOK.id,'1')}catch(e){return}
  location.hash='#seviyye';
}

/* ---------- topic ---------- */
let T=null,step=0,st=null;
let LOCKV=false;
function lockedView(n,gt){
  const t=TP(n);LOCKV=true;
  app.append(h('a',{class:'backlink',href:'#'},'← Bütün mövzular'),brand(null),
    h('div',{class:'card donebox pop'},h('div',{class:'trophy'},gt==='level'?'🧭':'🔒'),h('h2',{style:'font-size:24px;font-weight:900'},'Mövzu '+n+'. '+t.title),
      h('p',{style:'font-weight:800'},gt==='level'?'Əvvəlcə səviyyə testini et – haradan başlamalı olduğunu tapaq.':gt==='tomorrow'?'Bu mövzu sabah açılacaq. Bu gün çox yaxşı çalışdın!':'Bu mövzu hələ bağlıdır. Mövzular hər gün bir-bir açılır.'),
      gt==='level'?h('a',{class:'big',href:'#seviyye',style:'text-decoration:none;display:block'},'🧭 Səviyyə testi →'):null,
      h('a',{class:'backlink',href:'#'},'← Bütün mövzular')));
}
function topic(n){
  const gt=gate(n);if(gt!=='open'&&gt!=='new')return lockedView(n,gt);
  T=TP(n);
  if(!st||st.n!==n)st={n,ans:{},tries:{},first:{},shown:{},self:{},act:0,last:Date.now()};
  tick();
  const total=T.problems.length;
  const lbl=step===0?'Əsas fikir':step<=total?'Tapşırıq '+step+' / '+total:'Nəticə';
  app.append(h('a',{class:'backlink',href:'#'},'← Bütün mövzular'),
    h('div',{class:'prog'},h('div',{class:'lbl'},h('span',{},'Mövzu '+n+'. '+T.title),h('span',{},lbl)),h('div',{class:'track'},h('i',{style:'width:'+Math.max(4,step/(total+1)*100)+'%'}))));
  if(step===0)conceptView(); else if(step<=total)problemView(T.problems[step-1],step-1); else doneView(n);
}
let lastAuto=null;
function teacher(text,aud,tag){
  foxEl=h('div',{class:'fox','aria-hidden':'true'},'🦊');
  vEl=audioUrl(aud)?h('button',{class:'vbtn',onclick(){player&&!player.paused?stop():play(aud)}},'🔊 Dinlə'):null;
  const auto=audioUrl(aud)?h('button',{class:'auto'+(P.sound?'':' off'),onclick(){P.sound=!P.sound;save();auto.className='auto'+(P.sound?'':' off');auto.lastChild.textContent=P.sound?'Avtomatik səs: açıq':'Avtomatik səs: bağlı';if(!P.sound)stop()}},h('i'),P.sound?'Avtomatik səs: açıq':'Avtomatik səs: bağlı'):null;
  const akey=location.hash+'|'+step+'|'+aud;
  if(P.sound&&audioUrl(aud)&&akey!==lastAuto){lastAuto=akey;setTimeout(()=>play(aud),300)}
  return h('div',{class:'card teach'},foxEl,h('div',{class:'tag'},h('b',{},'Müəllim oxuyur'),h('span',{},tag)),h('h2',{},text),(vEl||auto)?h('div',{class:'voice'},vEl,auto):null);
}
function conceptView(){
  app.append(teacher(T.concept,T.conceptAudio,'Əsas fikir'),h('div',{class:'card task concept pop'},h('div',{class:'paper'},h('img',{src:T.conceptImg,alt:T.concept}))));
  setBar(null,'Tapşırıqlara başla →',()=>{step=1;if(!LVM&&typeof st.n==='number')dStart(st.n);go()},'go');
}
function problemView(p,k){
  const c=p.check, done=st.first[k]!==undefined||st.shown[k];
  app.append(teacher(p.ins,p.audio,'Tapşırıq '+(k+1)));
  const w=p.web,src=w?w.stem:p.img;
  const task=h('div',{class:'card task pop'},src?h('div',{class:'paper'},h('img',{src,alt:''})):null);
  app.append(task);
  if(w){webView(p,k,task);return}
  if(c){
    let a=st.ans[k]||(st.ans[k]=c.slots.map(()=>null)); let active=Math.max(0,a.indexOf(null));
    const solved=st.first[k]!==undefined&&a.every((v,j)=>String(v)===String(c.slots[j]));
    const locked=solved||st.shown[k];
    const eq=h('div',{class:'eq'});const slots=c.slots.map((_,j)=>{const s=h('button',{class:'slot',disabled:locked,onclick(){active=j;paint()}});return s});
    if(c.mode==='sign')c.pairs.forEach(([x,y],j)=>{if(j)eq.append(h('span',{class:'br'}));eq.append(h('span',{class:'fixed'},x),slots[j],h('span',{class:'fixed'},y))});
    else slots.forEach(s=>eq.append(s));
    const paint=()=>slots.forEach((s,j)=>{s.textContent=a[j]??'';let cl='slot';if(a[j]!==null)cl+=' filled';if(!locked&&j===active)cl+=' active';if(locked)cl+=String(a[j])===String(c.slots[j])?' right':' wrong';s.className=cl});
    task.append(h('p',{class:'paperhint'},c.slots.length>1?'Cavabları soldan sağa yaz:':'Cavabı yaz:'),eq);
    const set=v=>{a[active]=v;if(v!==null&&active<a.length-1&&c.mode==='sign')active++;paint();upd()};
    if(!locked){
      if(c.mode==='sign')task.append(h('div',{class:'signs'},['>','<','='].map(sg=>h('button',{onclick(){set(sg)}},sg))));
      else{const pad=h('div',{class:'pad'});[1,2,3,4,5,6,7,8,9,0].forEach(d=>pad.append(h('button',{onclick(){const cur=a[active]==null?'':String(a[active]);let v=(cur+d).replace(/^0(\d)/,'$1');if(v.length>2)v=String(d);set(Number(v))}},String(d))));pad.append(h('button',{class:'del',onclick(){set(null)}},'⌫ Sil'));task.append(pad)}
    }
    const tries=st.tries[k]||0;
    if(solved)task.append(h('div',{class:'fb ok'},h('span',{},'🌟'),st.first[k]?'Əla! Düzgün cavab!':'Düzgün! Afərin, tapdın!'));
    else if(st.shown[k])task.append(h('div',{class:'fb no'},h('span',{},'💡'),'Düzgün cavab: '+p.ans));
    else if(tries)task.append(h('div',{class:'fb no'},h('span',{},'💪'),'Yenə cəhd et! Səhv xananı düzəlt.'));
    paint();
    function upd(){
      if(locked){setBar(k,'Növbəti →',next,'go');return}
      const full=a.every(v=>v!==null);
      setBar(k,'Cavabı yoxla ✓',()=>{const ok=a.every((v,j)=>String(v)===String(c.slots[j]));if(LVM)return lvAnswer(ok);st.tries[k]=(st.tries[k]||0)+1;
        if(ok){if(st.first[k]===undefined)st.first[k]=st.tries[k]===1;chime(true);confetti();praise(true)}else{chime(false);praise(st.tries[k]<2?false:null);if(st.tries[k]>=2)st.shown[k]=true;if(st.first[k]===undefined&&st.tries[k]>=2)st.first[k]=false}
        render()},'main',!full);
    }
    upd();
  }else{
    const r=h('div',{class:'reveal'});
    if(!st.shown[k]){r.append(h('p',{class:'paperhint'},p.icon==='circle'?'Düzgün şəkli barmağınla göstər və ya dəftərdə dairəyə al.':p.icon==='connect'?'Dəftərdə xətlə birləşdir.':p.icon==='draw'?'Dəftərdə çək.':'Dəftərdə yaz.'),h('button',{class:'sec',onclick(){st.shown[k]=true;render()}},'👀 Cavabı göstər'))}
    else{r.append(h('div',{class:'answer'},'✅ '+p.ans),h('div',{class:'self'},h('button',{class:st.self[k]===true?'on':'',onclick(){st.self[k]=true;render()}},'😊 Düz tapdım'),h('button',{class:st.self[k]===false?'on':'',onclick(){st.self[k]=false;render()}},'🤔 Səhv etdim')))}
    task.append(r);
    setBar(k,'Növbəti →',next,'go');
  }
}
/* ---------- tap answers: choice, multi, order, match, dots ---------- */
function webView(p,k,task){
  const w=p.web,m=w.mode;
  const area=h('div',{class:'task'});task.append(area);
  const init={choice:null,multi:[],order:[],match:(w.left||[]).map(()=>null),dots:Array(10).fill(false)}[m];
  let a=st.ans[k]!==undefined?st.ans[k]:(st.ans[k]=JSON.parse(JSON.stringify(init)));
  const same=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
  const isOk=()=>m==='choice'?a===w.ans:m==='multi'?same([...a].sort((x,y)=>x-y),w.ans):m==='order'?same(a,w.ans):m==='match'?same(a,w.ans):a.filter(Boolean).length===w.n;
  const set=v=>{st.ans[k]=a=v;draw()};
  draw();
  function draw(){
  area.replaceChildren();
  const solved=st.first[k]!==undefined&&isOk(), shown=!!st.shown[k], locked=solved||shown;
  const optEl=(o,j,cls,fn)=>h('button',{class:'opt'+cls,disabled:locked,onclick:fn},o.img?h('img',{src:o.img,alt:''}):o.t);
  let hint;
  if(m==='choice'||m==='multi'||m==='order'){
    hint=m==='choice'?'Düzgün cavaba toxun:':m==='multi'?'Uyğun olanların hamısına toxun:':(w.hint||'Heyvanlara sıra ilə toxun: 1-ci, 2-ci, 3-cü yer.');
    const box=h('div',{class:'opts'+(w.opts.length<=3?' few':'')});
    w.opts.forEach((o,j)=>{
      let cls='';const pos=m==='order'?a.indexOf(j):-1;
      const sel=m==='choice'?a===j:m==='multi'?a.includes(j):pos>=0;
      const good=m==='choice'?w.ans===j:m==='multi'?w.ans.includes(j):false;
      if(sel)cls+=' sel';
      if(locked&&m!=='order'){if(good)cls+=' right';else if(sel)cls+=' wrong'}
      const b=optEl(o,j,cls,()=>{
        if(m==='choice')set(j);
        else if(m==='multi')set(a.includes(j)?a.filter(x=>x!==j):[...a,j]);
        else set(pos>=0?a.slice(0,pos):[...a,j]);
      });
      const badge=m==='order'?(locked&&shown?w.ans.indexOf(j)+1:pos>=0?pos+1:0):0;
      if(badge)b.append(h('span',{class:'badge'},String(badge)));
      box.append(b)});
    area.append(h('p',{class:'paperhint'},hint),box);
  }else if(m==='match'){
    hint='Hər qrupu say və onun ədədinə toxun:';
    const rows=h('div',{class:'mrows'});
    w.left.forEach((L,i)=>{const nums=h('div',{class:'nums'});
      w.right.forEach((t,j)=>{let cls='';if(a[i]===j)cls+=' sel';if(locked){if(w.ans[i]===j)cls+=' right';else if(a[i]===j)cls+=' wrong'}
        nums.append(optEl({t},j,cls,()=>{const b=[...a];b[i]=j;set(b)}))});
      rows.append(h('div',{class:'mrow'},h('div',{class:'lft'},h('img',{src:L.img,alt:''})),nums))});
    area.append(h('p',{class:'paperhint'},hint),rows);
  }else if(m==='dots'){
    hint='Dairələrə toxun və rənglə:';
    const fr=h('div',{class:'dframe'});
    a.forEach((on,j)=>fr.append(h('button',{class:'dcell'+(on?' on':''),disabled:locked,'aria-label':'dairə',onclick(){const b=[...a];b[j]=!b[j];set(b)}})));
    area.append(h('p',{class:'paperhint'},hint),fr,h('div',{class:'dcount'},'🔵 '+a.filter(Boolean).length));
  }
  if(m==='order'&&!locked&&a.length)area.append(h('button',{class:'sec',onclick(){set([])}},'⌫ Yenidən başla'));
  if(solved)area.append(h('div',{class:'fb ok'},h('span',{},'🌟'),st.first[k]?'Əla! Düzgün cavab!':'Düzgün! Afərin, tapdın!'));
  else if(shown)area.append(h('div',{class:'fb no'},h('span',{},'💡'),'Düzgün cavab: '+p.ans));
  else if(st.tries[k])area.append(h('div',{class:'fb no'},h('span',{},'💪'),'Yenə cəhd et!'));
  if(locked){setBar(k,'Növbəti →',next,'go');return}
  const ready=m==='choice'?a!==null:m==='multi'?a.length>0:m==='order'?a.length===w.opts.length:m==='match'?a.every(v=>v!==null):a.some(Boolean);
  setBar(k,'Cavabı yoxla ✓',()=>{const ok=isOk();if(LVM)return lvAnswer(ok);st.tries[k]=(st.tries[k]||0)+1;
    if(ok){if(st.first[k]===undefined)st.first[k]=st.tries[k]===1;chime(true);confetti();praise(true)}
    else{chime(false);praise(st.tries[k]<2?false:null);if(st.tries[k]>=2){st.shown[k]=true;if(st.first[k]===undefined)st.first[k]=false}}
    render()},'main',!ready);
}
}
function next(){step++;go()}
function doneView(n){
  const t=T,auto=autoCount(t),stars=Object.entries(st.first).filter(([k,v])=>v===true).length;
  if(!st.logged){const isNew=!!KOD&&gate(n)==='new',r=topicStats();st.logged=true;
    P.t[n]={done:true,stars:Math.max(stars,(P.t[n]&&P.t[n].stars)||0)};save();
    dRecord(n,stars,auto,isNew,r.x)}
  const g=n<BOOK.last?gate(n+1):null,rest=!!KOD&&g!=null&&g!=='open'&&g!=='new';
  if(stars>=auto*0.7)setTimeout(confetti,200);
  app.append(h('div',{class:'card donebox pop'},h('div',{class:'trophy'},stars>=auto*0.7?'🏆':'🌱'),h('h2',{style:'font-size:28px;font-weight:900'},'Mövzu bitdi!'),
    h('p',{},'İlk cəhddə düzgün: ⭐ '+stars+' / '+auto),
    h('p',{class:'muted'},stars>=auto*0.7?'Əla iş! Növbəti mövzuya keçə bilərsən.':'Yaxşı çalışdın! Bu mövzunu bir də təkrar etmək faydalı olar.'),
    rest?h('div',{class:'lvcard rest',style:'width:100%;box-sizing:border-box;text-align:left'},h('span',{class:'ic'},'🌙'),h('div',{},h('b',{},'Bugünlük bitdi! Afərin!'),h('span',{},'Sabah yeni mövzu açılacaq. İstəsən, keçdiyin mövzuları təkrar et.')))
      :n<BOOK.last?h('a',{class:'big',href:'#t'+(n+1),style:'text-decoration:none;display:block'},'Növbəti mövzu →'):null,
    h('button',{class:'sec',onclick(){st=null;step=0;lastAuto=null;go()}},'🔄 Mövzunu təkrarla'),
    h('a',{class:'backlink',href:'#'},'← Bütün mövzular')));
}
function setBar(k,label,fn,kind,disabled){
  if(LVM){barIn.replaceChildren(h('span',{class:'qn'},'Sual '+(k+1)),h('button',{class:'bbtn main',disabled:!!disabled,onclick:fn},'Cavab ver →'));bar.hidden=false;return}
  const back=h('button',{class:'bbtn back','aria-label':'Geri',disabled:step===0,onclick(){step--;go()}},'←');
  const main=h('button',{class:'bbtn main'+(kind==='go'?' go':''),disabled:!!disabled,onclick:fn},label);
  barIn.replaceChildren(back,h('span',{class:'qn'},k==null?'0 / '+T.problems.length:(k+1)+' / '+T.problems.length),main);bar.hidden=false;
}

/* ---------- router ---------- */
function render(){stop();LVM=false;LOCKV=false;app.replaceChildren();bar.hidden=true;if(location.hash==='#seviyye'){levelPage();return}const m=location.hash.match(/^#t(\d+)$/);if(m&&TP(+m[1]))topic(+m[1]);else home();playPraise()}
function go(){render();scrollTo(0,0)}
addEventListener('hashchange',()=>{dLeave();st=null;step=0;lastAuto=null;if(location.hash!=='#seviyye'||!LT||LT.phase!=='intro')LT=null;go()});
const KOD=sagirdKodu();
let SAGIRD=KOD?{name:sagirdAdiYaddas(KOD),done:false}:null;
if(KOD&&API_URL)sagirdMelumati(KOD).then(r=>{if(r&&r.ok){
  SAGIRD={name:r.name,done:!!r.done,level:r.level||null,daily:r.daily||null,loaded:true};sagirdAdiYaddas(KOD,r.name);
  dResend();
  const srv=r.level&&r.level.done;
  if(!srv&&P.lv&&P.lv.sent){delete P.lv;save()} // müəllim nəticəni silib – testi yenidən etmək olar
  if(!srv&&P.lv&&!P.lv.sent)lvSend();             // əvvəl göndərilməyən nəticə
  if(D){if(!location.hash||LOCKV)render();maybeAutoLevel()}
}}).catch(()=>{});
Promise.all([fetch('data/topics.json').then(r=>r.json()),fetch('data/audio.json').then(r=>r.json()).catch(()=>[])]).then(([d,a])=>{D=d;a.forEach(id=>AUD[id]=1);go();maybeAutoLevel()}).catch(()=>{app.replaceChildren(h('p',{class:'muted'},'Məlumat yüklənmədi. Səhifəni yeniləyin.'))});
