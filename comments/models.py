from django.db import models

from products.models import Product


class Comment(models.Model):
    """Предстовление о коментарии"""

    product = models.ForeignKey(Product,  related_name='comment', on_delete=models.CASCADE)

    comment_author = models.CharField('Автор комментария', max_length=50)

    comment_text = models.TextField('Текст комментария', max_length=200)

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
