# Generated by Django 3.1.dev20200410100027 on 2020-04-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200414_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsinbasket',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ'),
        ),
    ]
