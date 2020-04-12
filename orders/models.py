from django.db import models

from products.models import Product
 
class Orders(models.Model):
    session_key = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE, null=True,  verbose_name='Товар')
    price_per_item = models.IntegerField(default = 1, verbose_name='Цена за одну штуку')
    quantity_nbr = models.IntegerField(default = 1, verbose_name='Количество товара')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default = 0, verbose_name='Общая сумма за товар')
    is_active = models.BooleanField(default=True, verbose_name='Актиность товара в корзине')
    
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
    
    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.quantity_nbr)*self.product.price
        
        super(Orders, self).save(*args, **kwargs)