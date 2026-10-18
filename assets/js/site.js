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
  // evento de clique no WhatsApp (Vercel Analytics, se ativado, e GA, se existir)
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href*="api.whatsapp.com"]');if(!a)return;
    var p=location.pathname;
    try{if(window.va)window.va('event',{name:'whatsapp_click',data:{pagina:p}})}catch(_){}
    try{if(window.gtag)window.gtag('event','whatsapp_click',{pagina:p})}catch(_){}
  },true);
})();
