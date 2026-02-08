from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(verbose_name='Название продукта',max_length=150)
    weight = models.PositiveIntegerField(verbose_name='Количество в кг')