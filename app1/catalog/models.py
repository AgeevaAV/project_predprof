from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User
from orders.models import Order

class Catalog(models.Model):
    name = models.CharField(verbose_name='Назавание',max_length=150, unique=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/', blank=True, null=True)
    structure = models.CharField(verbose_name='Состав',max_length=150, unique=None)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    breakfast_or_lunch = models.CharField(verbose_name='Тип: завтрак или обед',max_length=10)
    fish = models.BooleanField(verbose_name='Аллерген на рыбу', default=False)
    chicken =  models.BooleanField(verbose_name='Аллерген на курицу', default=False)
    lactose =  models.BooleanField(verbose_name='Аллерген на лактозу', default=False)
    class Meta:
        db_table = 'menu'
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    def __str__(self):
        return self.name
class Box(models.Model):
    name = models.CharField(verbose_name='Назавание',max_length=150, unique=True)
    count1 = models.PositiveIntegerField(verbose_name='Количество дней')
    image = models.ImageField(verbose_name='Фотография', upload_to='images/', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Стоимость')

    class Meta:
        db_table = 'box'
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'
    
    def __str__(self):
        return self.name
class BuyBox(models.Model):
    name = models.CharField(verbose_name='Назавание',max_length=150)
    count1 = models.PositiveIntegerField(verbose_name='Количество дней')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField()
    end_box = models.DateTimeField()

    created_at_lunch = models.DateField(blank=True, null=True)
    created_at_breakfast = models.DateField(blank=True, null=True)
    class Meta:
        db_table = 'buybox'
        verbose_name = 'Купленные наборы'
        verbose_name_plural = 'Купленные наборы'
    
    def __str__(self):
        return self.name
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name="Блюдо")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )
    created_at = models.DateTimeField(verbose_name="Дата оценки")

    class Meta:
        db_table = 'rating'
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
    
    def __str__(self):
        return self.user.name
    
