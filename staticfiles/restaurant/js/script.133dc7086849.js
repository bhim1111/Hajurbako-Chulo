document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.menu-tab');
    const groups = document.querySelectorAll('.menu-items-group');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Hide all groups
            groups.forEach(g => g.style.display = 'none');

            // Add active class to clicked tab
            tab.classList.add('active');
            // Show the target group
            const target = tab.getAttribute('data-target');
            const targetGroup = document.getElementById(target);
            if (targetGroup) {
                targetGroup.style.display = 'grid';
            }
        });
    });
});
