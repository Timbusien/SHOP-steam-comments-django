from django.shortcuts import render
from .models import CategoryModel, ProductModel

# Create your views here.

def index(request):
    products = ProductModel.objects.all()
    return render(request, 'item/index.html', {'title' : 'Главное меню', 'products' : products})



def about(request):
    return render(request, 'item/about.html')
