 $(document).ready(function(){
var steps = ['.res-step-one','.res-step-two','.res-step-three','.res-step-four'];
var pages = ['.res-form-one','.res-form-two','.res-form-three','.res-form-four'];
	var i = $('#step-no').val();
    if (i!=0){


            $('.res-form-one').css('left','150%')

    }
	$(document).ready(function(){
		var getClass = pages[i-1];
		$(".res-steps").removeClass('active');
		$(steps[i]).addClass('active');
		i++;
		if(getClass != ".res-form-four"){

				$(getClass).css('left', '150%');

			$(getClass).next().animate({
				left: '0%'
			}, 500, function(){
				$(this).css('display','block');
			});
		}
	});

	/* step back */


	/* click from top bar steps */







});