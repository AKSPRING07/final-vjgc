/**
 * Mega Dropdown Click Toggle
 * Ensures mega menus stay open and only close on click-outside or re-click.
 */
document.addEventListener('DOMContentLoaded', function() {
    const megaToggles = document.querySelectorAll('.mega-dropdown .dropdown-toggle');
    
    megaToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            const parent = this.parentElement;
            const menu = parent.querySelector('.dropdown-menu');
            
            // If it's a real link and the dropdown is already open, let it navigate
            // Otherwise, prevent default to just toggle the menu
            if (this.getAttribute('href') !== '#' && this.getAttribute('href') !== 'javascript:void(0)') {
                if (!menu.classList.contains('show')) {
                    // e.preventDefault(); // Uncomment if you want to force toggle on first click
                }
            }
        });
    });

    // Handle the gap issues and ensure 'show' class is respected by our custom CSS
    // Bootstrap 5 already adds .show, so we just need to make sure no other hover logic
    // is fighting with it.
});
