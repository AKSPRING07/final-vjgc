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
        var path = window.location.pathname;
        var fileName = path.split('/').pop();

        items.forEach(function (item) {
            item.classList.remove("nav-current");
        });

        // 1. Try to find item based on links within its dropdown or itself
        currentItem = items.find(function (item) {
            var links = item.querySelectorAll("a");
            for (var i = 0; i < links.length; i++) {
                var href = links[i].getAttribute("href");
                if (href && fileName && href.indexOf(fileName) !== -1 && fileName !== "") {
                    return true;
                }
            }
            return false;
        });

        // 2. Fallback for specific pages or when no match found
        if (!currentItem) {
            if (fileName === "index-2.html" || fileName === "") {
                // Default to first item (About Us) on Home Page if no other match
                currentItem = items.find(function (item) {
                    return item.textContent.trim().indexOf("About Us") !== -1;
                }) || items[0];
            }
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
                navList.classList.add("is-hovering");
                moveIndicator(item);
            });

            item.addEventListener("focusin", function () {
                navList.classList.add("is-hovering");
                moveIndicator(item);
            });
        });

        navList.addEventListener("mouseleave", function () {
            navList.classList.remove("is-hovering");
            moveIndicator(currentItem);
        });

        navList.addEventListener("focusout", function () {
            window.requestAnimationFrame(function () {
                if (!navList.contains(document.activeElement)) {
                    navList.classList.remove("is-hovering");
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
