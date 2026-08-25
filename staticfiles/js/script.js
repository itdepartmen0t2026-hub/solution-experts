
document.addEventListener('DOMContentLoaded',()=>{
 document.querySelectorAll('.year').forEach(e=>e.textContent=new Date().getFullYear());
 const path=location.pathname.replace(/\\/g,'/');
 document.querySelectorAll('.navbar a.nav-link').forEach(a=>{const href=a.getAttribute('href'); if(href && !href.startsWith('#') && path.endsWith(href.replace('../',''))) a.classList.add('active');});
});
