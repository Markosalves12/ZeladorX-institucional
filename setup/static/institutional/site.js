(function () {
  const header = document.querySelector('[data-site-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-site-menu]');
  const themeToggle = document.querySelector('[data-theme-toggle]');
  const progress = document.querySelector('[data-reading-progress]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const precisePointer = window.matchMedia('(pointer: fine)');

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

  const updateScrollEffects = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 12);
    if (progress) {
      const available = document.documentElement.scrollHeight - window.innerHeight;
      const ratio = available > 0 ? Math.min(window.scrollY / available, 1) : 0;
      progress.style.transform = `scaleX(${ratio})`;
    }
    if (!reducedMotion.matches) {
      document.documentElement.style.setProperty('--scroll-shift', `${Math.min(window.scrollY * 0.08, 70)}px`);
    }
  };
  updateScrollEffects();
  window.addEventListener('scroll', updateScrollEffects, { passive: true });

  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      const icon = toggle.querySelector('i');
      if (icon) icon.className = open ? 'fas fa-times' : 'fas fa-bars';
    });
  }

  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reducedMotion.matches) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const siblings = entry.target.parentElement ? Array.from(entry.target.parentElement.children) : [];
          const order = Math.max(0, siblings.indexOf(entry.target));
          entry.target.style.setProperty('--reveal-delay', `${Math.min(order * 70, 280)}ms`);
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }

  const hero = document.querySelector('[data-immersive-hero]');
  const tiltCard = document.querySelector('[data-tilt-card]');
  const parallaxLayers = document.querySelectorAll('[data-parallax]');
  if (hero && tiltCard && precisePointer.matches && !reducedMotion.matches) {
    let frame = 0;
    hero.addEventListener('pointermove', (event) => {
      if (frame) cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const bounds = hero.getBoundingClientRect();
        const x = (event.clientX - bounds.left) / bounds.width - 0.5;
        const y = (event.clientY - bounds.top) / bounds.height - 0.5;
        tiltCard.style.setProperty('--tilt-x', `${y * -7}deg`);
        tiltCard.style.setProperty('--tilt-y', `${x * 9}deg`);
        tiltCard.style.setProperty('--pointer-x', `${event.clientX - bounds.left}px`);
        tiltCard.style.setProperty('--pointer-y', `${event.clientY - bounds.top}px`);
        parallaxLayers.forEach((layer) => {
          const depth = Number(layer.dataset.depth || 0);
          layer.style.transform = `translate3d(${x * depth * 120}px, ${y * depth * 120}px, 0)`;
        });
      });
    });
    hero.addEventListener('pointerleave', () => {
      tiltCard.style.setProperty('--tilt-x', '0deg');
      tiltCard.style.setProperty('--tilt-y', '-4deg');
      parallaxLayers.forEach((layer) => { layer.style.transform = 'translate3d(0,0,0)'; });
    });
  }

  if (precisePointer.matches && !reducedMotion.matches) {
    document.querySelectorAll('[data-depth-surface]').forEach((surface) => {
      surface.addEventListener('pointermove', (event) => {
        const bounds = surface.getBoundingClientRect();
        const x = (event.clientX - bounds.left) / bounds.width - 0.5;
        const y = (event.clientY - bounds.top) / bounds.height - 0.5;
        surface.style.transform = `perspective(1000px) rotateX(${y * -2.5}deg) rotateY(${x * 3.5}deg) translateY(-4px)`;
      });
      surface.addEventListener('pointerleave', () => { surface.style.transform = ''; });
    });
  }
})();
