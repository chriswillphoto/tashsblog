(function(){

  let navBar = document.getElementById('nav')

  var lastScrollTop = 0;
  // element should be replaced with the actual target element on which you have applied scroll, use window in case of no target element.
  window.addEventListener("scroll", function(){ // or window.addEventListener("scroll"....
     var st = window.pageYOffset || document.documentElement.scrollTop; // Credits: "https://github.com/qeremy/so/blob/master/so.dom.js#L426"
     if (st > lastScrollTop){
         // downscroll code
         console.log('down')
         navBar.classList = 'hidden-nav'
     } else {
        // upscroll code
        console.log('up')
        navBar.classList = ""
     }
     lastScrollTop = st;
  }, false);


})()