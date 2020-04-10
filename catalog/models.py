from django.db import models
from django.shortcuts import reverse


def category_img_name(instance, filename):
    """Фнкция состовляющая путь хранения картини категории"""

    return 'categories/{0}/img/{1}'.format(instance.slug, filename)


class Category(models.Model):
    """Категории товаров"""

    name = models.CharField('Название категории', max_length=30)

    slug = models.SlugField('URL категории', max_length=30, unique=True)

    img = models.ImageField('Картинка категории', upload_to=category_img_name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Создание персональной сылки на текущую категорию"""
        return reverse('catalog:category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
