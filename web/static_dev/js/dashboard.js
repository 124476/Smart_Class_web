document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar
    const menuBar = document.querySelector('.content nav .bx-menu');
    const sideBar = document.querySelector('.sidebar');

    if (menuBar && sideBar) {
        menuBar.addEventListener('click', function() {
            sideBar.classList.toggle('close');
        });
    }

    // Active menu item
    const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');

    sideLinks.forEach(item => {
        item.addEventListener('click', function() {
            sideLinks.forEach(i => {
                i.parentElement.classList.remove('active');
            });
            this.parentElement.classList.add('active');
        });
    });

    // Search toggle for mobile
    const searchBtn = document.querySelector('.content nav form .form-input button');
    const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
    const searchForm = document.querySelector('.content nav form');

    if (searchBtn && searchBtnIcon && searchForm) {
        searchBtn.addEventListener('click', function(e) {
            if (window.innerWidth < 576) {
                e.preventDefault();
                searchForm.classList.toggle('show');
                if (searchForm.classList.contains('show')) {
                    searchBtnIcon.classList.replace('bx-search', 'bx-x');
                } else {
                    searchBtnIcon.classList.replace('bx-x', 'bx-search');
                }
            }
        });
    }

    // Theme toggle
    const toggler = document.getElementById('theme-toggle');

    if (toggler) {
        toggler.addEventListener('change', function() {
            if (this.checked) {
                document.body.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            } else {
                document.body.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // Check saved theme preference
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark');
        if (toggler) toggler.checked = true;
    }

    // Responsive adjustments
    window.addEventListener('resize', function() {
        if (window.innerWidth < 768) {
            if (sideBar) sideBar.classList.add('close');
        } else {
            if (sideBar) sideBar.classList.remove('close');
        }

        if (window.innerWidth > 576) {
            if (searchBtnIcon) searchBtnIcon.classList.replace('bx-x', 'bx-search');
            if (searchForm) searchForm.classList.remove('show');
        }
    });

    // Initialize with correct state
    if (window.innerWidth < 768 && sideBar) {
        sideBar.classList.add('close');
    }
});