from django.db import models

from products.models import Product
from django.contrib.auth.models import User
    
    
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, default=None,  verbose_name='Название статуса')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, default = None, verbose_name='Пользователь')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default = 0, verbose_name='Сумма заказа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    
    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)
        

class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, on_delete=models.CASCADE, null=True,  verbose_name='Заказ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, null=True,  verbose_name='Товар')
    price_per_item = models.IntegerField(default = 1, verbose_name='Цена за одну штуку')
    quantity_nbr = models.IntegerField(default = 1, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default = 0, verbose_name='Общая сумма')
    is_active = models.BooleanField(default=True, verbose_name='Состояние')
    
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
    
    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print (self.quantity_nbr)

        self.total_price = int(self.quantity_nbr) * price_per_item

        super(ProductsInOrder, self).save(*args, **kwargs)
        
    
class ProductsInBasket(models.Model):
    order = models.ForeignKey(Order, blank=True, on_delete=models.CASCADE, null=True,  verbose_name='Заказ')
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, default = None, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, null=True,  verbose_name='Товар')
    price_per_item = models.IntegerField(default = 1, verbose_name='Цена за одну штуку')
    quantity_nbr = models.IntegerField(default = 1, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default = 0, verbose_name='Общая сумма')
    is_active = models.BooleanField(default=True, verbose_name='Состояние')
    
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
    
    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.quantity_nbr)*self.product.price
        
        super(ProductsInBasket, self).save(*args, **kwargs)