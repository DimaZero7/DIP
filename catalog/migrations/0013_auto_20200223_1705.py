# Generated by Django 3.1.dev20191227090824 on 2020-02-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200222_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='categorys'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Категория'),
        ),
    ]
