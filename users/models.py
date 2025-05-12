from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=35, null=True, blank=True, verbose_name="Номер телефона"
    )
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="users/avatars", null=True, blank=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_STATUS = [
        ("cash", "наличные"),
        ("transfer", "перевод на счет"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )
    data_payment = models.DateField(auto_now_add=True, verbose_name="Дата платежа")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Оплаченный курс",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Оплаченный урок",
    )
    payment_amount = models.PositiveIntegerField(verbose_name="Сумма платежа")
    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS,
        default="transfer",
        verbose_name="Метод оплаты",
    )
    session_id = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="id сессии"
    )
    link = models.URLField(
        max_length=400, null=True, blank=True, verbose_name="Ссылка на оплату"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.payment_amount
