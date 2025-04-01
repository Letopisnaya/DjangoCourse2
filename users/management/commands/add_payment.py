from django.core.management.base import BaseCommand

from materials.models import Course
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(email="admin@gmail.com")
        paid_course = Course.objects.get(name="Начальный модуль")

        payment = Payment.objects.create(
            user=user, course=paid_course, payment_amount="1000", payment_method="cash"
        )
        payment.save()