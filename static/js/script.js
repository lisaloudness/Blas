$(document).ready(function(){
  $(".sidenav").sidenav({edge: "right"}); // Hamburger Menu Collapse
  $('.carousel.carousel-slider').carousel({  // Menu Carousel
    fullWidth: true});
  $('select').formSelect();
  $('.collapsible').collapsible();
  $('.tooltipped').tooltip();
  $('ul.tabs').tabs();
  $('#textarea1').val('New Text');
  $('.modal').modal();
  $('#textarea1').val('New Text');
});

//Dynamic create ingredient field on add_recipe form
$(document).ready(function () {
  var ingredient_ = 4; // initialize to 0

  var createInputs = function () {
      ingredient_++; // Increment on each click
      var inputHtml = '<div class="input-field col s6"><i class="material-icons prefix">local_dining</i><input type="text" id="ingredient_' + ingredient_ + '" name="ingredient_' + ingredient_ + '"><label for="ingredient_' + ingredient_ + '">Ingredient ' + ingredient_ + '</label></div>';
      $("#ip_div").append(inputHtml);
  };
  // Create form attributes for new ingredient
  $("#btn").click(function () {
      createInputs();
      $("#form")
    .find("input")
    .each(function (i) {
      $(this).attr("id", "ingredient_" + i);
      $(this).attr("placeholder", "ingredient_" + i);
      $(this).attr("name", "ingredient_" + i);
    });
  });
});
  
  