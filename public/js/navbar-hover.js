/**
 * Adani-style Nav Hover Indicator
 * Shared across all pages — matches index-2.html exactly
 */
(function () {
    var desktopWidth = 992;
    var header = document.querySelector(".adani-nav-fx");

    if (!header) {
        return;
    }

    var navList = header.querySelector(".navbar-nav");
    if (!navList) {
        return;
    }

    var indicator = null;
    var currentItem = null;

    function getTopLevelItems() {
        return Array.prototype.filter.call(navList.children, function (child) {
            return child.classList && child.classList.contains("nav-item");
        });
    }

    function getTopLevelLink(item) {
        return item ? item.querySelector(".nav-link") : null;
    }

    function ensureIndicator() {
        if (window.innerWidth < desktopWidth) {
            if (indicator) {
                indicator.style.opacity = "0";
            }
            return false;
        }

        if (!indicator) {
            indicator = document.createElement("span");
            indicator.className = "nav-hover-indicator";
            navList.appendChild(indicator);
        }

        return true;
    }

    function resolveCurrentItem() {
        var items = getTopLevelItems();

        items.forEach(function (item) {
            item.classList.remove("nav-current");
        });

        var path = window.location.pathname;

        // Detection logic
        currentItem = items.find(function (item) {
            // Check if any dropdown item is active
            var activeDropdownItem = item.querySelector(".dropdown-item.active");
            if (activeDropdownItem) {
                // User Request: index-2.html is NOT a services page for highlighting
                if (path.indexOf("index-2.html") !== -1 && item.textContent.trim().indexOf("Services") !== -1) {
                    return false;
                }
                return true;
            }
            return false;
        }) || items.find(function (item) {
            var link = getTopLevelLink(item);
            return link && link.classList.contains("active");
        }) || null;

        // Fallback: Default to "About Us" if no match found (or if we are on index-2.html)
        if (!currentItem || path.indexOf("index-2.html") !== -1) {
            currentItem = items.find(function (item) {
                return item.textContent.trim().indexOf("About Us") !== -1;
            }) || items[0];
        }

        if (currentItem) {
            currentItem.classList.add("nav-current");
        }
    }

    function moveIndicator(item) {
        if (!ensureIndicator()) {
            return;
        }

        var link = getTopLevelLink(item);
        if (!link) {
            indicator.style.opacity = "0";
            return;
        }

        var listRect = navList.getBoundingClientRect();
        var linkRect = link.getBoundingClientRect();
        var offset = linkRect.left - listRect.left;

        indicator.style.width = linkRect.width + "px";
        indicator.style.opacity = "1";
        indicator.style.transform = "translate3d(" + offset + "px, 0, 0) scale(1)";
    }

    function syncIndicator() {
        resolveCurrentItem();
        moveIndicator(currentItem);
    }

    function bindEvents() {
        getTopLevelItems().forEach(function (item) {
            item.addEventListener("mouseenter", function () {
                moveIndicator(item);
            });

            item.addEventListener("focusin", function () {
                moveIndicator(item);
            });
        });

        navList.addEventListener("mouseleave", function () {
            moveIndicator(currentItem);
        });

        navList.addEventListener("focusout", function () {
            window.requestAnimationFrame(function () {
                if (!navList.contains(document.activeElement)) {
                    moveIndicator(currentItem);
                }
            });
        });
    }

    function scheduleSync() {
        window.requestAnimationFrame(syncIndicator);
    }

    bindEvents();
    syncIndicator();

    window.addEventListener("load", scheduleSync);
    window.addEventListener("resize", scheduleSync);
    window.addEventListener("scroll", scheduleSync, { passive: true });

    if (window.ResizeObserver) {
        new ResizeObserver(scheduleSync).observe(navList);
    }
})();
