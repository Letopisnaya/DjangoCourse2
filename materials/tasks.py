from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_subscription(email):
    send_mail(
        "Подписка", "Курс, на который вы подписаны, обновлен", EMAIL_HOST_USER, email
    )


@shared_task
def last_login_check():
    today = timezone.now().today()
    users = User.objects.filter(last_login__isnull=False)
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} отключен")
        else:
            print(f"Пользователь {user.email} активен")