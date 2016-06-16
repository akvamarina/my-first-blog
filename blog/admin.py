from django.contrib import admin
from .models import Post			# импорт (включение!) конкретной модели для управления ей


admin.site.register(Post)		# регистрация модели


# Register your models here.
