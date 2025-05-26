from django.db import models


class CoreModel(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Заголовок",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True
