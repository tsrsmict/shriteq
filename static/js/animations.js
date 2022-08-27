  // https://stackoverflow.com/questions/27462306/css3-animate-elements-if-visible-in-viewport-page-scroll
  function callbackFunc(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("is-inViewport", entry.isIntersecting);
        }
    });
}

let options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.3
};

let observer = new IntersectionObserver(callbackFunc, options);
document.querySelectorAll('.cssanimation').forEach(el => observer.observe(el));