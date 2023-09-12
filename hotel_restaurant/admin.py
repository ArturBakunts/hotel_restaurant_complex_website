from django.contrib import admin

from . import models

admin.site.register(models.ReservedTable)
admin.site.register(models.Table)