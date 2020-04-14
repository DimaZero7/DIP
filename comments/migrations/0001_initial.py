# Generated by Django 3.1.dev20200410100027 on 2020-04-14 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Автор комментария')),
                ('comment_text', models.TextField(max_length=200, verbose_name='Текст комментария')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='products.product')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]