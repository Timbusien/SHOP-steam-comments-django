from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import TaskForm

from .models import Task
# from .models import CategoryModel, ProductModel

# Create your views here.

def index(request):
    task = Task.objects.all()
    return render(request, 'item/index.html', {'title' : 'Главное меню', 'tasks' : task})


def about(request):
    return render(request, 'item/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = 'неверный коментарий'
    form = TaskForm()
    context = {
        'form' : form,
        'error': error

    }
    return render(request, 'item/create.html', context)


# class Shop_Page(ListView):
#     template_name = 'item/index.html'
#     queryset = ProductModel.objects.all()
#     context_object_name = 'store'
#
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = CategoryModel.objects.all()
#
#         return context