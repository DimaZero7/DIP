# Generated by Django 3.1.dev20191227090824 on 2020-03-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200302_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=200, verbose_name='Текст комментария'),
        ),
    ]