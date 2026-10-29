(function(){
  var reduz=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // revelar ao rolar
  var alvo=document.querySelectorAll('.s-card,.h-sobre>*,.h-esportes a,.h-sec h2,.s-main h2,.s-main>p,.s-main>ul,.s-main>ol,.s-faq details,.s-cta,.pt-papel,.pt-passo,.s-grid a,.s-foto,.h-end');
  alvo.forEach(function(el){el.classList.add('rv')});
  if('IntersectionObserver' in window && !reduz){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.06});
    alvo.forEach(function(el,i){el.style.transitionDelay=((i%3)*80)+'ms';io.observe(el)});
  }else{alvo.forEach(function(el){el.classList.add('on')})}
  // cabeçalho compacto, parallax leve no hero e contagem de cliques no WhatsApp
  var h=document.querySelector('.s-header'),v=document.querySelector('.h-hero .fundo'),f=document.querySelector('.s-foto img');
  var t=false;
  function g(){t=false;var y=window.scrollY||0;if(h)h.classList.toggle('mini',y>40);
    if(!reduz&&y<900){if(v)v.style.transform='translate3d(0,'+(y*.16)+'px,0) scale(1.08)';if(f)f.style.transform='translate3d(0,'+(y*.06)+'px,0) scale(1.06)'}}
  window.addEventListener('scroll',function(){if(!t){t=true;requestAnimationFrame(g)}},{passive:true});g();
  // vídeo: pausa fora da tela ou com movimento reduzido
  if(v&&v.tagName==='VIDEO'){
    if(reduz){v.removeAttribute('autoplay');v.pause()}
    else if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?v.play().catch(function(){}):v.pause()})}).observe(v)}
  }
  // menu do celular fecha ao navegar
  var mn=document.getElementById('mn');
  if(mn)document.querySelectorAll('.s-nav a').forEach(function(a){a.addEventListener('click',function(){mn.checked=false})});
  // blog: busca e filtro por tema (sem JS, todos os artigos aparecem)
  var bg=document.querySelector('[data-blog]');
  if(bg){
    var cs=[].slice.call(bg.querySelectorAll('.b-card')),bi=document.querySelector('.b-busca'),
        chs=[].slice.call(document.querySelectorAll('.b-chip[data-tema]')),bv=document.querySelector('.b-vazio'),
        tema=new URLSearchParams(location.search).get('tema')||'',bt;
    var sem=function(x){return (x||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase()};
    function aplica(){
      var q=sem(bi?bi.value.trim():''),n=0;
      cs.forEach(function(c){
        var ok=(!tema||(' '+c.getAttribute('data-temas')+' ').indexOf(' '+tema+' ')>=0)&&(!q||q.split(/\s+/).every(function(p){return sem(c.getAttribute('data-busca')).indexOf(p)>=0}));
        c.hidden=!ok;if(ok)n++;
      });
      bg.classList.toggle('filtrando',!!(tema||q));
      chs.forEach(function(b){b.classList.toggle('on',b.getAttribute('data-tema')===tema);b.setAttribute('aria-pressed',b.getAttribute('data-tema')===tema)});
      if(bv)bv.hidden=n>0;
    }
    chs.forEach(function(b){b.addEventListener('click',function(){
      tema=b.getAttribute('data-tema');aplica();
      try{var u=new URL(location.href);tema?u.searchParams.set('tema',tema):u.searchParams.delete('tema');history.replaceState(null,'',u)}catch(_){}
      if(window.gtag&&tema)gtag('event','blog_tema',{tema:tema});
    })});
    if(bi)bi.addEventListener('input',function(){aplica();clearTimeout(bt);
      bt=setTimeout(function(){var q=bi.value.trim();if(window.gtag&&q.length>2)gtag('event','search',{search_term:q})},1500)});
    if(!chs.some(function(b){return b.getAttribute('data-tema')===tema}))tema='';
    aplica();
  }
  // origem do lead: guarda de onde a pessoa chegou e anota no texto do WhatsApp
  var og=(function(){
    try{var k=sessionStorage.getItem('og');if(k)return k}catch(_){}
    var q=new URLSearchParams(location.search),o=q.get('utm_source')||q.get('origem')||'';
    if(!o&&document.referrer){try{
      var r=new URL(document.referrer).hostname.replace(/^www\./,'');
      if(r&&r.indexOf('edferrarijr.com')<0)o=/google\./.test(r)?'google':/bing\./.test(r)?'bing':/instagram\./.test(r)?'instagram':/facebook\.|fb\./.test(r)?'facebook':/duckduckgo\./.test(r)?'duckduckgo':r;
    }catch(_){}}
    o=(o||'direto').toLowerCase().replace(/[^a-z0-9._-]/g,'').slice(0,30)||'direto';
    try{sessionStorage.setItem('og',o)}catch(_){}
    return o;
  })();
  var pg=location.pathname.replace(/^\/+|\/+$/g,'').split('/').pop()||'inicio';
  function marca(a){
    if(a.getAttribute('data-og'))return;
    try{var u=new URL(a.href),t=u.searchParams.get('text')||'';
      u.searchParams.set('text',t+' (origem: '+og+' · página: '+pg+')');a.href=u.toString();a.setAttribute('data-og','1')}catch(_){}
  }
  document.querySelectorAll('a[href*="api.whatsapp.com"]').forEach(marca);
  // Google Analytics 4: só liga quando o ID de medição (G-XXXXXXX) for preenchido
  var GA_ID='G-05ECV1TCKJ';
  if(GA_ID){
    var gs=document.createElement('script');gs.async=true;gs.src='https://www.googletagmanager.com/gtag/js?id='+GA_ID;document.head.appendChild(gs);
    window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
    gtag('js',new Date());gtag('set','user_properties',{origem:og});gtag('config',GA_ID);
  }
  // evento de clique no WhatsApp (Vercel Analytics, se ativado, e GA, se existir)
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href*="api.whatsapp.com"]');if(!a)return;
    var p=location.pathname;marca(a);
    try{if(window.va)window.va('event',{name:'whatsapp_click',data:{pagina:p,origem:og}})}catch(_){}
    try{if(window.gtag)window.gtag('event','whatsapp_click',{pagina:p,origem:og})}catch(_){}
  },true);
})();
