from django.db import models
    
class Feedback(models.Model):
    user = models.CharField(max_length=200, verbose_name='Пользователь')
    email = models.CharField(max_length=200, verbose_name='Почта пользователя')
    message = models.TextField('Текст комментария', max_length=200)
    date = models.DateTimeField('Дата добовления', auto_now_add=True)

    def __str__(self):
        return "%s Сообщение от %s с текстом  %s" % (self.id, self.user, self.message)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

        