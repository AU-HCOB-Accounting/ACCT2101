(function () {
  var chapters = [
    { file: 'intro.html', num: '', title: 'Introduction', short: 'Intro' },
    { file: 'ch01.html', num: '1', title: 'Accounting & the Business Environment', short: 'Ch 1' },
    { file: 'ch02.html', num: '2', title: 'Recording Business Transactions', short: 'Ch 2' },
    { file: 'ch03.html', num: '3', title: 'The Adjusting Process', short: 'Ch 3' },
    { file: 'ch04.html', num: '4', title: 'Completing the Accounting Cycle', short: 'Ch 4' },
    { file: 'ch05.html', num: '5', title: 'Merchandising Operations', short: 'Ch 5' },
    { file: 'ch06.html', num: '6', title: 'Merchandise Inventory', short: 'Ch 6' },
    { file: 'ch07.html', num: '7', title: 'Internal Control and Cash', short: 'Ch 7' },
    { file: 'ch08.html', num: '8', title: 'Receivables', short: 'Ch 8' },
    { file: 'ch09.html', num: '9', title: 'Plant Assets, Natural Resources, and Intangibles', short: 'Ch 9' },
    { file: 'ch11.html', num: '11', title: 'Current Liabilities', short: 'Ch 11' },
    { file: 'ch12.html', num: '12', title: 'Long-Term Liabilities', short: 'Ch 12' },
    { file: 'ch13.html', num: '13', title: "Stockholders' Equity", short: 'Ch 13' }
  ];

  var currentFile = location.pathname.split('/').pop() || 'index.html';

  function buildSidebar() {
    var sidebar = document.createElement('nav');
    sidebar.id = 'sidebar';
    sidebar.innerHTML = '<div id="sidebar-header">' +
      '<span class="sidebar-book-title">ACCT 2101</span>' +
      '<button id="sidebar-close" aria-label="Close navigation">&times;</button>' +
      '</div>' +
      '<ul id="sidebar-chapters"></ul>';

    var ul = sidebar.querySelector('#sidebar-chapters');

    chapters.forEach(function (ch) {
      var isCurrent = currentFile === ch.file;
      var li = document.createElement('li');
      li.className = 'sidebar-chapter' + (isCurrent ? ' active' : '');

      var a = document.createElement('a');
      a.href = ch.file;
      a.className = 'sidebar-chapter-link';
      a.innerHTML = (ch.num ? '<span class="sidebar-ch-num">Ch ' + ch.num + '</span>' : '<span class="sidebar-ch-num">Intro</span>') +
        '<span class="sidebar-ch-title">' + ch.title + '</span>';

      li.appendChild(a);

      if (isCurrent) {
        var sections = document.querySelectorAll('h2.section-title');
        if (sections.length > 0) {
          var subUl = document.createElement('ul');
          subUl.className = 'sidebar-sections';
          sections.forEach(function (h2) {
            if (!h2.id) {
              h2.id = 'sec-' + h2.textContent.trim().toLowerCase()
                .replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '').substring(0, 40);
            }
            var subLi = document.createElement('li');
            var subA = document.createElement('a');
            subA.href = '#' + h2.id;
            subA.className = 'sidebar-section-link';
            subA.textContent = h2.textContent.trim();
            subA.addEventListener('click', function (e) {
              e.preventDefault();
              h2.scrollIntoView({ behavior: 'smooth', block: 'start' });
              history.replaceState(null, '', '#' + h2.id);
              if (window.innerWidth < 1100) sidebar.classList.remove('open');
            });
            subLi.appendChild(subA);
            subUl.appendChild(subLi);
          });
          li.appendChild(subUl);
        }
      }

      ul.appendChild(li);
    });

    // Interactive tools (not chapters) — appears at the bottom of every page
    var toolLi = document.createElement('li');
    toolLi.className = 'sidebar-chapter sidebar-tool';
    var toolA = document.createElement('a');
    toolA.href = 'Accounting-Cycle-Simulators.html';
    toolA.target = '_blank';
    toolA.rel = 'noopener';
    toolA.className = 'sidebar-chapter-link';
    toolA.innerHTML = '<span class="sidebar-ch-num">Tool</span>' +
      '<span class="sidebar-ch-title">🔄 Cycle Simulators</span>';
    toolLi.appendChild(toolA);
    ul.appendChild(toolLi);

    document.body.insertBefore(sidebar, document.body.firstChild);

    var toggle = document.createElement('button');
    toggle.id = 'sidebar-toggle';
    toggle.setAttribute('aria-label', 'Open navigation');
    toggle.innerHTML = '<span></span><span></span><span></span>';
    document.body.appendChild(toggle);

    toggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
    });

    sidebar.querySelector('#sidebar-close').addEventListener('click', function () {
      sidebar.classList.remove('open');
    });

    document.addEventListener('click', function (e) {
      if (window.innerWidth < 1100 && sidebar.classList.contains('open') &&
          !sidebar.contains(e.target) && e.target !== toggle) {
        sidebar.classList.remove('open');
      }
    });

    highlightOnScroll(sidebar);
  }

  function highlightOnScroll(sidebar) {
    var sectionLinks = sidebar.querySelectorAll('.sidebar-section-link');
    if (sectionLinks.length === 0) return;

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          var scrollY = window.scrollY || window.pageYOffset;
          var current = null;
          var headings = document.querySelectorAll('h2.section-title');
          headings.forEach(function (h) {
            if (h.getBoundingClientRect().top <= 120) current = h.id;
          });
          sectionLinks.forEach(function (a) {
            a.classList.toggle('viewing', a.getAttribute('href') === '#' + current);
          });
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildSidebar);
  } else {
    buildSidebar();
  }
})();
