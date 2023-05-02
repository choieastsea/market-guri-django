from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='전화번호')
    address = models.CharField(max_length=100, blank=True, verbose_name='주소')
    class Meta:
        db_table = 'profile'
        verbose_name = '회원'
        verbose_name_plural = '회원들'