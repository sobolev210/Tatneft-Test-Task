from django.contrib import admin

from apps.core.models import FuelStation, FuelType, FuelPrice, AdditionalService

admin.site.register(FuelStation)
admin.site.register(FuelType)
admin.site.register(FuelPrice)
admin.site.register(AdditionalService)
