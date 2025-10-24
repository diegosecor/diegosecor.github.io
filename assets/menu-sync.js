(function(){
  const listToggle = document.getElementById('list-toggle');
  const projectMenu = document.getElementById('project-menu');
  const arrow = document.getElementById('arrow');

  if (!listToggle || !projectMenu) {
    return;
  }

  // create overlay if needed
  let menuOverlay = document.querySelector('.menu-overlay');
  if (!menuOverlay) {
    menuOverlay = document.createElement('div');
    menuOverlay.className = 'menu-overlay';
    document.body.appendChild(menuOverlay);
  }

  // Keep the project menu and overlay flush with the header on mobile.
  const headerEl = document.querySelector('header');
  function updateMenuTop() {
    const h = (headerEl && headerEl.offsetHeight) ? headerEl.offsetHeight : 55;
    projectMenu.style.top = h + 'px';
    if (menuOverlay) menuOverlay.style.top = h + 'px';
  }
  // run on next frame to ensure sizes are available
  requestAnimationFrame(updateMenuTop);
  window.addEventListener('resize', updateMenuTop);

  let scrollY = 0;
  function openMobileMenu(){
    updateMenuTop();
    menuOverlay.classList.add('active');
    projectMenu.classList.add('active');
    if (arrow) arrow.textContent = '↑';
    scrollY = window.scrollY || window.pageYOffset;
    document.body.style.top = '-' + scrollY + 'px';
    document.body.classList.add('menu-open');
  }
  function closeMobileMenu(){
    menuOverlay.classList.remove('active');
    projectMenu.classList.remove('active');
    if (arrow) arrow.textContent = '↓';
    document.body.classList.remove('menu-open');
    document.body.style.top = '';
    if (scrollY) window.scrollTo(0, scrollY);
  }

  listToggle.addEventListener('click', function(e){
    e.stopPropagation();
    // Treat small screens and tablets (up to 900px) as mobile for the menu behavior
    if (window.matchMedia && window.matchMedia('(max-width: 900px)').matches){
      if (projectMenu.classList.contains('active')) closeMobileMenu(); else openMobileMenu();
    } else {
      projectMenu.classList.toggle('active');
      if (arrow) arrow.textContent = projectMenu.classList.contains('active') ? '↑' : '↓';
    }
  });

  menuOverlay.addEventListener('click', closeMobileMenu);
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') { closeMobileMenu(); } });
  document.addEventListener('click', function(e){
    if (!projectMenu.contains(e.target) && !listToggle.contains(e.target)) {
      if (window.matchMedia && window.matchMedia('(max-width: 900px)').matches) closeMobileMenu();
      else { projectMenu.classList.remove('active'); if (arrow) arrow.textContent = '↓'; }
    }
  });
})();
