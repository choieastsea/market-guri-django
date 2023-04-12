from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True, verbose_name='상품코드')
    name = models.CharField(max_length=100, verbose_name='상품명')
    price = models.PositiveIntegerField(verbose_name='상품가격')
    stock_count = models.PositiveIntegerField(verbose_name='남은수량')

    class Meta:
        db_table = 'item'
        verbose_name = '상품'
        verbose_name_plural = '상품들'
