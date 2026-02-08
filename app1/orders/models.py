from django.db import models
from django.conf import settings
# Create your models here.
class Order(models.Model):
    structure = models.CharField(verbose_name='Состав заказа',max_length=150)
    ready = models.BooleanField(verbose_name='Готов/нет', default=False)
    take_order = models.BooleanField(verbose_name='Забран ли', default=False)
    priceAll = models.PositiveIntegerField(verbose_name='Стоимость')
    count1 = models.PositiveIntegerField(verbose_name='Количество')
    breakfast_or_lunch = models.CharField(verbose_name='Тип: завтрак или обед',max_length=10)
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField()
    boxORnot = models.BooleanField(verbose_name='Набор ли', default=False) #Удалить
    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.structure

class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey('catalog.Catalog', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    breakfast_or_lunch1 = models.CharField(max_length=10)

    
    class Meta:
        unique_together = ['user', 'product']  
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"