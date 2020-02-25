from django.db import models
from django.shortcuts import reverse


class Manufacture(models.Model):  # Модель производителей
    name = models.CharField(max_length=15, verbose_name='Название компании')  # Имя производителя
    img = models.ImageField(upload_to='manufacturer',
                            help_text='500x500px', verbose_name='Логотип компании')  # Логотип производителей
    country = models.CharField(max_length=60, verbose_name='Страна производитель')  # Страна произвродителя

    def __str__(self):
        return self.name

    class Meta:  # Название модели для понимания человеком
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


def category_img_name(instance, filename):  # Функция состовлет путь для картинки категории
    return 'categorys/{0}/img/{1}'.format(instance.name, filename)


class Category(models.Model):  # Модель категорий товаров
    name = models.CharField(max_length=30, verbose_name='Название категории')  # Имя категории
    slug = models.SlugField(max_length=30, unique=True, verbose_name='понятный url')  # Человеко понятный url
    img = models.ImageField(upload_to='categorys', verbose_name='Кaртинка категории')  # Кaртинка категории

    def get_absolute_url(self):  # Создание персональной сылки для обекта
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:  # Название модели для понимания человеком
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


def poster_img_name(instance, filename):  # Функция состовлет путь для постера
    return 'products/{0}/img/poster/{1}'.format(instance.slug, filename)


class Product(models.Model):  # Модель товаров

    # Связь один ко многим(внешний ключ категории)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    # Связь один ко многим(внешний ключ производителя)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, verbose_name='Производитель')

    name = models.CharField(max_length=50, verbose_name='Имя товара')  # Имя товара
    slug = models.SlugField(max_length=30, unique=True, verbose_name='URL товара', blank=True)  # Человеко понятный url
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')  # Дата добавления товара
    price = models.IntegerField(verbose_name='Цена', help_text=' руб.')  # Цена товара
    warehouse = models.IntegerField(verbose_name='Количество товара', help_text='шт.')  # Количество товара
    warranty = models.IntegerField(verbose_name='Гарантия', help_text='месяцев')  # Гарантия товара
    description = models.TextField(verbose_name='Описание')  # Описание товара
    specifications = models.TextField(verbose_name='Характеристики')  # Характеристики товара
    set = models.TextField(verbose_name='Комплект поставки')  # Комплект поставки
    slider = models.BooleanField(verbose_name='Товар на слайдере', default=False)  # Будет ли товар в слайдере
    poster = models.ImageField(upload_to=poster_img_name, help_text='700x200px',
                               verbose_name='Картинка для постера')  # Постер товара

    def get_absolute_url(self):  # Создание персональной сылки для обекта
        return reverse('product_detail_url', kwargs={'slug': self.slug})
    # Название модели для понимания человеком
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    # from catalog.models import *
    # p = Product.objects.all()
    # t1 = p.get(name='товар 1')
    
    def __str__(self):
        return self.name



def product_img_name(instance, filename):  # Функция состовлет путь для картинок товаров
    return 'products/{0}/img/{1}'.format(instance.products.slug, filename)


class ProductsImage(models.Model):  # Модель картинок товаров

    # Связь один ко многим(внешний ключ товаров)
    products = models.ForeignKey(Product, related_name='prodimg', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=product_img_name)  # Поле для загрузки картинок для товаров
    # Название модели для понимания человеком
    
    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'

    
    
