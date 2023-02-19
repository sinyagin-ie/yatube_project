from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name = 'index'),
    # Страница со списком сообществ
    path('group/<slug:slug>/', views.group_post, name = 'group_list'),
]