from django.contrib import admin

from . import models

admin.site.register(models.Table)
admin.site.register(models.ReservedTable)

