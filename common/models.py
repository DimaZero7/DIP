from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    message = models.TextField('Сообщение')
    date = models.DateTimeField('Дата добовления', auto_now_add=True)
    
