from django.contrib import admin
from .models import ProductModel, CategoryModel, Task


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
#
#
@admin.register(ProductModel)
class ProductModeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'uploaded_at']
    search_fields = ['title', 'price']
    list_filter = ['uploaded_at']


admin.site.register(Task)

