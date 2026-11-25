'use strict';

(function () {
  const esc = (s) =>
    String(s ?? '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');

  // 1. Scroll progress bar & active nav link
  const progBar = document.querySelector('.nav-prog');
  const navLinks = [...document.querySelectorAll('.nav-links a[href^="#"]')];
  const sections = navLinks
    .map((a) => document.querySelector(a.getAttribute('href')))
    .filter(Boolean);

  function onScroll() {
    if (progBar) {
      const doc = document.documentElement;
      const max = doc.scrollHeight - doc.clientHeight;
      const pct = max > 0 ? Math.min(100, Math.max(0, (window.scrollY / max) * 100)) : 0;
      progBar.style.width = `${pct.toFixed(1)}%`;
    }
    if (!sections.length) return;
    const y = window.scrollY + 120;
    let current = sections[0]?.id || '';
    for (const sec of sections) {
      if (!sec.hidden && sec.offsetTop <= y) current = sec.id;
    }
    for (const a of navLinks) {
      a.classList.toggle('active', a.getAttribute('href') === `#${current}`);
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // 2. Single-frame Figure Switcher & Lightbox (index.html)
  const figTabs = [...document.querySelectorAll('[data-fig-tab]')];
  const activeImg = document.querySelector('#active-fig-img');
  const activeWebp = document.querySelector('#active-fig-webp');
  const activeLink = document.querySelector('#active-fig-link');
  const activeCap = document.querySelector('#active-fig-cap');
  const activePdf = document.querySelector('#active-fig-pdf');
  const activeZoom = document.querySelector('#active-fig-zoom');

  const lightbox = document.querySelector('#fig-lightbox');
  const lbImg = document.querySelector('#lb-img');
  const lbTitle = document.querySelector('#lb-title');
  const lbCap = document.querySelector('#lb-cap');
  const lbPdf = document.querySelector('#lb-pdf');
  const lbClose = document.querySelector('#lb-close');
  const lbPrev = document.querySelector('#lb-prev');
  const lbNext = document.querySelector('#lb-next');

  let activeFigIndex = 0;

  function setActiveFigure(index) {
    if (!figTabs.length || !activeImg) return;
    activeFigIndex = (index + figTabs.length) % figTabs.length;
    const tab = figTabs[activeFigIndex];
    figTabs.forEach((t) => t.classList.toggle('active', t === tab));

    const { figNum, figSrc, figWebp, figPdf, figCap, figW, figH } = tab.dataset;
    activeImg.src = figSrc;
    activeImg.alt = figCap;
    if (figW && figH) {
      activeImg.width = Number(figW);
      activeImg.height = Number(figH);
    }
    if (activeWebp && figWebp) activeWebp.srcset = figWebp;
    if (activeLink) {
      activeLink.href = figSrc;
      activeLink.setAttribute('aria-label', `Inspect Figure ${figNum}`);
    }
    if (activePdf) activePdf.href = figPdf;
    if (activeCap) {
      const m = figCap.match(/^(Figure\s+\d+\s*\([^)]+\)\.)\s*(.*)$/);
      activeCap.innerHTML = m
        ? `<strong>${esc(m[1])}</strong> ${esc(m[2])}`
        : esc(figCap);
    }
  }

  function openLightbox(index) {
    if (!figTabs.length || !lightbox) return;
    const targetIdx = typeof index === 'number' ? index : activeFigIndex;
    setActiveFigure(targetIdx);
    const tab = figTabs[activeFigIndex];
    lbImg.src = tab.dataset.figSrc;
    lbImg.alt = tab.dataset.figCap;
    lbTitle.textContent = `Figure ${tab.dataset.figNum} of ${figTabs.length}`;
    lbCap.textContent = tab.dataset.figCap;
    lbPdf.href = tab.dataset.figPdf;
    lightbox.hidden = false;
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!lightbox || lightbox.hidden) return;
    lightbox.hidden = true;
    document.body.style.overflow = '';
  }

  figTabs.forEach((tab, idx) => {
    tab.addEventListener('click', () => setActiveFigure(idx));
  });
  activeLink?.addEventListener('click', (e) => {
    e.preventDefault();
    openLightbox(activeFigIndex);
  });
  activeZoom?.addEventListener('click', () => openLightbox(activeFigIndex));
  lbClose?.addEventListener('click', closeLightbox);
  lbPrev?.addEventListener('click', () => openLightbox(activeFigIndex - 1));
  lbNext?.addEventListener('click', () => openLightbox(activeFigIndex + 1));
  lightbox?.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (!lightbox || lightbox.hidden) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') openLightbox(activeFigIndex - 1);
    if (e.key === 'ArrowRight') openLightbox(activeFigIndex + 1);
  });

  // 3. BibTeX copy
  const copyBtn = document.querySelector('[data-copy]');
  const copyStatus = document.querySelector('#copy-status');
  if (copyBtn) {
    const target = document.querySelector(copyBtn.dataset.copy);
    copyBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(target.textContent);
        copyStatus.textContent = 'Copied to clipboard.';
      } catch {
        const range = document.createRange();
        range.selectNodeContents(target);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        copyStatus.textContent = 'Selected. Press Ctrl/Cmd+C.';
      }
      setTimeout(() => {
        if (copyStatus) copyStatus.textContent = '';
      }, 2800);
    });
  }

  // 4. Portal tabs on explorer.html (#evidence vs #benchmarks)
  const portalTabs = [...document.querySelectorAll('[data-portal-tab]')];
  const portalPanels = [...document.querySelectorAll('[data-portal-panel]')];
  function setPortalTab(name) {
    if (!portalTabs.length) return;
    portalTabs.forEach((t) => t.classList.toggle('active', t.dataset.portalTab === name));
    portalPanels.forEach((p) => {
      p.hidden = p.dataset.portalPanel !== name;
    });
    navLinks.forEach((a) => a.classList.toggle('active', a.getAttribute('href') === `#${name}`));
  }
  portalTabs.forEach((t) => {
    t.addEventListener('click', () => {
      const target = t.dataset.portalTab;
      setPortalTab(target);
      history.replaceState(null, '', `#${target}`);
    });
  });
  navLinks.forEach((a) => {
    if (portalTabs.length && (a.getAttribute('href') === '#evidence' || a.getAttribute('href') === '#benchmarks')) {
      a.addEventListener('click', () => setPortalTab(a.getAttribute('href').slice(1)));
    }
  });
  if (portalTabs.length && window.location.hash === '#benchmarks') {
    setPortalTab('benchmarks');
  }

  // 5. Load JSON datasets
  async function initData() {
    const hasCoverage = Boolean(document.querySelector('#cov-rows'));
    const hasExplorer = Boolean(document.querySelector('#comp-list'));
    const hasBenchmarks = Boolean(document.querySelector('#rt-list'));
    if (!hasCoverage && !hasExplorer && !hasBenchmarks) return;

    try {
      const requests = [];
      if (hasCoverage || hasExplorer) requests.push(fetch('assets/data/evidence.json').then((r) => r.json()));
      else requests.push(Promise.resolve(null));
      if (hasBenchmarks) requests.push(fetch('assets/data/benchmarks.json').then((r) => r.json()));
      else requests.push(Promise.resolve(null));

      const [evidence, benchmarks] = await Promise.all(requests);
      if (evidence) initCoverageAndExplorer(evidence);
      if (benchmarks) initBenchmarks(benchmarks);
    } catch (err) {
      const el = document.querySelector('#comp-list') || document.querySelector('#cov-rows');
      if (el) {
        el.innerHTML = `<div style="padding:20px;color:var(--crimson);">Failed to load data (${esc(err.message)}).</div>`;
      }
    }
  }

  function initCoverageAndExplorer(evidence) {
    const covRowsEl = document.querySelector('#cov-rows');
    const covTotalEl = document.querySelector('#cov-total-note');
    const isHomeMode = Boolean(document.querySelector('[data-cov-mode-root="home"]'));
    const modeBtns = [...document.querySelectorAll('[data-cov-mode]')];
    let strictMode = false;

    const searchEl = document.querySelector('#exp-search');
    const dirEl = document.querySelector('#exp-direction');
    const execOnlyEl = document.querySelector('#exp-exec-only');
    const compOnlyEl = document.querySelector('#exp-comp-only');
    const strictOnlyEl = document.querySelector('#exp-strict-only');
    const useTabs = [...document.querySelectorAll('#use-tabs [data-use]')];
    const countEl = document.querySelector('#exp-count');
    const listEl = document.querySelector('#comp-list');
    const toggleAllBtn = document.querySelector('#exp-toggle-all');
    const resetBtn = document.querySelector('#exp-reset');

    const params = new URLSearchParams(window.location.search);
    const validUses = new Set(['all', 'train', 'generate', 'plan', 'representation', 'assess', 'execute']);
    const initialUse = validUses.has(params.get('use')) ? params.get('use') : 'all';
    const initialStrict = params.get('strict') === '1';

    const state = {
      use: initialUse,
      query: '',
      direction: 'all',
      execOnly: false,
      compOnly: initialStrict,
      strictOnly: initialStrict,
      showAll: false,
      expandedId: null,
    };

    if (initialStrict) {
      if (compOnlyEl) compOnlyEl.checked = true;
      if (strictOnlyEl) strictOnlyEl.checked = true;
    }

    function renderCoverage() {
      if (!covRowsEl) return;
      const maxPapers = Math.max(...evidence.summary_by_use.map((u) => u.core_papers), 26);
      covRowsEl.innerHTML = evidence.summary_by_use
        .map((row) => {
          const compCount = strictMode ? row.sensitivity_papers : row.component_papers;
          const execPct = ((row.execution_papers / maxPapers) * 100).toFixed(1);
          const compPct = ((compCount / maxPapers) * 100).toFixed(1);
          const corePct = ((row.core_papers / maxPapers) * 100).toFixed(1);
          const bundledDiff = row.component_papers - row.sensitivity_papers;
          const diffBadge =
            strictMode && bundledDiff > 0
              ? ` <span style="color:var(--terra)">(−${bundledDiff})</span>`
              : '';
          return `
            <div class="cov-row" data-jump-use="${esc(row.use_key)}" title="Click to inspect ${esc(row.label)} studies">
              <div>
                <div class="cov-name">${esc(row.label)}</div>
                <div class="cov-dim">${esc(row.illus_dim)} · e.g., ${esc(row.illus_study)}</div>
              </div>
              <div class="cov-bar-track">
                <div style="position:absolute;left:0;top:0;bottom:0;width:${corePct}%;background:rgba(20,24,31,0.08);"></div>
                <div class="cov-bar-exec" style="width:${execPct}%"></div>
                <div class="cov-bar-comp" style="width:${compPct}%"></div>
              </div>
              <div class="cov-nums">
                <b>${row.core_papers}</b> core · <b>${row.execution_papers}</b> exec · <b>${compCount}</b> comp${diffBadge}
              </div>
            </div>
          `;
        })
        .join('');

      if (covTotalEl) {
        covTotalEl.innerHTML = strictMode
          ? `Sensitivity check: <b>26</b> papers with component tests (removed 4 bundled records: NavForesee ×2, NavThinker ×1, DreamAvoid ×1). Action generation 4 → 2; Execution 2 → 1.`
          : `Full set: <b>75</b> core papers · <b>56</b> execution outcomes · <b>29</b> component tests (30 records: 21 improve, 8 mixed, 1 worsens).`;
      }

      covRowsEl.querySelectorAll('[data-jump-use]').forEach((el) => {
        el.addEventListener('click', () => {
          const u = el.dataset.jumpUse;
          if (isHomeMode) {
            const q = new URLSearchParams({ use: u });
            if (strictMode) q.set('strict', '1');
            window.location.href = `explorer.html?${q.toString()}`;
            return;
          }
          state.use = u;
          if (strictMode) {
            state.compOnly = true;
            state.strictOnly = true;
            if (compOnlyEl) compOnlyEl.checked = true;
            if (strictOnlyEl) strictOnlyEl.checked = true;
          }
          syncUseTabs();
          renderExplorer();
          document.querySelector('#explorer')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      });
    }

    modeBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        strictMode = btn.dataset.covMode === 'strict';
        modeBtns.forEach((b) => b.classList.toggle('active', b === btn));
        renderCoverage();
      });
    });

    function syncUseTabs() {
      useTabs.forEach((t) => t.classList.toggle('active', t.dataset.use === state.use));
    }

    function renderExplorer() {
      if (!listEl) return;
      const q = state.query.trim().toLowerCase();
      const filtered = evidence.comparisons.filter((c) => {
        if (state.use !== 'all' && c.use !== state.use) return false;
        if (state.direction !== 'all' && c.direction !== state.direction) return false;
        if (state.execOnly && !c.downstream) return false;
        if (state.compOnly && !c.specific) return false;
        if (state.strictOnly && (!c.specific || c.bundled_omitted)) return false;
        if (q) {
          const hay = `${c.key} ${c.alias || ''} ${c.title} ${c.authors} ${c.use_label} ${c.comparison} ${c.result} ${c.endpoint} ${c.other_changes} ${c.locator} ${c.rationale || ''}`.toLowerCase();
          if (!hay.includes(q)) return false;
        }
        return true;
      });

      const uniquePapers = new Set(filtered.map((c) => c.key)).size;
      if (countEl) {
        countEl.innerHTML = `Showing <strong>${filtered.length}</strong> comparison${filtered.length === 1 ? '' : 's'} across <strong>${uniquePapers}</strong> unique paper${uniquePapers === 1 ? '' : 's'} (corpus: 93 / 75)`;
      }

      const PAGE_DEFAULT = 12;
      const limit = state.showAll ? filtered.length : PAGE_DEFAULT;
      const visible = filtered.slice(0, limit);

      if (!visible.length) {
        listEl.innerHTML = `<div style="padding:28px;text-align:center;color:var(--ink-mute);">No comparisons match the active filters.</div>`;
      } else {
        listEl.innerHTML = visible
          .map((c) => {
            const isOpen = state.expandedId === c.id;
            const dirClass = `badge-${c.direction}`;
            const compBadge = c.bundled_omitted
              ? `<span class="badge badge-bundled">Bundled (omitted in 26)</span>`
              : c.specific
                ? `<span class="badge badge-comp">Component test</span>`
                : c.downstream
                  ? `<span class="badge badge-use">Execution (coupled)</span>`
                  : `<span class="badge badge-use">Non-execution</span>`;
            return `
              <div class="comp-item">
                <button type="button" class="comp-summary" data-comp-id="${c.id}" aria-expanded="${isOpen}">
                  <div class="comp-paper-col">
                    <strong>${esc(c.authors || c.key)} (${esc(c.year || '—')})</strong>
                    <span>${c.alias ? `${esc(c.alias)} · ` : ''}${esc(c.key)} · #${c.id}</span>
                  </div>
                  <div><span class="badge badge-use">${esc(c.use_label)}</span></div>
                  <div class="comp-contrast-col">
                    ${esc(c.comparison)}
                    <span class="sub-title">${esc(c.title)}</span>
                  </div>
                  <div class="comp-flags-col">
                    <span class="badge ${dirClass}">${esc(c.direction)}</span>
                    ${compBadge}
                  </div>
                  <div class="comp-chevron">${isOpen ? '−' : '+'}</div>
                </button>
                <div class="comp-detail" ${isOpen ? '' : 'hidden'}>
                  <div class="comp-detail-grid">
                    <div class="detail-field"><b>Reported Result</b><p>${esc(c.result)}</p></div>
                    <div class="detail-field"><b>Endpoint &amp; Status</b><p>${esc(c.endpoint)} (${c.downstream ? 'Execution outcome' : 'Non-execution / proxy'})</p></div>
                    <div class="detail-field"><b>Co-varying Factors</b><p>${esc(c.other_changes)}</p></div>
                    <div class="detail-field"><b>Coding Note</b><p>${esc(c.granularity || (c.specific ? 'Qualifying component test' : 'Coupled / proxy'))}${c.rationale ? ` — ${esc(c.rationale)}` : ''}</p></div>
                  </div>
                  <div class="detail-footer">
                    <span class="mono" style="color:var(--ink-mute);">Source locator: ${esc(c.locator)}</span>
                    <a href="${esc(c.url)}" target="_blank" rel="noopener">Open primary source ↗</a>
                  </div>
                </div>
              </div>
            `;
          })
          .join('');

        listEl.querySelectorAll('[data-comp-id]').forEach((btn) => {
          btn.addEventListener('click', () => {
            const id = Number(btn.dataset.compId);
            state.expandedId = state.expandedId === id ? null : id;
            renderExplorer();
          });
        });
      }

      if (toggleAllBtn) {
        if (filtered.length <= PAGE_DEFAULT) {
          toggleAllBtn.hidden = true;
        } else {
          toggleAllBtn.hidden = false;
          toggleAllBtn.textContent = state.showAll
            ? `Collapse to first ${PAGE_DEFAULT}`
            : `Show all ${filtered.length} matching comparisons`;
        }
      }
    }

    useTabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        state.use = tab.dataset.use;
        state.showAll = false;
        syncUseTabs();
        renderExplorer();
      });
    });

    searchEl?.addEventListener('input', () => {
      state.query = searchEl.value;
      renderExplorer();
    });
    dirEl?.addEventListener('change', () => {
      state.direction = dirEl.value;
      renderExplorer();
    });
    execOnlyEl?.addEventListener('change', () => {
      state.execOnly = execOnlyEl.checked;
      renderExplorer();
    });
    compOnlyEl?.addEventListener('change', () => {
      state.compOnly = compOnlyEl.checked;
      if (!state.compOnly && state.strictOnly) {
        state.strictOnly = false;
        if (strictOnlyEl) strictOnlyEl.checked = false;
      }
      renderExplorer();
    });
    strictOnlyEl?.addEventListener('change', () => {
      state.strictOnly = strictOnlyEl.checked;
      if (state.strictOnly) {
        state.compOnly = true;
        if (compOnlyEl) compOnlyEl.checked = true;
      }
      renderExplorer();
    });
    toggleAllBtn?.addEventListener('click', () => {
      state.showAll = !state.showAll;
      renderExplorer();
    });
    resetBtn?.addEventListener('click', () => {
      state.use = 'all';
      state.query = '';
      state.direction = 'all';
      state.execOnly = false;
      state.compOnly = false;
      state.strictOnly = false;
      state.showAll = false;
      state.expandedId = null;
      if (searchEl) searchEl.value = '';
      if (dirEl) dirEl.value = 'all';
      if (execOnlyEl) execOnlyEl.checked = false;
      if (compOnlyEl) compOnlyEl.checked = false;
      if (strictOnlyEl) strictOnlyEl.checked = false;
      syncUseTabs();
      renderExplorer();
    });

    renderCoverage();
    syncUseTabs();
    renderExplorer();
  }

  function initBenchmarks(bm) {
    const tabBtns = [...document.querySelectorAll('[data-bench-tab]')];
    const panels = [...document.querySelectorAll('[data-bench-panel]')];
    tabBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        const target = btn.dataset.benchTab;
        tabBtns.forEach((b) => b.classList.toggle('active', b === btn));
        panels.forEach((p) => {
          p.hidden = p.dataset.benchPanel !== target;
        });
      });
    });

    // RoboTwin controls & list (12 default + Show all 33)
    const rtFilterEl = document.querySelector('#rt-filter');
    const rtSortEl = document.querySelector('#rt-sort');
    const rtListEl = document.querySelector('#rt-list');
    const rtToggleBtn = document.querySelector('#rt-toggle-all');
    let rtShowAll = false;

    function renderRoboTwin() {
      if (!rtListEl) return;
      const mode = rtFilterEl?.value || 'all';
      const sortBy = rtSortEl?.value || 'gap_desc';
      let rows = bm.robotwin.profiles.filter((p) => {
        if (mode === 'cotrain') return p.setting === 'cotrain';
        if (mode === 'single') return p.setting !== 'cotrain';
        return true;
      });
      rows = [...rows].sort((a, b) => {
        if (sortBy === 'gap_asc') return a.mean_gap_pp - b.mean_gap_pp;
        if (sortBy === 'declines_desc') return b.decline_tasks - a.decline_tasks || b.mean_gap_pp - a.mean_gap_pp;
        return b.mean_gap_pp - a.mean_gap_pp;
      });

      const RT_DEFAULT = 12;
      const visible = rtShowAll ? rows : rows.slice(0, RT_DEFAULT);

      rtListEl.innerHTML = visible
        .map((r) => {
          const decW = (r.decline_tasks / 50) * 100;
          const tieW = (r.tie_tasks / 50) * 100;
          const incW = (r.increase_tasks / 50) * 100;
          const gapSign = r.mean_gap_pp > 0 ? `−${r.mean_gap_pp.toFixed(1)}` : `+${Math.abs(r.mean_gap_pp).toFixed(1)}`;
          const gapClass = r.mean_gap_pp <= 0 ? 'pos' : 'neg';
          const tag = r.setting === 'cotrain' ? 'co-train' : 'single-task';
          return `
            <div class="rt-row">
              <div class="rt-model">${esc(r.model)} <small>(${tag})</small></div>
              <div class="rt-gap ${gapClass}">${gapSign} pp</div>
              <div class="rt-stack" title="${r.decline_tasks} decline / ${r.tie_tasks} tie / ${r.increase_tasks} improve">
                <div class="rt-seg-dec" style="width:${decW}%"></div>
                <div class="rt-seg-tie" style="width:${tieW}%"></div>
                <div class="rt-seg-inc" style="width:${incW}%"></div>
              </div>
              <div class="rt-counts">${r.decline_tasks}↓ · ${r.tie_tasks}= · ${r.increase_tasks}↑</div>
            </div>
          `;
        })
        .join('');

      if (rtToggleBtn) {
        if (rows.length <= RT_DEFAULT) {
          rtToggleBtn.hidden = true;
        } else {
          rtToggleBtn.hidden = false;
          rtToggleBtn.textContent = rtShowAll ? `Show top ${RT_DEFAULT}` : `Show all ${rows.length} configurations`;
        }
      }
    }
    rtFilterEl?.addEventListener('change', () => {
      rtShowAll = false;
      renderRoboTwin();
    });
    rtSortEl?.addEventListener('change', renderRoboTwin);
    rtToggleBtn?.addEventListener('click', () => {
      rtShowAll = !rtShowAll;
      renderRoboTwin();
    });
    renderRoboTwin();

    // RoboDojo capability bars
    const capEl = document.querySelector('#rd-capability-bars');
    if (capEl) {
      const wall = bm.robodojo.capability_comparison.find((x) => x.method.startsWith('WALL-OSS'));
      const vpp2 = bm.robodojo.capability_comparison.find((x) => x.method === 'VPP2');
      const dims = [
        { key: 'avg_sr', label: 'Overall Avg. SR' },
        { key: 'memory_sr', label: 'Memory' },
        { key: 'precision_sr', label: 'Precision' },
        { key: 'long_sr', label: 'Long-Horizon' },
        { key: 'gen_sr', label: 'Generalization' },
        { key: 'open_sr', label: 'Open' },
      ];
      capEl.innerHTML = dims
        .map((d) => {
          const vVal = vpp2[d.key];
          const wVal = wall[d.key];
          return `
            <div class="cap-row">
              <div class="cap-label">${esc(d.label)}</div>
              <div class="cap-bars">
                <div class="cap-bar-line">
                  <span class="mono">VPP2</span>
                  <div class="cap-track"><div class="cap-fill-vpp" style="width:${vVal.toFixed(1)}%"></div></div>
                  <span class="mono tnum">${vVal.toFixed(2)}%</span>
                </div>
                <div class="cap-bar-line">
                  <span class="mono">WALL-OSS</span>
                  <div class="cap-track"><div class="cap-fill-wall" style="width:${wVal.toFixed(1)}%"></div></div>
                  <span class="mono tnum">${wVal.toFixed(2)}%</span>
                </div>
              </div>
            </div>
          `;
        })
        .join('');
    }

    // RoboDojo 66 configs (15 default + Show all 66)
    const rdGridEl = document.querySelector('#rd-policy-grid');
    const rdToggleBtn = document.querySelector('#rd-toggle-all');
    let rdShowAll = false;
    function renderRdGrid() {
      if (!rdGridEl) return;
      const RD_DEFAULT = 15;
      const maxCells = Math.max(...bm.robodojo.profiles.map((p) => p.pos_score_zero_sr), 26);
      const list = rdShowAll ? bm.robodojo.profiles : bm.robodojo.profiles.slice(0, RD_DEFAULT);
      rdGridEl.innerHTML = list
        .map((p) => {
          const pct = ((p.pos_score_zero_sr / maxCells) * 100).toFixed(1);
          return `
            <div class="rd-policy-item">
              <div class="rd-policy-top">
                <strong>${esc(p.policy_key)}</strong>
                <span>${p.pos_score_zero_sr} / ${p.observed} cells</span>
              </div>
              <div class="rd-mini-bar"><div class="rd-mini-fill" style="width:${pct}%"></div></div>
            </div>
          `;
        })
        .join('');
      if (rdToggleBtn) {
        rdToggleBtn.textContent = rdShowAll
          ? `Show top ${RD_DEFAULT} configurations`
          : `Show all ${bm.robodojo.profiles.length} configurations`;
      }
    }
    rdToggleBtn?.addEventListener('click', () => {
      rdShowAll = !rdShowAll;
      renderRdGrid();
    });
    renderRdGrid();
  }

  initData();
})();
