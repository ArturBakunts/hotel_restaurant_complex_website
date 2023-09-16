from django.db import models
from django.utils import timezone


class Room(models.Model):
    title = models.CharField(max_length=50, default='')
    guests_qty = models.IntegerField(default=0)
    price_optional = models.CharField(max_length=20, default='')
    free_room_qty = models.IntegerField(default=0)
    default_price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to='room_images/', null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class RoomOption(models.Model):
    title = models.CharField(max_length=50, default='')
    options = models.CharField(max_length=300, default='')
    ind = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ReservedRoom(models.Model):
    full_name = models.CharField(max_length=250, default='')
    email = models.EmailField(default='')
    type = models.ForeignKey(Room, on_delete=models.CASCADE)
    option = models.ForeignKey(RoomOption, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    additional_message = models.CharField(max_length=250, default='empty')

    def __str__(self):
        return self.full_name



# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
#
# class CustomUser(AbstractUser):
#     phone_number = PhoneNumberField(unique=True, blank=True, null=True)
#
#     def __str__(self):
#         return self.username

# pip install django-phonenumber-field

# В файле вашего проекта Django settings.pyдобавьте 'phonenumber_field'в INSTALLED_APPSсписок:
# питон
#
# Скопировать код
# INSTALLED_APPS = [
#     # ...
#     'phonenumber_field',
#     # ...
# ]