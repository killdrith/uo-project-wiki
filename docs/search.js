const search = document.querySelector('#search');
search.addEventListener('input', () => {
  const terms = search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  let count = 0;
  document.querySelectorAll('nav a').forEach(link => {
    const body = wikiSearch[link.getAttribute('href')].toLowerCase();
    link.hidden = !terms.every(term => body.includes(term));
    if (!link.hidden) count++;
  });
  document.querySelector('#search-status').textContent = terms.length ? `${count} matching pages` : '';
});
