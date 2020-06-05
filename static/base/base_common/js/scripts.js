////Перезагрузка страницы при изменение размера окна
//var s_win_w = $(window).width();
//$(window).resize(function () {
//    win_w = $(window).width();
//    if (win_w >= s_win_w * 1.3 || win_w <= s_win_w * 0.7) {
//        location.reload();
//    }
//});

//Уменьшение шапки пи скроле вниз
$(window).scroll(function () {
    if ($(this).scrollTop() > 1 && $(window).width() > 769) {
        $('header').addClass("header-resize");
    } else {
        $('header').removeClass("header-resize");
    }
});

//Геренация случайного цвета подсветки
var colors = ['#FF283F', 'rgba(233, 33, 243, 1)', 'rgba(25, 212, 247, 1)'];
randomColor = colors[Math.random() * colors.length ^ 0];
document.documentElement.style.setProperty('--red', randomColor);


//Построен документ(DOM) и загружены все скрипты
$(document).ready(function () {
    console.log('\x1b[33m%s\x1b[0m', 'Остановитесь');

    //анимация кнопки поиска
    $('.header-search-button').mouseenter(function () {
        $(this).css("transform", "rotate(180deg)");
    })
    $('.header-search-button').mouseleave(function () {
        $(this).css("transform", "rotate(360deg)");
    })

    //Логика сообщений
    function messages() {
        if ($('.messages li').hasClass('messages-item')) {
            $('.bell').toggleClass('bell-active');
            $('.messages').toggleClass('messages-active');
            $('.header-about').toggleClass('header-about-min');
            setTimeout(function () {
                $('.bell').toggleClass('bell-active');
                $('.messages').toggleClass('messages-active');
                $('.header-about').toggleClass('header-about-min');
            }, 4000);
        }
    }

    messages();

    //Закрытие модального окна
    function alert_close() {
        setTimeout(function () {
            $('.alert').html(" ");
        }, 4000);
    }

    //Открытие сообщения модального окна
    function alert_open(text) {
        $('.alert').html(" ");
        $('.alert').append('<li class="messages-item alert-item">' + text + '</li>');
        messages();
        alert_close();
    }

    //Двежение кнопки открывающей меню
    $('.menu-active').click(function () {
        if ($(window).width() < 600) {
            $('body').toggleClass('lock');
            $('.username').toggleClass('none');
        }
        $(this).toggleClass('active');
        $('.main-menu').toggleClass('check');
        $('.content').toggleClass('resize');
        $('.header-buttons').toggleClass('buttons-active');
        $('.active-for-mobile').toggleClass('display-icons');
    })

    //Логика спойлеров 
    if ($(window).width() < 769) {
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


    //Логика окна корзины
    $('.shopping').click(function (e) {
        $('.shopping-list').slideToggle();
    })
    $('.close-basket').click(function () {
        $('.shopping-list').slideUp();
    })


    //Логика фильтров
    //Открытие блока фильтров
    $('.filter-main-title span').click(function () {
        $('.filter-main-title').toggleClass('active');
        $('.filter-container').toggleClass('active');
    })

    //Кастомый option
    $('.filter-select .filter-title').click(function () {
        $(this).toggleClass('active');
        $(this).next().toggleClass('active');
        console.log('клик');
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
                breakpoint: 600,
                settings: {
                    dots: false
                }
            }
        ]
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

    //Добавление товаров в корзину
    function basketUpdating(user_id, product_id, quantity_nbr, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.quantity_nbr = quantity_nbr;
        var csrf_token = $('#csrf_token input[name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        if (is_delete) {
            data["is_delete"] = true;
        }
        var url = form.attr('action');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK')
                if (data.product_total_quantity_nbr || data.product_total_quantity_nbr == 0) {
                    $('.shopping .counter').text(data.product_total_quantity_nbr);
                    $('.shopping-list-container').html(" ");
                    $.each(data.products, function (key, value) {
                        $('.shopping-list-container').
                        append('<tr class="shopping-item"><td>' + value.name + '</td><td>' + value.quantity_nbr + 'шт.</td><td>' + value.price_per_item * value.quantity_nbr + '</td><td class="shopping-list-delete" data-product_id="' + value.id + '" title="Удалить товар"></td></tr>');
                    })
                }
            },
            error: function () {
                console.log('error')
            }
        })
    }

    var form = $('#buyProduct');
    form.on('submit', function (e) {
        e.preventDefault();
        //Запретить добавить товар в корзину если товара нет на складе
        if ($('.warehouse').text() == 0) {
            alert_open('Товаров нет на складе');
        }
        //Запретить добавить товар в корзину если указан 0 или больше чем есть в наличии
        else if ($('input #quantity_nbr').val() == 0) {
            alert_open('Указано не правильное количество');
        }
        //Запретить добавить товар в корзину если указано больше чем есть на складе
        else if ($('input #quantity_nbr').val() >= $('.warehouse').text()) {
            alert_open('Указано больше чем есть на складе');
        } else {
            var user_id = $('.username_id').text(); //Получение id пользователя
            var quantity_nbr = $('#quantity_nbr').val(); //Получить количество товара которого хотят купить
            var addBasket = $('#addBasket'); //Получение кнопки отправки формы для считывания с неё data атрибутов
            var product_id = addBasket.data('product-id'); //Получение id продукта в бд

            basketUpdating(user_id, product_id, quantity_nbr, is_delete = false);

            alert_open('Товар добавлен в корзину');

        }
    })


    //Удаление товаров из коризы
    $(document).on('click', '.shopping-list-delete', function (e) {
        e.preventDefault();
        var user_id = $('.username_id').text(); //Получение id пользователя
        product_id = $(this).data("product_id");
        quantity_nbr = 0;
        basketUpdating(user_id, product_id, quantity_nbr, is_delete = true);
        $(this).closest('tr').remove();

        alert_open('Товар удален из корзины');
    })

    //Уведомление о том что товаров в корзине нет
    $('.add-order').click(function (e) {
        if ($('.shopping-list-container tr').hasClass('shopping-item')) {
            console.log('Товар в коризне');
        } else {
            e.preventDefault();
            alert_open('Товар в коризне нет');
        }
    })

    //Просмотр картинок в полном размере
    $('.slider-img').click(function () {
        $(this).clone() // сделаем копию картинки на которую было нажато
            .addClass("active-slider-img") // добавим этой копии класс активации
            .appendTo(".product-big-content"); // вставим измененный элемент в элемент для просмотра
        $("body").addClass("lock");
        $(".product-big").addClass("active-product-big");
    })
    $('.product-big-close').click(function () {
        $(".product-big-content").html('');
        $("body").removeClass("lock");
        $(".product-big").removeClass("active-product-big");
    })

    //Взамодействие с input number
    $(function () {
        (function quantityProducts() {
            var $quantityArrowMinus = $(".down-value");
            var $quantityArrowPlus = $(".up-value");

            $quantityArrowMinus.click(quantityMinus);
            $quantityArrowPlus.click(quantityPlus);

            function quantityMinus(e) {
                e.preventDefault();
                var $quantityNum = $(this).siblings('.input-number');
                if ($quantityNum.val() > 1) {
                    $quantityNum.val(+$quantityNum.val() - 1);
                }
            }

            function quantityPlus(e) {
                e.preventDefault();
                var $quantityNum = $(this).siblings('.input-number');
                $quantityNum.val(+$quantityNum.val() + 1);
            }
        })();
    });

    //Переключатель
    function shift(switch_item, switch_type, url) {
        if (switch_item == 'False') {
            switch_item = 'True';
        } else if (switch_item == 'True') {
            switch_item = 'False';
        }
        var data = {};
        var csrf_token = $('#csrf_token input[name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        data.switch_item = switch_item;
        data.switch_type = switch_type;
        
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function () {
                console.log('OK');
            },
            error: function () {
                console.log('error');
            }
        })
    }

    //Переключение сетки товаров
    $('.grid').click(function (e) {
        e.preventDefault();
        if ($('.header-container div').hasClass('username')) {
            var switch_item = $('.grid').data('grid');
            var url = $('.grid-link').attr('href');
            var switch_type = 'grid';
            shift(switch_item, switch_type, url);
            $('.main-product').toggleClass('change-grid');
            $('.grid').toggleClass('active-grid');
            $('.grid').data('grid', switch_item.grid_status);
        } else {
            $('.grid').toggleClass('active-grid');
            $('.main-product').toggleClass('change-grid');
        }
    })

    //Сена темы    
    //Переключение сетки товаров
    $('.theme').click(function (e) {
        if ($('.theme').hasClass('dark')) {
            $(this).removeClass('dark');
            $(this).addClass('light');
        } else {
            $(this).removeClass('light');
            $(this).addClass('dark');
        }
        e.preventDefault();
        var switch_item = $('.theme').data('theme');
        var url = $('.theme').attr('href');
        var switch_type = 'theme';
        shift(switch_item, switch_type, url);
        location.reload();
    })


    $(document).on('focus', ".auth-input input", function () {
        var input = $(this).closest('.auth-item').children('.auth-help');
        input.addClass('active');
    })

    $(document).on('blur', ".auth-input input", function () {
        var input = $(this).closest('.auth-item').children('.auth-help');
        input.removeClass('active');
    })

    setTimeout(function () {
        $('.auth-help').removeClass('active');
    }, 4000);

});

//Взаимодействие со свайпами
if ($(window).width() < 600) {
    jQuery('body').swipe({
        swipeStatus: function (event, phase, direction, distance, duration, fingerCount, fingerData, currentDirection) {
            if (phase == "start") {
                // сработает в начале swipe
            }
            if (phase == "end") {
                //сработает через 30 пикселей то число которое выбрали в threshold
                //Открытие меню при свайпах
                if (direction == 'left') {
                    $('body').toggleClass('lock');
                    $('.menu-active').toggleClass('active');
                    $('.main-menu').toggleClass('check');
                    $('.content').toggleClass('resize');
                    $('.header-buttons').toggleClass('buttons-active');
                    $('.active-for-mobile').toggleClass('display-icons');
                    $('.username').toggleClass('none');
                }
                //Закрытие меню при свайпае
                if (direction == 'right') {
                    $('body').toggleClass('lock');
                    $('.menu-active').toggleClass('active');
                    $('.main-menu').toggleClass('check');
                    $('.content').toggleClass('resize');
                    $('.header-buttons').toggleClass('buttons-active');
                    $('.active-for-mobile').toggleClass('display-icons');
                    $('.username').toggleClass('none');
                }
            }
        },
        triggerOnTouchEnd: false,
        threshold: 300 // сработает через 30 пикселей
    })
}
