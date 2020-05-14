from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_img_name(instance, filename):
    """Функция состовлет путь для картинок профиля"""

    return 'profile/{0}/img/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    city = models.CharField('Город', max_length=50, blank=True)
    street = models.CharField('Улица', max_length=50, blank=True)
    number_house = models.CharField('Номер дома', max_length=50, blank=True)
    number_room = models.CharField('Номер квартиры', max_length=50, blank=True)
    photo = models.FileField('Фото профиля', upload_to=profile_img_name, blank=True)

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
