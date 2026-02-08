from django.db import models

# Create your models here.
class Applications(models.Model):

    product = models.CharField(verbose_name='Назавание продукта',max_length=100)
    weight = models.FloatField(verbose_name='Количество(кг)')
    fast = models.BooleanField(verbose_name='Срочность')
    aggre_or_disagree = models.BooleanField(verbose_name='Согласие', null = True)

    class Meta:
        db_table = 'applications'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.product


class Income(models.Model):
    expenses = models.PositiveIntegerField(verbose_name='Затраты')
    purchases = models.PositiveIntegerField(verbose_name='Покупки учеников')
    income = models.PositiveIntegerField(verbose_name='Доход')

    class Meta:
        db_table = 'income'
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'