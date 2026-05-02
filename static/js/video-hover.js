/**
 * video-hover.js
 * Handles play/pause on hover for blog cards and other video elements.
 */

document.addEventListener('DOMContentLoaded', function() {
    const blogCards = document.querySelectorAll('.blog-meta-one');

    blogCards.forEach(card => {
        const video = card.querySelector('video');
        
        if (video) {
            // Ensure the video is paused initially (redundancy)
            video.pause();

            card.addEventListener('mouseenter', () => {
                // play() returns a promise to handle browsers that block autoplay/interrupted play
                const playPromise = video.play();
                
                if (playPromise !== undefined) {
                    playPromise.catch(error => {
                        console.log("Playback prevented by browser: ", error);
                    });
                }
            });

            card.addEventListener('mouseleave', () => {
                video.pause();
                // Optional: Uncomment below to reset video to start on leave
                // video.currentTime = 0;
            });
        }
    });
});
