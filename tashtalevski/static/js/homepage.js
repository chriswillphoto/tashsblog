// homepage elements
(function() {
  const quad = document.getElementsByClassName("quadtriptych")[0];
  const aboutText = document.getElementsByClassName("about-text")[0];
  let fadedIn = {
    quad: false,
    aboutText: false
  };

  window.addEventListener("scroll", function() {
    if (!fadedIn.quad && window.scrollY / quad.offsetTop > 0.3) {
      quad.classList = quad.classList + " loaded";
      fadedIn = { ...fadedIn, quad: true };
      console.log(fadedIn);
    }

    if (!fadedIn.aboutText && window.scrollY / (aboutText.getBoundingClientRect().top + window.scrollY) > 0.6) {
      aboutText.classList = aboutText.classList + " loaded";
      fadedIn = { ...fadedIn, aboutText: true };
      console.log(fadedIn)
    }
  });
})();
