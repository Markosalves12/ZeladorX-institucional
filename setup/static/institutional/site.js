(function () {
  const header = document.querySelector('[data-site-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-site-menu]');
  const themeToggle = document.querySelector('[data-theme-toggle]');

  const updateThemeControl = () => {
    if (!themeToggle) return;
    const darkTheme = document.documentElement.dataset.theme === 'dark';
    const nextTheme = darkTheme ? 'claro' : 'escuro';
    themeToggle.setAttribute('aria-label', `Ativar tema ${nextTheme}`);
    themeToggle.setAttribute('title', `Ativar tema ${nextTheme}`);
    const icon = themeToggle.querySelector('i');
    if (icon) icon.className = darkTheme ? 'fas fa-sun' : 'fas fa-moon';
  };

  updateThemeControl();

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const nextTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = nextTheme;
      try {
        localStorage.setItem('zeladorx.institutional.theme', nextTheme);
      } catch (error) {
        // The selected theme still applies when browser storage is unavailable.
      }
      updateThemeControl();
    });
  }

  if (header) {
    const updateHeader = () => header.classList.toggle('is-scrolled', window.scrollY > 12);
    updateHeader();
    window.addEventListener('scroll', updateHeader, { passive: true });
  }

  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      const icon = toggle.querySelector('i');
      if (icon) icon.className = open ? 'fas fa-times' : 'fas fa-bars';
    });
  }

  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }
})();