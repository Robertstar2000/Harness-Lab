const filter = document.getElementById('filter');

if (filter) {
  filter.addEventListener('input', (event) => {
    const query = event.target.value.trim().toLowerCase();
    document.querySelectorAll('.download-list li').forEach((item) => {
      item.hidden = !item.textContent.toLowerCase().includes(query);
    });
  });
}

document.querySelectorAll('a[target="_blank"]').forEach((link) => {
  const rel = new Set((link.getAttribute('rel') || '').split(/\s+/).filter(Boolean));
  rel.add('noopener');
  rel.add('noreferrer');
  link.setAttribute('rel', [...rel].join(' '));
});
