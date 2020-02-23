jQuery(document).ready(function () {
    /*Включение анимированного фона*/
    particlesJS.load('particles-js', '/static/base/common/js/config.json', function () {
        console.log('callback - particles.js config loaded');
    });
});

//    *******Скрипт шапки******
$(window).scroll(function () {
    if ($(this).scrollTop() > 1 && $(window).width() > 769) {
        $('header').addClass("header-resize");
    } else {
        $('header').removeClass("header-resize");
    }
});

//когда документ загружен
$(document).ready(function () {

    //анимация кнопки поиска
    $('.header-search-button').mouseenter(function () {
        $(this).css("transform", "rotate(180deg)");
    })
    $('.header-search-button').mouseleave(function () {
        $(this).css("transform", "rotate(360deg)");
    })
    $(window).resize(function () {
        if ($(window).width() > 500) {
            $('body').removeClass('lock');
        }
    });

    //Двежение кнопки открывающей меню
    $('.menu-active').click(function () {
        if ($(window).width() < 500) {
            $('body').toggleClass('lock');
        }
        $(this).toggleClass('active');
        $('.main-menu').toggleClass('check');
        $('.content').toggleClass('resize');
        $('.header-buttons').toggleClass('buttons-active');
        $('.active-for-mobile').toggleClass('display-icons');
    })

    //    Кнопки фильтра
    $('.filt-price').click(function () {
        $('.filt-date.button1').removeClass('active-filters');
        $('.filt-date.button2').removeClass('active-filters');
        $('.filt-rate.button1').removeClass('active-filters');
        $('.filt-rate.button2').removeClass('active-filters');
    })

    $('.filt-date').click(function () {
        $('.filt-price.button1').removeClass('active-filters');
        $('.filt-price.button2').removeClass('active-filters');
        $('.filt-rate.button1').removeClass('active-filters');
        $('.filt-rate.button2').removeClass('active-filters');
    })

    $('.filt-rate').click(function () {
        $('.filt-price.button1').removeClass('active-filters');
        $('.filt-price.button2').removeClass('active-filters');
        $('.filt-date.button1').removeClass('active-filters');
        $('.filt-date.button2').removeClass('active-filters');
    })

    $('.button1').click(function () {
        $(this).addClass('active-filters');
        $(this).next().removeClass('active-filters');
    })

    $('.button2').click(function () {
        $(this).addClass('active-filters');
        $(this).prev().removeClass('active-filters');
    })

    //    Взаимодействие со спойлерами
    if ($(window).width() <= '769') {
        console.log("окно меньше 769");
        $('.footer-block-title').click(function () {
            console.log("клик");
            $(this).toggleClass('footer-active').next().slideToggle(300);
        })
        $('.detail-li-title').click(function () {
            console.log("клик");
            $(this).toggleClass('detail-active').next().slideToggle(300);
        })
    } else {
        console.log("окно больше 769");
    }

    //    Слайдер на главной странице
    $('.slider').slick({
        //arrows:true, отображение стрелок
        dots: true, // активация точек
        //slidesToShow: 3, количество отображаемых слаййдов
        //slidesToScroll: 1, количество пролистываемых слайдов
        speed: 1000, // время анимации
        //easing: 'linear' тип анимации
        //infinite: false, бесконечное пролистывание
        //initialSlide: 2, начальный слайд
        autoplay: true, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        //draggable: true,  //Свайп для ПК
        //swipe:true,  Свайп для телефонов
        //waitForAnimate:false,Ускоренноя прокрутка слайдов стрелками
        //rows: 1, //количество рядов
        responsive: [
            {
                breakpoint: 500,
                settings: {
                    dots: false
                }
            }
        ]
    });

    $('.slider-min').slick({
        arrows: false, //отображение стрелок
        dots: false, // активация точек
        speed: 1000, // время анимации
        fade: true,
        autoplay: false, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        asNavFor: ".sub-slider-min"


    });
    $('.sub-slider-min').slick({
        arrows: true, //отображение стрелок
        dots: false, // активация точек
        slidesToShow: 3,
        speed: 1000, // время анимации
        autoplay: false, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        infinite: true, //бесконечное пролистывание
        asNavFor: ".slider-min",
        conterMode: true,
        focusOnSelect: true,

    });
});

//Добавление товаров в корзину
$(document).ready(function () {
    var form = $('#buyProduct');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var quantity_nbr = $('#quantity_nbr').val();
        console.log(quantity_nbr);
        var addBasket = $('#addBasket');
        var product_id = addBasket.data('product-id');
        var product_title = addBasket.data('product-title');
        var product_price = addBasket.data('product-price');
        console.log(product_id);
        console.log(product_title);

        var data = {};
        data.product_id = product_id;
        data.quantity_nbr = quantity_nbr;
        var csrf_token = $('#buyProduct [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr('action');

        console.log(data);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK')
                console.log('Цена')
                // /if(значение цены){
                //     $('.total-price').text(data.значение цены);
                // }
            },
            error: function () {
                console.log('error')
            }
        })


        $('.shopping-list-container').append('<tr class="shopping-item"><td>' + product_title + '</td><td>' + quantity_nbr + 'шт.</td><td>' + product_price + '</td><td class="shopping-list-delete" title="Удалить товар"></td></tr>');
    })

    $(document).on('click', '.shopping-list-delete', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })

    $(document).on('click', '.shopping-list-delete', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })

    $('.add-order').click(function () {
        if ($('.shopping-list-container tr').hasClass('shopping-item')) {
            console.log('Товар в коризне');
        } else {
            console.log('Товар в коризне нет');
            $('.alert').css('display', 'block');
        }
    })

    $('.alert-button').click(function () {
        $('.alert').css('display', 'none');
    })

});





//$( window ).resize(function () {
//    var bodyWidth = $('body').width();
//    if (bodyWidth < 769) {
//        console.log("окно меньше 769");
//        $('.footer-block-title').click(function () {
//            console.log("клик");
//            $(this).toggleClass('footer-active').next().slideToggle(300);
//        })
//        $('.detail-li-title').click(function () {
//            console.log("клик");
//            $(this).toggleClass('detail-active').next().slideToggle(300);
//        })
//    } else {
//        console.log("окно больше 769");
//    }
//});
