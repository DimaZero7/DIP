from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')
    street = models.CharField(max_length=50, blank=True, verbose_name='Улица')
    number_house = models.CharField(max_length=50, blank=True, verbose_name='Номер дома')
    number_room = models.CharField(max_length=50, blank=True, verbose_name='Номер квартиры')
    photo = models.FileField(upload_to='users', blank=True, verbose_name='Фото профиля')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()