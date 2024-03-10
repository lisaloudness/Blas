$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"}); // Hamburger Menu Collapse
    $('.carousel.carousel-slider').carousel({  // Menu Carousel
      fullWidth: true});
    $('.carousel').carousel();                // Menu Carousel
    $('select').formSelect();
    $('.collapsible').collapsible();
  });


// slider
var slider = document.getElementById('slider');
noUiSlider.create(slider, {
  start: [20, 80],
  connect: true,
  step: 1,
  orientation: 'horizontal', // 'horizontal' or 'vertical'
  range: {
    'min': 0,
    'max': 100
  },
  format: wNumb({
    decimals: 0
  })
 });

// Carousel 
var instance = M.Carousel.init({
  fullWidth: true
});

  