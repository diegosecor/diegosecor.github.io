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
    // expose CSS variable for fallback stylesheets
    try { document.documentElement.style.setProperty('--menu-top', h + 'px'); } catch (e) {}
  }
  // run on next frame to ensure sizes are available
  requestAnimationFrame(updateMenuTop);
  window.addEventListener('resize', updateMenuTop);

  let scrollY = 0;
  function openMobileMenu(){
    updateMenuTop();
    // Ensure overlay and menu are visible and full-width on tablets by
    // applying inline styles (this overrides per-page inline CSS ordering).
    if (menuOverlay) {
      menuOverlay.style.display = 'block';
      menuOverlay.style.left = '0';
      menuOverlay.style.right = '0';
      menuOverlay.style.top = projectMenu.style.top || (headerEl ? headerEl.offsetHeight + 'px' : '55px');
      menuOverlay.style.bottom = '0';
      menuOverlay.style.background = 'rgba(0,0,0,0.45)';
      menuOverlay.style.zIndex = '900';
      menuOverlay.classList.add('active');
    }
    if (projectMenu) {
      projectMenu.style.display = 'block';
      projectMenu.style.position = 'fixed';
      projectMenu.style.left = '0';
      projectMenu.style.right = '0';
      projectMenu.style.top = projectMenu.style.top || (headerEl ? headerEl.offsetHeight + 'px' : '55px');
      projectMenu.style.bottom = '0';
      projectMenu.style.width = '100vw';
      projectMenu.style.maxWidth = '100vw';
      projectMenu.style.minWidth = '0';
      projectMenu.style.maxHeight = 'calc(100vh - ' + (headerEl ? headerEl.offsetHeight + 'px' : '55px') + ')';
      projectMenu.style.overflowY = 'auto';
      projectMenu.style.boxSizing = 'border-box';
      projectMenu.style.padding = '16px 18px 20px 18px';
      projectMenu.style.zIndex = '901';
      projectMenu.classList.add('active');
    }
    if (arrow) arrow.textContent = '↑';
    scrollY = window.scrollY || window.pageYOffset;
    document.body.style.top = '-' + scrollY + 'px';
    document.body.classList.add('menu-open');
  }
  function closeMobileMenu(){
    if (menuOverlay) {
      menuOverlay.classList.remove('active');
      menuOverlay.style.display = '';
      menuOverlay.style.left = '';
      menuOverlay.style.right = '';
      menuOverlay.style.top = '';
      menuOverlay.style.bottom = '';
      menuOverlay.style.background = '';
      menuOverlay.style.zIndex = '';
    }
    if (projectMenu) {
      projectMenu.classList.remove('active');
      projectMenu.style.display = '';
      projectMenu.style.position = '';
      projectMenu.style.left = '';
      projectMenu.style.right = '';
      projectMenu.style.top = '';
      projectMenu.style.bottom = '';
      projectMenu.style.width = '';
      projectMenu.style.maxWidth = '';
      projectMenu.style.minWidth = '';
      projectMenu.style.maxHeight = '';
      projectMenu.style.overflowY = '';
      projectMenu.style.boxSizing = '';
      projectMenu.style.padding = '';
      projectMenu.style.zIndex = '';
    }
    if (arrow) arrow.textContent = '↓';
    document.body.classList.remove('menu-open');
    document.body.style.top = '';
    if (scrollY) window.scrollTo(0, scrollY);
  }

  // Decide whether current device should behave as "mobile list".
  // Use viewport width OR touch-capable devices (many iPad Pros have large CSS widths).
  function isMobileLike() {
    try {
      const touch = (navigator.maxTouchPoints && navigator.maxTouchPoints > 0) || ('ontouchstart' in window);
      const ua = (navigator.userAgent || '').toLowerCase();
      const isiPad = ua.indexOf('ipad') !== -1 || (ua.indexOf('macintosh') !== -1 && navigator.maxTouchPoints > 1);
      const smallViewport = window.matchMedia && window.matchMedia('(max-width: 900px)').matches;
      return smallViewport || touch || isiPad;
    } catch (e) { return false; }
  }

  listToggle.addEventListener('click', function(e){
    e.stopPropagation();
    if (isMobileLike()) {
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
      if (isMobileLike()) closeMobileMenu();
      else { projectMenu.classList.remove('active'); if (arrow) arrow.textContent = '↓'; }
    }
  });
})();
