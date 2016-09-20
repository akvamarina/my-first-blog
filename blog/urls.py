from django.conf.urls import url
from . import views         # все представления из приложения blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),      # name - имя для идентификации данного url
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

 # ^$ - начало и конец = пустая строка, т.к. адрес порта - не часть url, т.е.
 # запрос к веб-сайту по адресу 'http://127.0.0.1:8000/' = '', т.е. '^$'

 