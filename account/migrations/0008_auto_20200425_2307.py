# Generated by Django 3.1.dev20200410100027 on 2020-04-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200425_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_house',
            field=models.CharField(max_length=50, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_room',
            field=models.CharField(max_length=50, verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(upload_to='users', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Улица'),
        ),
    ]