$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"}); // Hamburger Menu Collapse
    $('.carousel.carousel-slider').carousel({  // Menu Carousel
      fullWidth: true});
    $('.carousel').carousel();                // Menu Carousel
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('ul.tabs').tabs();
    $('#textarea1').val('New Text');
   
  });



// Carousel 
var instance = M.Carousel.init({
  fullWidth: true
});

  