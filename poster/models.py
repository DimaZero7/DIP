from django.db import models

from products.models import Product


def poster_img_name(instance, filename):
    """Состовлет путь для изображения постера"""

    return 'products/{0}/img/poster/{1}'.format(instance.product.slug, filename)


class Poster(models.Model):
    """Постер на главной"""

    # связь один к одному с товарами
    product = models.OneToOneField(Product, related_name='prodposter', on_delete=models.CASCADE)

    slider = models.BooleanField('Будет ли товар на слайдере?', default=False)

    img = models.ImageField('Изоброжение товара постере', upload_to=poster_img_name, help_text='700x200px')


