'use strict';

const evidenceFilter = document.querySelector('#evidence-use');
const evidenceCards = [...document.querySelectorAll('#evidence-cards [data-use]')];
const evidenceCount = document.querySelector('#evidence-count');

function showMatchingEvidence() {
  let visible = 0;
  for (const card of evidenceCards) {
    card.hidden = Boolean(evidenceFilter.value) && card.dataset.use !== evidenceFilter.value;
    if (!card.hidden) visible += 1;
  }
  evidenceCount.textContent = visible === 1 ? '1 comparison' : `${visible} comparisons`;
}

evidenceFilter.addEventListener('change', showMatchingEvidence);
showMatchingEvidence();
evidenceFilter.closest('.evidence-tools').hidden = false;

const copyButton = document.querySelector('[data-copy]');
const copyStatus = document.querySelector('#copy-status');
const bibtex = document.querySelector(copyButton.dataset.copy);

copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(bibtex.textContent);
    copyStatus.textContent = 'BibTeX copied.';
  } catch {
    const range = document.createRange();
    range.selectNodeContents(bibtex);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    copyStatus.textContent = 'BibTeX selected. Use your copy shortcut.';
  }
});
