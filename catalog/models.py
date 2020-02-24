from django.db import models
from django.shortcuts import reverse

class Manufacture(models.Model): #Модель производителей
    name = models.CharField(max_length=15, verbose_name='Название компании') #Имя производителя
    img = models.ImageField(upload_to='manufacturer', help_text='500x500px', verbose_name='Логотип компании')#Логотип производителей
    country = models.CharField(max_length=60, verbose_name='Страна производитель')  #Страна произвродителя
  
    #Название модели для понимания человеком
    class Meta:
        verbose_name='Производитель'
        verbose_name_plural='Производители'

    def __str__(self):
        return self.name
    


def category_img_name(instance, filename):  # Функция состовлет путь для картинки категории
    return 'categorys/{0}/img/{1}'.format(instance.name, filename)


class Category(models.Model):  # Модель категорий товаров
    name = models.CharField(max_length=30, verbose_name='Название')  # Имя категории
    slug = models.SlugField(max_length=30, unique=True)  # Человеко понятный url
    img = models.ImageField(upload_to='categorys', verbose_name='Изображение')  # Кортинка категории

    #Название модели для понимания человеком
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def get_absolute_url(self):  # Создание персональной сылки для обекта
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):  # Модель товаров
    # Связь один ко многим(внешний ключ категории)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # Связь один ко многим(внешний ключ производителя)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, verbose_name='Производитель') 
    name = models.CharField(max_length=50, verbose_name='Имя товара')  # Имя товара
    slug = models.SlugField(max_length=30, unique=True, verbose_name='URL товара', blank=True)  # Человеко понятный url
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')  # Дата добавления товара
    price = models.IntegerField(verbose_name='Цена')  # Цена товара
    warehouse = models.IntegerField(verbose_name='Количество товара', help_text='шт.')  # Количество товара
    warranty = models.IntegerField(verbose_name='Гарантия', help_text='месяцев')  # Гарантия товара
    description = models.TextField(verbose_name='Описание')  # Описание товара
    specifications = models.TextField(verbose_name='Характеристики')  # Характеристики товара
    complect = models.TextField(verbose_name='Комплект поставки')  # Комплект поставки
    
    
    #Тебе нужно вывести только эти товары в слайдер на главнной странице
#    action = models.BooleanField(verbose_name='Акционный товар?') # Проверка акционности товара
#    poster = models.ImageField(upload_to='poster', help_text='700x200px', verbose_name='Акционный постер') # Постер акции

    #Название модели для понимания человеком
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def get_absolute_url(self):  # Создание персональной сылки для обекта
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


def product_img_name(instance, filename):  # Функция состовлет путь для картинок товаров
    return 'products/{0}/img/{1}'.format(instance.products.slug, filename)


class ProductsImage(models.Model):  # Модель картинок товаров

    #Название модели для понимания человеком
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
    
    
    # Связь один ко многим(внешний ключ товаров)
    products = models.ForeignKey(Product,  related_name='prodimg', on_delete=models.CASCADE)

    img = models.ImageField(upload_to=product_img_name)  # Поле для загрузки картинок для товаров

