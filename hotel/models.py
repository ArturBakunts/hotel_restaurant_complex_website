from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    passport_id = models.CharField(max_length=20)
    bank_card_number = models.CharField(max_length=20)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username

