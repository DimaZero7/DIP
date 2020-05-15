from django.db import models
from django.shortcuts import reverse


def manufacture_img_name(instance, filename):
    """Функция состовлет путь для картинок производителей"""

    return 'manufacture/{0}/img/{1}'.format(instance.slug, filename)


class Manufacture(models.Model):
    """Производители товаров"""

    name = models.CharField('Название компании', max_length=30)
    slug = models.SlugField('URL производителя', max_length=30, unique=True)
    img = models.ImageField('Логотип компании', upload_to=manufacture_img_name, help_text='500x500px')
    country = models.CharField('Страна производитель', max_length=60)

    def get_absolute_url(self):
        """Создание персональной ссылки для экземпляра модели"""

        return reverse('manufacture:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'