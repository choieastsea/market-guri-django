from django.db import models
from django.conf import settings
from item.models import Item

# Create your models here.
class Question(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='상품', default=None)
    title = models.CharField(verbose_name='질문 제목', max_length=100)
    content = models.TextField(verbose_name='질문 내용')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, verbose_name='질문자') # 사용자 삭제되면 질문도 삭제되도록
    date_created = models.DateField(verbose_name='작성일자', auto_now_add=True) # 질문 생성되면 자동으로 해당 시간으로 초기화
    class Meta:
        db_table = 'question'
        verbose_name = '질문'
        verbose_name_plural = '질문들'

class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE, verbose_name='질문')
    answer = models.TextField(verbose_name='판매자 답변')
    date_created = models.DateField(verbose_name='작성일자', auto_now_add=True)
    class Meta:
        db_table = 'answer'
        