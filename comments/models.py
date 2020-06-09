from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User


class Comment(models.Model):
    """Предстовление о коментарии"""

    product = models.ForeignKey(Product,  related_name='comment', on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, default = None, verbose_name='Пользователь')

    comment_text = models.TextField('Текст комментария', max_length=200)

    
    def __str__(self):
        return "Комментарий %s к товару %s" % (self.user.username, self.product.name)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

        