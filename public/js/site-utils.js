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
