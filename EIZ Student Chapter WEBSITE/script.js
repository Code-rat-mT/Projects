/* =========================================
   Tabs & Home dropdown
   ========================================= */

function showTab(tabId, buttonElement) {
  const contents = document.querySelectorAll('.tab-content');
  const buttons = document.querySelectorAll('.tab-button');

  contents.forEach(c => c.classList.remove('active'));
  buttons.forEach(b => b.classList.remove('active'));

  const targetTab = document.getElementById(tabId);
  if (targetTab) targetTab.classList.add('active');
  if (buttonElement) buttonElement.classList.add('active');

  // Close the Home dropdown if it’s open
  const dd = document.getElementById('home-dropdown');
  if (dd) dd.style.display = 'none';
}

function setupRoadmap(navId) {
  const nav = document.getElementById(navId);
  if (!nav) return;

  const container = nav.closest('.content-wrapper')?.querySelector('.roadmap-content')
                 || document.getElementById('services-content')
                 || document.querySelector(`#${navId}`)?.closest('.tab-content')?.querySelector('.roadmap-content');
  if (!container) return;

  const sections = container.querySelectorAll('section');
  const defaultImage = container.querySelector('.default-image');
  const defaultSectionId = nav.querySelector('li.active')?.getAttribute('data-target');

  // Initial display
  sections.forEach(section => {
    const isDefault = (section.id === defaultSectionId);
    section.classList.toggle('active', isDefault);
    section.style.display = isDefault ? 'block' : 'none';
  });
  if (defaultImage) defaultImage.style.display = defaultSectionId ? 'none' : 'block';

  const items = nav.querySelectorAll('li');

  if (items.length > 0) {
    // List-based nav
    items.forEach(item => {
      item.addEventListener('click', () => {
        items.forEach(i => i.classList.remove('active'));
        item.classList.add('active');

        const targetId = item.getAttribute('data-target');

        sections.forEach(section => {
          section.classList.remove('active');
          section.style.display = 'none';
        });

        if (defaultImage) defaultImage.style.display = 'none';

        const targetElem = container.querySelector(`#${targetId}`);
        if (targetElem) {
          targetElem.classList.add('active');
          targetElem.style.display = 'block';
          targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  } else if (nav.tagName === 'SELECT') {
    // Dropdown nav
    nav.addEventListener('change', () => {
      const selectedValue = nav.value;
      sections.forEach(section => {
        section.classList.remove('active');
        section.style.display = 'none';
      });

      if (!selectedValue) {
        if (defaultImage) defaultImage.style.display = 'block';
      } else {
        if (defaultImage) defaultImage.style.display = 'none';
        const targetElem = container.querySelector(`#${selectedValue}`);
        if (targetElem) {
          targetElem.classList.add('active');
          targetElem.style.display = 'block';
          targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  }

  // Optional scroll sync
  container.addEventListener('scroll', () => {
    let currentActive = null;
    const scrollPosition = container.scrollTop + 30;

    sections.forEach(section => {
      if (section.offsetTop <= scrollPosition && section.style.display !== 'none') {
        currentActive = section.id;
      }
    });

    if (currentActive && items.length > 0) {
      items.forEach(i =>
        i.classList.toggle('active', i.getAttribute('data-target') === currentActive)
      );
      sections.forEach(section =>
        section.classList.toggle('active', section.id === currentActive)
      );
    }
  });
}

// Toggle dropdown visibility (Home)
function toggleDropdown(id) {
  const dropdown = document.getElementById(id);
  if (!dropdown) return;
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
}

// Show Home section content beside dropdown
function showHomeSection(sectionId) {
  const container = document.getElementById('home-content');
  if (!container) return;
  const sections = container.querySelectorAll('section');
  const defaultImage = container.querySelector('.default-image');

  sections.forEach(s => (s.style.display = 'none'));
  if (defaultImage) defaultImage.style.display = 'none';

  const dd = document.getElementById('home-dropdown');
  if (dd) dd.style.display = 'none';

  const target = document.getElementById(sectionId);
  if (target) {
    target.style.display = 'block';
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  } else if (defaultImage) {
    defaultImage.style.display = 'block';
  }
}

// Contact form submit handler
function handleFormSubmit(event) {
  event.preventDefault();
  const name = document.getElementById('name')?.value.trim();
  const email = document.getElementById('email')?.value.trim();
  const message = document.getElementById('message')?.value.trim();

  if (!name || !email || !message) {
    alert('Please fill all fields.');
    return false;
  }

  alert(`Thank you, ${name}! Your message has been sent.`);
  event.target.reset();
  return false;
}

/* =========================================
   Support – utilities
   ========================================= */

function setVisible(el, show) {
  if (!el) return;
  el.hidden = !show;
  el.style.display = show ? '' : 'none'; // override inline display:none if present
}

/* =========================================
   Support – main panels (financial / sponsor / mentor / resources)
   ========================================= */

function showSupportPanel(which) {
  // Hide all top-level support panels first
  ['financialBlock', 'panel-sponsor', 'panel-mentor', 'panel-resources']
    .forEach(id => setVisible(document.getElementById(id), false));

  if (!which) return;

  const targetId =
    which === 'financial' ? 'financialBlock' :
    which === 'sponsor'   ? 'panel-sponsor'   :
    which === 'mentor'    ? 'panel-mentor'    :
    which === 'resources' ? 'panel-resources' : '';

  if (!targetId) return;

  // Show the chosen panel
  setVisible(document.getElementById(targetId), true);

  // If not in financial, reset its sub-panels & radios
  if (which !== 'financial') {
    ['panel-momo','panel-bank','panel-paypal','panel-cash']
      .forEach(id => setVisible(document.getElementById(id), false));
    document.querySelectorAll('input[name="payMethod"]').forEach(r => (r.checked = false));
  }
}

/* =========================================
   Support – select handler
   ========================================= */

function handleSupportTypeChange(val) {
  const value = (val || '').trim();
  if (!value) {
    showSupportPanel(null);
    return;
  }
  showSupportPanel(value);
}

/* =========================================
   Support – financial: payment method panels
   ========================================= */

function handlePaymentMethodChange(method) {
  const panels = {
    momo:   'panel-momo',
    bank:   'panel-bank',
    paypal: 'panel-paypal',
    cash:   'panel-cash'
  };

  // hide all first
  Object.values(panels).forEach(id => setVisible(document.getElementById(id), false));

  // show selected
  setVisible(document.getElementById(panels[method]), true);

  // Optional: prefill demo bank “intent” link
  if (method === 'bank') {
    const amt = (document.getElementById('donationAmount')?.value || '').trim();
    const ref = (document.getElementById('donationRef')?.value || '').trim();
    const acc = (document.getElementById('bankAcc')?.textContent || '').trim();
    const link = document.getElementById('bankIntent');
    if (link) {
      link.href = `https://pay.google.com/gp/w/u/0/home/activity?amt=${encodeURIComponent(amt)}&ref=${encodeURIComponent(ref)}&acc=${encodeURIComponent(acc)}`;
    }
  }
}

/* =========================================
   Support – copy helpers + toast
   ========================================= */

function copyText(id) {
  const el = document.getElementById(id);
  if (!el) return;
  navigator.clipboard.writeText(el.textContent.trim())
    .then(() => toast('Copied!'))
    .catch(() => alert('Copy failed. Please copy manually.'));
}

function copyGroup(ids) {
  const list = Array.isArray(ids) ? ids : String(ids || '').split(',').map(s => s.trim()).filter(Boolean);
  const txt = list.map(key => {
    const node = document.getElementById(key);
    return `${key}: ${node ? node.textContent.trim() : ''}`;
  }).join('\n');
  navigator.clipboard.writeText(txt).then(() => toast('Bank details copied!'));
}

let toastTimer;
function toast(msg) {
  let t = document.getElementById('toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'toast';
    Object.assign(t.style, {
      position: 'fixed',
      bottom: '18px',
      left: '50%',
      transform: 'translateX(-50%)',
      padding: '10px 14px',
      background: '#111',
      color: '#fff',
      borderRadius: '8px',
      font: '500 14px/1 Poppins, sans-serif',
      zIndex: 9999,
      boxShadow: '0 8px 24px rgba(0,0,0,.25)',
      transition: 'opacity .25s ease'
    });
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.style.opacity = '1';
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => (t.style.opacity = '0'), 1600);
}

/* =========================================
   DOM ready
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {
  // Init any roadmap navs you might have
  ['services-roadmap', 'projects-roadmap', 'partners-roadmap', 'home-roadmap-select']
    .forEach(setupRoadmap);

  // Activate default tab
  const defaultTab = document.querySelector('.tabs .tab-button.active') || document.querySelector('.tabs .tab-button');
  if (defaultTab) {
    const tabId = defaultTab.getAttribute('data-tab')
               || defaultTab.getAttribute('onclick')?.match(/'([^']+)'/)?.[1];
    if (tabId) showTab(tabId, defaultTab);
  }

  // Support select init + change (works with inline onchange too)
  const select = document.getElementById('supportType');
  if (select) {
    // Wrap in .select-field if you’re using the pretty select CSS
    if (!select.parentElement.classList.contains('select-field')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'select-field';
      select.parentElement.insertBefore(wrapper, select);
      wrapper.appendChild(select);
    }
    handleSupportTypeChange(select.value || '');
    select.addEventListener('change', e => handleSupportTypeChange(e.target.value));
  }

  // Delegate payment method radios
  document.addEventListener('change', (e) => {
    const t = e.target;
    if (t && t.name === 'payMethod') handlePaymentMethodChange(t.value);
  });

  // Buttons that jump to Contact tab from support panels
  document.addEventListener('click', (e) => {
    const jump = e.target.closest('[data-tab-jump="contact"]');
    if (jump) {
      const contactBtn = Array.from(document.querySelectorAll('.tab-button'))
        .find(b => b.textContent?.toLowerCase().includes('contact'));
      showTab('contact', contactBtn);
    }
  });
});
