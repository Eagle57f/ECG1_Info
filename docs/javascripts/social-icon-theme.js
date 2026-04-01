(() => {
  const siteLinkSelector = '.md-social__link[href="https://eagle57f.github.io/"]';

  const updateIcon = () => {
    const siteLink = document.querySelector(siteLinkSelector);
    if (!siteLink) {
      return;
    }

    const svg = siteLink.querySelector('svg');
    if (!svg) {
      return;
    }

    const isDark = document.body?.getAttribute('data-md-color-scheme') === 'slate';
    svg.querySelectorAll('path').forEach((path) => {
      path.setAttribute('fill', isDark ? '#c0c2c6' : '#000000');
    });
  };

  const observeTheme = () => {
    updateIcon();

    const observer = new MutationObserver(updateIcon);
    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ['data-md-color-scheme'],
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', observeTheme, { once: true });
  } else {
    observeTheme();
  }
})();