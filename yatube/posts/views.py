from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template, {})

# Страница со списком сообществ;
def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template, {'slug': slug})
