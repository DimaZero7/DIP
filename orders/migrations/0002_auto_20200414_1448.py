# Generated by Django 3.1.dev20200410100027 on 2020-04-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=24, verbose_name='Название статуса'),
        ),
    ]