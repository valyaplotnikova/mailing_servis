from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
        help_text='Введите заголовок')
    content = models.TextField(
        verbose_name="Контент",
        help_text="Ведите контент",
    )
    preview = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение"
    )

    views_count = models.IntegerField(
        default=0,
        verbose_name="Счетчик просмотров"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        blank=True,
        null=True,
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.title} {self.content}"

    class Meta:
        verbose_name = "блог"  # Настройка для наименования одного объекта
        verbose_name_plural = "блоги"  # Настройка для наименования набора объектов
        ordering = ("title", "content",)
