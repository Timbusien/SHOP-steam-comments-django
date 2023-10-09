from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=70)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    img = models.FileField(upload_to='items')
    favorite_by = models.ManyToManyField(User, related_name='favorite_items', blank=True)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукты для магазина'
        verbose_name_plural = 'добавление продуктов'



class Task(models.Model):
    title = models.CharField('Тема', max_length=100)
    task = models.TextField('Содержание')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Жалобы или поправки'
        verbose_name_plural = 'Содержание жалобы'






