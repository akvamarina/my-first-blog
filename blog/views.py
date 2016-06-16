from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    # отдельная переменная для выборки (подмножества) из бд
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # возвращает соотв html-страницу в ответ на запрос (erquest)
