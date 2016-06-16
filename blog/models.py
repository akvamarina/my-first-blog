from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')         # автор записи - ссылка на другую модель(!) - ForeignKey
    title = models.CharField(max_length=200)        # заголовок - поле символов длиной не более 200
    text = models.TextField()                       # запись - неогр. текстовое поле
    created_date = models.DateTimeField(            # дата создания - текущая дата на момент созд.
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    # методы
    def publish(self):                              #   публикация записи - самого объекта (self)
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

