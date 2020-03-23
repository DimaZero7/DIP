jQuery(document).ready(function () {
    /*Включение анимированного фона*/
    particlesJS.load('particles-js', '/static/base/common/js/config.json', function () {
        console.log('callback - particles.js config loaded');
    });
});

//Перезагрузка страницы при изменение размера окна
var s_win_w = $(window).width();
$(window).resize(function () {
    win_w = $(window).width();
    if (win_w >= s_win_w * 1.3 || win_w <= s_win_w * 0.7) {
        location.reload();
    }
});

//Уменьшение шапки пи скроле вниз
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

    //Логика спойлеров 
    if ($(window).width() <= '769') {
        $('.spoilers').addClass('mobil');
    } else {
        $('.spoilers').removeClass('mobil');
    }
    
    $('.spoiler-active').click(function () {
        if ($('.spoilers').hasClass('mobil')) {
            $('.spoiler-active').not($(this)).removeClass('arrow-active');
            $('.spoiler-content').not($(this).next()).slideUp(300);
        }
        $(this).toggleClass('arrow-active').next().slideToggle(300);
    })


    //Слайдеры
    //Главный слайдер
    $('.slider').slick({
        dots: true, // активация точек
        speed: 1000, // время анимации
        autoplay: true, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        responsive: [
            {
                breakpoint: 500,
                settings: {
                    dots: false
                }
            }
        ]
        //arrows:true, отображение стрелок
        //slidesToShow: 3, количество отображаемых слаййдов
        //slidesToScroll: 1, количество пролистываемых слайдов
        //easing: 'linear' тип анимации
        //infinite: false, бесконечное пролистывание
        //initialSlide: 2, начальный слайд
        //draggable: true,  //Свайп для ПК
        //swipe:true,  Свайп для телефонов
        //waitForAnimate:false,Ускоренноя прокрутка слайдов стрелками
        //rows: 1, //количество рядов
    });

    //Сладйер на странице товара
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

    //Сладйер на странице товара вспомогательный
    $('.sub-slider-min').slick({
        arrows: true, //отображение стрелок
        dots: false, // активация точек
        //centerMode: true,
        slidesToShow: 3,
        speed: 1000, // время анимации
        autoplay: false, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        infinite: true, //бесконечное пролистывание
        asNavFor: ".slider-min",
        focusOnSelect: true,
    });

});

//Добавление товаров в корзину
$(document).ready(function () {
    var form = $('#buyProduct');
    console.log(form);
    counter = 0;
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

        $('.shopping').append('<span class="counter">' + counter + '</span>');
    })
    $(document).on('click', '.detail-add-basket', function (e) {
        counter = counter + 1;
    })


    $(document).on('click', '.shopping-list-delete', function (e) {
        e.preventDefault();
        $(this).closest('tr').remove();
        counter = counter - 1;
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
