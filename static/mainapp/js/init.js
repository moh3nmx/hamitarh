
$.noConflict();
(function($){
  $(function(){

    // $('.button-collapse').sideNav();

  $('.button-collapse').sideNav({
      menuWidth: 300, // Default is 300
      edge: 'right', // Choose the horizontal origin
      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens,
    }
  );

      $('.parallax').parallax();
      $('.slider').slider();

    $('.img-box-zoom div').hover(function () {
        $(this).find('.img-zoom').addClass('overlay');
        $(this).find('.project-card-detail').css('visibility','visible');
        $(this).find('.project-card-detail').css('opacity',1);

    },function () {
       $(this).find('.img-zoom').removeClass('overlay');
        $(this).find('.project-card-detail').css('visibility','hidden');
        $(this).find('.project-card-detail').css('opacity',0);

    });

    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

      $('.carousel').carousel({
            dist:-20,
            shift:10,
            padding:20

      });
      // setInterval(function () {
      //     $('.carousel').carousel('next');
      // } , 5000);


      $("a").on('click', function(event) {

          // Make sure this.hash has a value before overriding default behavior
          if (this.hash !== "") {
              // Prevent default anchor click behavior
              event.preventDefault();

              // Store hash
              var hash = this.hash;

              // Using jQuery's animate() method to add smooth page scroll
              // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
              $('html, body').animate({
                  scrollTop: $(hash).offset().top
              }, 800, function () {

                  // Add hash (#) to URL when done scrolling (default click behavior)
                  window.location.hash = hash ;
              });
          } // End if
      })
      var Show = false;
      $('.expand-btn').click(function () {

            if (!Show){
                $('.hidden-items').slideDown(1000);
                $('#expand-btn').removeClass('zmdi-caret-down');
                $('#expand-btn').addClass('zmdi-caret-up');
                Show = true;
            }else{
                $('.hidden-items').slideUp(1000);
                $('#expand-btn').removeClass('zmdi-caret-up');
                $('#expand-btn').addClass('zmdi-caret-down');
                Show = false;
            }
        })
     


  }); // end of document ready


})(jQuery); // end of jQuery name space

