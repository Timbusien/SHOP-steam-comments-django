from django.shortcuts import render, redirect
# from django.views.generic import ListView
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskForm
from .models import Task
# from .models import CategoryModel, ProductModel

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("item:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="item/register.html", context={"register_form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("item:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()

    return render(request=request, template_name="item/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('item:homepage')


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