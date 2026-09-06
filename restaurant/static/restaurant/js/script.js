document.addEventListener('DOMContentLoaded', () => {
    // Menu Category Tabs logic
    const tabs = document.querySelectorAll('.menu-tab');
    const groups = document.querySelectorAll('.menu-items-group');
    const tabsWrapper = document.querySelector('.menu-tabs-wrapper');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            groups.forEach(g => g.style.display = 'none');

            tab.classList.add('active');
            const target = tab.getAttribute('data-target');
            const targetGroup = document.getElementById(target);
            if (targetGroup) {
                targetGroup.style.display = 'grid';
            }

            // Scroll selected tab into view smoothly on mobile
            if (tabsWrapper) {
                const tabLeft = tab.offsetLeft;
                const tabWidth = tab.offsetWidth;
                const wrapperWidth = tabsWrapper.offsetWidth;
                tabsWrapper.scrollTo({
                    left: tabLeft - (wrapperWidth / 2) + (tabWidth / 2),
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile Navigation Hamburger Toggle logic
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    const navOverlay = document.getElementById('nav-overlay');

    function toggleMenu() {
        if (hamburger && navLinks) {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
            if (navOverlay) navOverlay.classList.toggle('active');
            document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
        }
    }

    function closeMenu() {
        if (hamburger && navLinks) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            if (navOverlay) navOverlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    if (navOverlay) {
        navOverlay.addEventListener('click', closeMenu);
    }

    // Close mobile menu when clicking any nav link
    if (navLinks) {
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', closeMenu);
        });
    }
});
