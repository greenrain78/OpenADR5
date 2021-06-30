from django.contrib import admin

# Register your models here.
from app_collect.models import equipments_info, power_info

admin.site.register(equipments_info)
admin.site.register(power_info)