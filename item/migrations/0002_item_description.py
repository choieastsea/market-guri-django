# Generated by Django 4.2 on 2023-06-16 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='', verbose_name='상품설명'),
        ),
    ]
