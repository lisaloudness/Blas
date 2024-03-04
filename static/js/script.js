$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"}); // Hamburger Menu Collapse
    $('.carousel.carousel-slider').carousel({  // Menu Carousel
      fullWidth: true});
    $('.carousel').carousel();                // Menu Carousel
  });



// Carousel 
var instance = M.Carousel.init({
  fullWidth: true
});

var instance = M.Carousel.getInstance(elem);
  