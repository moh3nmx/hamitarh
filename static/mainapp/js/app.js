$( document ).ready(function() {



    //$(".button-collapse").sideNav({
    //    edge: 'right'
    //});
   // $(".button-collapse").sideNav('show');

    //$( ".draggable" ).draggable({
    //    connectToSortable: ".sortable",
    //    revert: "invalid"
    //});
    $(".card")
        .mouseenter(function() {
            $( this ).addClass('z-depth-1-half');
        })
        .mouseleave(function() {
            $( this ).removeClass('z-depth-1-half');
        });
    var temp = $(".circle-progress").html();
    $(".circle-progress").html("");
    for(var j = 1; j<= 150; j++){
        $(".circle-progress").append("<div class='wave'></div>");

    }
    $(".circle-progress").append(temp);


    $('ul.tabs').tabs();
    $('.carousel.carousel-slider').carousel({full_width: true});



    $('.parallax').parallax();

    $('select').material_select();
    //if($('#modal1').length) {
    //    $('#modal1').openModal();
    //}

    $(".button-collapse").click(function() {
        console.log('clicked');
        $('.side-nav.fixed.right-aligned').css('height','100%');
        $('.side-nav.fixed.right-aligned').css('height',$('.side-nav.fixed.right-aligned').css('height')-64);
        console.log($('.side-nav.fixed.right-aligned').css('height'));
        if (window.matchMedia('(max-width: 992px)').matches) {
            if($('.side-nav.fixed').css('transform') == 'matrix(1, 0, 0, 1, 0, 0)')
                $('.side-nav.fixed').css('transform','translateX(105%)');
            else
                $('.side-nav.fixed').css('transform','translateX(0%)');
        }
        else{

            $('.side-nav.fixed').css('transform','translateX(0%)');
        }
    });
    //$('.check_group').click(function() {
        //alert($('input[name="group"]+label:before').css('top'));
        //if ($('input[name="group"]~label:before').css('top') == '0' ) {
        //    alert("HI!");
        //    $('input[name="group_details"]').show();
        //}
        //else {
        //    $('input[name="group_details"]').hide();
        //}
    //});
    //$('.modal-trigger').leanModal();
    //$("select.city-position").select2({
    //    dir: "rtl",
    //    language: "fa",
    //    placeholder: "موقعیت"
    //});
    //$("select.category").select2({
    //    dir: "rtl",
    //    language: "fa"
    //});

    //$('.help~.card-help').mouseover().show();

    $('.mainbody .card-help').fadeIn();

    $('.card-help .close').click(function(){
        $('.card-help.popupcard').fadeOut();
    });

    //var range = document.getElementById('tax');
    //
    //noUiSlider.create(range,{
    //    start: [0, 1000000],
    //    step: 10000,
    //    connect: true,
    //    direction: 'rtl',
    //    range: {
    //        'min': 0,
    //        'max': 1000000
    //    }
    //});
    if($('.mainbody').length) {



        setTimeout(function () {
            $('.card-help.popupcard').fadeOut();
        }, 7000);




        $nextpageurl = $('#nextpageurl').html();
        $previouspageurl = $('#previouspageurl').html();
        //$('.carousel.carousel-slider').carousel({full_width: true});
        var sliderInterval = setInterval(function () {
            $.ajax($nextpageurl)
                .done(function ($data) {
                    //console.log( $data );

                    $('.slidered').fadeOut('normal',function(){
                        console.log("success");
                        $('.slidered').html($data);
                        $nextpageurl = $('#nextpageurl').html();
                        $previouspageurl = $('#previouspageurl').html();
                        $('.slidered').fadeIn();
                        console.log($nextpageurl);

                    });


                })
                .fail(function () {
                    console.log("error");
                })
                .always(function () {
                    console.log("complete");
                });


        }, 10000);


        $('.home-arraw.larrow').click(function(){
            clearInterval(sliderInterval);
            $.ajax($nextpageurl)
                .done(function ($data) {
                    //console.log( $data );

                    $('.slidered').fadeOut('normal',function(){
                        console.log("success");
                        $('.slidered').html($data);
                        $nextpageurl = $('#nextpageurl').html();
                        $previouspageurl = $('#previouspageurl').html();
                        $('.slidered').fadeIn();
                        console.log($nextpageurl);

                    });



                })
                .fail(function () {
                    console.log("error");
                })
                .always(function () {
                    console.log("complete");

                    sliderInterval = setInterval(function () {
                        $.ajax($nextpageurl)
                            .done(function ($data) {
                                //console.log( $data );

                                $('.slidered').fadeOut('normal',function(){
                                    console.log("success");
                                    $('.slidered').html($data);
                                    $nextpageurl = $('#nextpageurl').html();
                                    $previouspageurl = $('#previouspageurl').html();
                                    $('.slidered').fadeIn();
                                    console.log($nextpageurl);

                                });


                            })
                            .fail(function () {
                                console.log("error");
                            })
                            .always(function () {
                                console.log("complete");
                            });


                    }, 10000);
                });
        });
        $('.home-arraw.rarrow').click(function(){
            clearInterval(sliderInterval);
            $.ajax($previouspageurl)
                .done(function ($data) {
                    //console.log( $data );

                    $('.slidered').fadeOut('normal',function(){
                        console.log("success");
                        $('.slidered').html($data);
                        $nextpageurl = $('#nextpageurl').html();
                        $previouspageurl = $('#previouspageurl').html();
                        $('.slidered').fadeIn();
                        console.log($nextpageurl);

                    });


                })
                .fail(function () {
                    console.log("error");
                })
                .always(function () {
                    console.log("complete");

                    sliderInterval = setInterval(function () {
                        $.ajax($nextpageurl)
                            .done(function ($data) {
                                //console.log( $data );

                                $('.slidered').fadeOut('normal',function(){
                                    console.log("success");
                                    $('.slidered').html($data);
                                    $nextpageurl = $('#nextpageurl').html();
                                    $previouspageurl = $('#previouspageurl').html();
                                    $('.slidered').fadeIn();
                                    console.log($nextpageurl);

                                });


                            })
                            .fail(function () {
                                console.log("error");
                            })
                            .always(function () {
                                console.log("complete");
                            });


                    }, 10000);
                });
        });



    }




    //$('.carousel').carousel();


    $( "#column1, #column2, #column3" ).sortable({
        connectWith: ".sortable",
        items: ".draggable",
        handle: ".card-header",
        cursor: "move"
    }).disableSelection();
/*
    $( "#register_form" ).submit(function( event ) {
        //alert( "Handler for .submit() called." );
        $('input#email').val($('input#phone').val()+'@sarmayedari.ir');
        $('input#mellicode').val(0);
        //event.preventDefault();
        //$( "#register_form" ).submit();
    });
    $( "#login_form" ).submit(function( event ) {
        //alert( "Handler for .submit() called." );
        $('input#email').val($('input#email').val()+'@sarmayedari.ir');
        //$('input#mellicode').val(0);
        //event.preventDefault();
        //$( "#register_form" ).submit();
    });
*/

    $('.yn-modal-trigger .btn-submit[data-id]').click(function( event ) {
        //console.log($(this).data('id'));
        event.preventDefault();
        $('#modal_yn_accept').data('id', $(this).data('id'));
        $('#modal_yn').openModal();
        //alert($('#modal_yn_accept').data('id'));
    });
    $('#modal_yn_accept').click(function(){
        $('form.yn-modal-trigger[data-id="'+$(this).data('id')+'"]').submit();
    });


    $("table.dragsort tbody").sortable({
        items: "> tr",
        appendTo: "parent",
        helper: "clone",
        handle: "td:first",
        //change: function( event, ui ) {
        //    var sortedIDs = $(this).sortable( "toArray" , { attribute: 'data-id' } );
        //    console.log(sortedIDs);
        //}
    }).disableSelection();

    $( "table.dragsort tbody" ).on( "sortstop", function( event, ui ) {

        var sortedIDs = $(this).sortable( "toArray" , { attribute: 'data-id' } );
        //sortedIDs.forEach(function(currentValue,index,arr){
        //    sortedIDs[index] = currentValue+'_'+index;
        //});
        $('#reorder').val(sortedIDs.join());
        console.log(sortedIDs);
        console.log('---------------');

    } );
    if($.isFunction('froalaEditor')){
        $('#body').froalaEditor({
            direction: 'rtl',
            placeholderText: null
        });


        $("a[href='https://froala.com/wysiwyg-editor']").hide();

    }

    $( ".commify" ).on('keyup paste', function() {
        $(this).val(numberWithCommas($(this).val()));
    });
    for (x=0;x<$('span.fund').length;x++){
            $('span.fund')[x].innerHTML = numberWithCommas($('span.fund')[x].innerHTML);
    }


});

function numberWithCommas(x) {
    x = x.replace(/[^\/\d]/g,'');
    var parts = x.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    return parts.join(".");
}


//# sourceMappingURL=app.js.map
function checkRegisterForm() {
    a = 0;

    var email = $("input#email").val();
    if ($("[name=name]").val().length < 6) {
        $("div#name").addClass('red lighten-4 ');
        $('#name-validation').addClass('red-text');
        $('#name-validation').html('وارد کردن نام و نام خانوادگی اجباری است و باید حداقل شامل 6 کاراکتر باشد.');
    }
    if ($("[name=name]").val().length >= 6) {
        $("div#name").addClass('green lighten-4 ');
        $('#name-validation').html('');
        a = a + 1;
    }
    if ($("[name=phone]").val() == "" || $("[name=phone]").val().length<11 || $("[name=phone]").val().length>11) {
        $('#phone-validation').addClass('red-text');
        $('#phone-validation').html('شماره همراه را به شکل صحیح وارد کنید.');
        $("div#tel").addClass('red lighten-4 ');
    }
    if ($("[name=phone]").val() != "" && $("[name=phone]").val().length==11) {
        $("div#tel").addClass('green lighten-4 ');
        $('#phone-validation').html('');
        a = a + 1;
    }
    if ($("[name=password1]").val().length < 6) {
        $("div#password").addClass('red lighten-4 ');
        $("div#password2").addClass('red lighten-4 ');
        $("#password-validation").text("رمزعبور باید حداقل 6 کاراکتر باشد.");
            $("#password-validation").addClass('red-text ');
    }
    if ($("[name=password1]").val().length >= 6) {
        $("div#password").addClass('green lighten-4 ');
        $("#password-validation").text("");


        if ($("input#password2").val() != $("[name=password1]").val()) {

            $("div#password2").addClass('red lighten-4 ');
            $("#password-validation").text("تکارار رمزعبور با رمزعبور ورودی همخوانی ندارد.");
            $("#password-validation").addClass('red-text ');
        }
        if ($("input#password2").val() == $("[name=password1]").val()) {
            $("div#password2").addClass('green lighten-4 ');
            $("#password-validation").text("");
            a = a + 1;

        }
        }




    console.log('email');




        if (a == 3) {
            $('#error').html('');
            if (email == '' || validateEmail(email)) {
                $("#email-validation").text("");
                $("#email").addClass('green lighten-4 ');
                $('#error').addClass('green-text');
                $('#error').html('ثبت نام با موفقیت انجام شد.');
                $("#email-validation").text("");
                console.log($('input#password').length);
                setTimeout(function () {
                    $('#login_form_membership').submit();
                }, 1000);
            }
            if (!validateEmail(email)) {
                $("#email-validation").text("ایمیل وارد شده صحیح نیست!");
                $("#email-validation").addClass('red-text');
            }

            } else {
                $('#error').addClass('red-text');
                $('#error').html( 'اطلاعات خود را به شکل صحیح وارد کنید:') ;
            }



}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function createAdForm() {
    var str = $('#amount_number').val();
    // alert(parseInt(str.replace(",", "") , 10));
    $('input#amount_number').val(str.replace(/[^\d.-]/g, ''));
    // alert($('input#amount_number').val())
    // alert($('input#amount_number').val())
    $('#create-ad').submit();
}
function passwordCheck() {
    if ($('input#password').val().length < 6){
        $('#pass-error').html("رمز انتخابی باید حداقل 6 کاراکتر باشد.");
        
    }else {
        if ($('input#password').val() != $('input#password2').val()){
        // console.log()
        $('#pass-error').html("عدم تطابق ورودی ها")

        }else {
            $('#login_form_membership').submit();
        }
    }

}

function InvestFormCreate(){
    a = 0;
    if ($('#tabs-2 textarea[name=exe_outline]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=market_size]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=marketing_plan]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=present_customers]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=damage]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=compet]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=rate_of_return]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=benefit_share]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=usage]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=present_income]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=resume]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=credits]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=investor_share]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=costs]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 textarea[name=revenue_model]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 input[name=expected_gain]').val() != '' ){
        a = a + 1;
    }
    if ($('#tabs-2 input[name=expected_time]').val() != '' ){
        a = a + 1;
    }

    if (a==17){
        $('#form-msg').html("<p class='green-text' style='text-align: center'>باموفقیت ثبت شد!</p>");
        setTimeout(function () {
            $('#more_detail').submit();
        }, 600)
    }else{
         $('#form-msg').html("<p class='red-text' style='text-align: center'>جهت شروع فرایند جذب سرمایه باید تمامی اطلاعات این مرحله را وارد کنید!</p>");
    }


}