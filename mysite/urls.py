from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),			# url-адрес администрирования (админ-страницы)
    url(r'', include('blog.urls')),
]
