from django.contrib import admin

from . import models

# hotel-admin bakuntsartur93@gmail.com 12345


admin.site.register(models.Room)
admin.site.register(models.ReservedRoom)
admin.site.register(models.RoomOption)

