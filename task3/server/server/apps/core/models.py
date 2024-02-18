from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.core.enums import CurrencyEnum


class FuelStation(models.Model):
    number = models.PositiveIntegerField(null=False)
    coordinate_x = models.FloatField(null=False)
    coordinate_y = models.FloatField(null=False)
    address = models.TextField(null=True)
    image_urls = ArrayField(
        models.CharField(max_length=2000),
        null=True, blank=True
    )
    services = models.ManyToManyField("AdditionalService", related_name="fuel_stations", blank=True)

    def __str__(self):
        return f"АЗС № {self.number}"

    # class Meta:


class AdditionalService(models.Model):
    name = models.CharField(max_length=500, null=False)
    icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Доп. сервис '{self.name}'"


class FuelType(models.Model):
    name = models.CharField(max_length=100, null=False)
    icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Топливо '{self.name}'"


class FuelPrice(models.Model):
    fuel_type = models.ForeignKey(FuelType, null=False, on_delete=models.CASCADE)
    fuel_station = models.ForeignKey(FuelStation, null=False, related_name="prices", on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    currency = models.CharField(max_length=10, choices=CurrencyEnum.choices())

    class Meta:
        unique_together = ["fuel_type", "fuel_station"]

    def __str__(self):
        return f"Цена топлива '{self.fuel_type}' для '{self.fuel_station}'"
