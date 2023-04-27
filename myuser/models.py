from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    # OneToOne Field로 django의 User model과 연결
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='계정')
    # additional fields
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='전화번호')
    address = models.CharField(max_length=100, blank=True, verbose_name='주소')

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'profile'
        verbose_name = '회원'
        verbose_name_plural = '회원들'
