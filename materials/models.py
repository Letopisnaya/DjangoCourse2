from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(
        upload_to="materials/course/previews",
        null=True,
        blank=True,
        verbose_name="Превью",
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    name_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Название курса",
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    preview = models.ImageField(
        upload_to="materials/lesson/previews",
        null=True,
        blank=True,
        verbose_name="Превью",
    )
    video = models.URLField(max_length=150, null=True, blank=True, verbose_name="Видео")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name