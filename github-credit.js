(() => {
  function updateGitHubCredit() {
    const link = document.querySelector('.credit');
    if (!link) return;

    if (link.href !== 'https://github.com/prajapatiiranjeet') link.href = 'https://github.com/prajapatiiranjeet';
    if (link.title !== 'GitHub profile: prajapatiiranjeet') link.title = 'GitHub profile: prajapatiiranjeet';
    if (link.getAttribute('aria-label') !== 'GitHub profile: prajapatiiranjeet') {
      link.setAttribute('aria-label', 'GitHub profile: prajapatiiranjeet');
    }
    if (link.hasAttribute('data-t-title')) link.removeAttribute('data-t-title');

    const icon = link.querySelector('.credit__x');
    if (icon) {
      icon.className = 'credit__github';
      icon.setAttribute('aria-hidden', 'true');
      icon.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .9a11.1 11.1 0 0 0-3.51 21.63c.55.1.76-.24.76-.54v-2.1c-3.1.68-3.76-1.32-3.76-1.32-.5-1.3-1.24-1.65-1.24-1.65-1.02-.7.08-.69.08-.69 1.13.08 1.73 1.16 1.73 1.16 1 .1.84 2.18 3.05 1.55.1-.72.4-1.2.7-1.48-2.48-.28-5.08-1.24-5.08-5.52 0-1.22.44-2.22 1.16-3-.12-.28-.5-1.42.1-2.96 0 0 .95-.3 3.06 1.15a10.65 10.65 0 0 1 5.57 0c2.12-1.45 3.06-1.15 3.06-1.15.61 1.54.23 2.68.11 2.96.72.78 1.15 1.78 1.15 3 0 4.3-2.6 5.24-5.09 5.51.4.34.76 1.01.76 2.04v3.03c0 .3.2.65.77.54A11.1 11.1 0 0 0 12 .9Z"/></svg>';
    }

    const username = link.querySelector('.credit__text b span');
    if (username && username.textContent !== 'prajapatiiranjeet') username.textContent = 'prajapatiiranjeet';
  }

  updateGitHubCredit();
  new MutationObserver(updateGitHubCredit).observe(document.getElementById('app') || document.body, {
    childList: true,
    subtree: true
  });
})();
