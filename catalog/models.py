from django.db import models
from django.shortcuts import reverse


def category_img_name(instance, filename):  # Функция состовлет путь для картинки категории
    return 'categorys/{0}/img/{1}'.format(instance.name, filename)


class Category(models.Model):  # Модель категорий товаров
    name = models.CharField(max_length=30)  # Имя категории
    slug = models.SlugField(max_length=30, unique=True)  # Человеко понятный url
    img = models.ImageField(upload_to=category_img_name)  # Кортинка категории

    def get_absolute_url(self):  # Создание персональной сылки для обекта
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):  # Модель товаров
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)  # Связь один ко многим(внешний ключ категории)
    name = models.CharField(max_length=50, verbose_name='Имя товара')  # Имя товара
    slug = models.SlugField(max_length=30, unique=True, verbose_name='URL товара', blank=True)  # Человеко понятный url
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')  # Дата добавления товара
    price = models.IntegerField(verbose_name='Цена')  # Цена товара
    warranty = models.IntegerField(verbose_name='Гарантия', help_text='месяцев')  # Гарантия товара
    country = models.CharField(max_length=50, verbose_name='Страна производитель')  # Производитель товара
    description = models.TextField(verbose_name='Описание')  # Описание товара
    specifications = models.TextField(verbose_name='Характеристики')  # Характеристики товара

    def get_absolute_url(self):  # Создание персональной сылки для обекта
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


def product_img_name(instance, filename):  # Функция состовлет путь для картинок товаров
    return 'products/{0}/img/{1}'.format(instance.products.slug, filename)


class ProductsImage(models.Model):  # Модель картинок товаров

    # Связь один ко многим(внешний ключ товаров)
    products = models.ForeignKey(Product,  related_name='prodimg', on_delete=models.CASCADE)

    img = models.ImageField(upload_to=product_img_name)  # Поле для загрзок картинок товаров




