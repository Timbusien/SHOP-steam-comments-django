from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),

]