from django.db import models
from item.models import Item
from django.conf import settings

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, verbose_name='사용자') # 사용자 삭제되면 장바구니도 삭제되도록
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='상품')
    amount = models.PositiveIntegerField(verbose_name='수량', default=1)
    date_created = models.DateField(verbose_name='최종 수정 일자', auto_now=True) # 추가되거나, 수정되면 update되도록 함
    class Meta:
        db_table = 'cart'
        verbose_name = '장바구니 물건'
        verbose_name_plural = '장바구니 물건들'