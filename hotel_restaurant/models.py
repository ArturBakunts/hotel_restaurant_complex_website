from django.db import models
from django.utils import timezone


class ReservedTable(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(default='')
    guest_qty = models.PositiveIntegerField(default=1)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Table(models.Model):
    guests_max_qty = models.PositiveIntegerField(default=1)
    free_tables_qty = models.IntegerField(default=0)
