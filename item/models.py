from django.db import models
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
    category = models.ManyToManyField(CategoryModel, null=True, blank=True)
    img = models.FileField(upload_to='item')
    favorite_by = models.ManyToManyField(User, related_name='favorite_item', blank=True)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукты для магазина'
        verbose_name_plural = 'добавление продуктов'
