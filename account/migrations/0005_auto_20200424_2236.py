# Generated by Django 3.1.dev20200410100027 on 2020-04-24 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200424_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Аккаунт', 'verbose_name_plural': 'Аккаунты'},
        ),
    ]