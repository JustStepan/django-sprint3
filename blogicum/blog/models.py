from django.db import models
from django.contrib.auth import get_user_model
from core.models import CoreModel


USER = get_user_model()


class Category(CoreModel):
    description = models.TextField(blank=False, verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='''Идентификатор страницы для URL;
        разрешены символы латиницы, цифры, дефис и подчёркивание.'''
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(CoreModel):
    name = models.CharField(
        max_length=256,
        blank=False,
        default='Планета Земля',
        verbose_name="Название места",
    )
    title = None

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(CoreModel):
    text = models.TextField(blank=False, verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='''Если установить дату и время в будущем —
         можно делать отложенные публикации.'''
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория',
    )
    author = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
