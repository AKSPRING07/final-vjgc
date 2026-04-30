$(function() {
    "use strict";

    // ------------------------ Blog Slider
    if ($(".vjs-blog-slider").length) {
        $('.vjs-blog-slider').slick({
            dots: false,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 5000,
            slidesToShow: 2,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1
                    }
                }
            ]
        });
    }
});

// ============================================================
// Vijayalakshmi Group - Global Site Utilities
// (Accessibility, Translation, and Persisted Settings)
// ============================================================

// Mode Logic (Light/Dark)
function vjsSetMode(mode) {
    if (mode === 'dark') {
        document.body.classList.add('vjs-dark-mode');
        localStorage.setItem('vjs-theme-mode', 'dark');
    } else {
        document.body.classList.remove('vjs-dark-mode');
        localStorage.setItem('vjs-theme-mode', 'light');
    }
}

// Font Size Logic
function vjsSetFontSize(size) {
    document.documentElement.classList.remove('vjs-font-small', 'vjs-font-normal', 'vjs-font-large');
    document.documentElement.classList.add('vjs-font-' + size);
    localStorage.setItem('vjs-font-size', size);
}

// Reset Settings
function vjsResetSettings() {
    vjsSetMode('light');
    vjsSetFontSize('normal');
    localStorage.clear();
}

// Google Translate Integration
function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'ta,en,hi',
        autoDisplay: false
    }, 'google_translate_element');
}

function translateTo(langCode) {
    const select = document.querySelector('select.goog-te-combo');
    if (select) {
        select.value = langCode;
        select.dispatchEvent(new Event('change'));
        
        // Update labels
        const labels = { 'ta': 'TAM', 'en': 'ENG', 'hi': 'HIN' };
        const labelText = labels[langCode] || 'ENG';
        const langLabels = document.querySelectorAll('.vjs-lang-label');
        langLabels.forEach(el => el.textContent = labelText);
    }
}

// Initialize Settings on Load
document.addEventListener('DOMContentLoaded', function() {
    const savedMode = localStorage.getItem('vjs-theme-mode');
    const savedSize = localStorage.getItem('vjs-font-size');
    
    if (savedMode) vjsSetMode(savedMode);
    if (savedSize) vjsSetFontSize(savedSize);
});
