(function () {
  // ---------------------------------------------------------------------------
  // Elements: menu button, project list, and direction arrow.
  // ---------------------------------------------------------------------------
  const listToggle = document.getElementById('list-toggle');
  const projectMenu = document.getElementById('project-menu');
  const arrow = document.getElementById('arrow');

  if (!listToggle || !projectMenu) {
    return;
  }

  // ---------------------------------------------------------------------------
  // Overlay: dark layer displayed behind the open menu.
  // ---------------------------------------------------------------------------
  let menuOverlay = document.querySelector('.menu-overlay');
  if (!menuOverlay) {
    menuOverlay = document.createElement('div');
    menuOverlay.className = 'menu-overlay';
    document.body.appendChild(menuOverlay);
  }

  // ---------------------------------------------------------------------------
  // Header position: keep the menu directly below the header.
  // ---------------------------------------------------------------------------
  const headerEl = document.querySelector('header');

  function getHeaderHeight() {
    return headerEl && headerEl.offsetHeight ? headerEl.offsetHeight : 55;
  }

  function updateMenuTop() {
    const headerHeight = getHeaderHeight();
    projectMenu.style.top = headerHeight + 'px';
    menuOverlay.style.top = headerHeight + 'px';
    document.documentElement.style.setProperty('--menu-top', headerHeight + 'px');
  }

  // Initialize the position after the page has calculated the header size.
  requestAnimationFrame(updateMenuTop);
  window.addEventListener('resize', updateMenuTop);

  // ---------------------------------------------------------------------------
  // Menu state: save the page position while the mobile menu is open.
  // ---------------------------------------------------------------------------
  let scrollY = 0;

  // ---------------------------------------------------------------------------
  // Open mobile menu: lock the page and display the menu over the content.
  // ---------------------------------------------------------------------------
  function openMobileMenu() {
    updateMenuTop();
    const headerHeight = getHeaderHeight();

    menuOverlay.style.display = 'block';
    menuOverlay.style.left = '0';
    menuOverlay.style.right = '0';
    menuOverlay.style.top = headerHeight + 'px';
    menuOverlay.style.bottom = '0';
    menuOverlay.style.background = 'rgba(0,0,0,0.45)';
    menuOverlay.style.zIndex = '900';
    menuOverlay.classList.add('active');

    projectMenu.style.display = 'block';
    projectMenu.style.position = 'fixed';
    projectMenu.style.left = '0';
    projectMenu.style.right = '0';
    projectMenu.style.top = headerHeight + 'px';
    projectMenu.style.bottom = '0';
    projectMenu.style.width = '100vw';
    projectMenu.style.maxWidth = '100vw';
    projectMenu.style.minWidth = '0';
    projectMenu.style.maxHeight = 'calc(100vh - ' + headerHeight + 'px)';
    projectMenu.style.overflowY = 'auto';
    projectMenu.style.boxSizing = 'border-box';
    projectMenu.style.padding = '16px 18px 20px 18px';
    projectMenu.style.zIndex = '901';
    projectMenu.classList.add('active');

    if (arrow) arrow.textContent = '↑';
    scrollY = window.scrollY || window.pageYOffset;
    document.body.style.top = '-' + scrollY + 'px';
    document.body.classList.add('menu-open');
  }

  // ---------------------------------------------------------------------------
  // Close mobile menu: restore the page and remove temporary inline styles.
  // ---------------------------------------------------------------------------
  function closeMobileMenu() {
    menuOverlay.classList.remove('active');
    menuOverlay.style.display = '';
    menuOverlay.style.left = '';
    menuOverlay.style.right = '';
    menuOverlay.style.top = '';
    menuOverlay.style.bottom = '';
    menuOverlay.style.background = '';
    menuOverlay.style.zIndex = '';

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

    if (arrow) arrow.textContent = '↓';
    document.body.classList.remove('menu-open');
    document.body.style.top = '';
    if (scrollY) window.scrollTo(0, scrollY);
  }

  // ---------------------------------------------------------------------------
  // Device type: use mobile behavior on small, touch-enabled, and iPad devices.
  // ---------------------------------------------------------------------------
  function isMobileLike() {
    const touch = navigator.maxTouchPoints > 0 || 'ontouchstart' in window;
    const userAgent = (navigator.userAgent || '').toLowerCase();
    const isIPad = userAgent.includes('ipad') ||
      (userAgent.includes('macintosh') && navigator.maxTouchPoints > 1);
    const smallViewport = window.matchMedia('(max-width: 900px)').matches;

    return smallViewport || touch || isIPad;
  }

  // ---------------------------------------------------------------------------
  // Toggle button: open the mobile menu or toggle the desktop dropdown.
  // ---------------------------------------------------------------------------
  listToggle.addEventListener('click', function (event) {
    event.stopPropagation();

    if (isMobileLike()) {
      if (projectMenu.classList.contains('active')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
      return;
    }

    projectMenu.classList.toggle('active');
    if (arrow) {
      arrow.textContent = projectMenu.classList.contains('active') ? '↑' : '↓';
    }
  });

  // ---------------------------------------------------------------------------
  // Close events: close the menu outside the menu or with the Escape key.
  // ---------------------------------------------------------------------------
  menuOverlay.addEventListener('click', closeMobileMenu);

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      closeMobileMenu();
    }
  });

  document.addEventListener('click', function (event) {
    if (projectMenu.contains(event.target) || listToggle.contains(event.target)) {
      return;
    }

    if (isMobileLike()) {
      closeMobileMenu();
    } else {
      projectMenu.classList.remove('active');
      if (arrow) arrow.textContent = '↓';
    }
  });
})();
