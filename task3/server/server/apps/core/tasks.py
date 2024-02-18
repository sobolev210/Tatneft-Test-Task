import time

import requests
from celery import shared_task
from django.conf import settings
from django.db import transaction

from .models import FuelStation


@shared_task()
def load_data_from_source_1():
    # retries, error handling
    resp = requests.get(settings.SOURCE1_URL)
    stations_data = resp.json()

    existing_station_ids = set(
        FuelStation.objects.all().values_list("id", flat=True)
    )
    source1_stations_ids = set(station["id"] for station in stations_data)

    with transaction.atomic():
        create_station_ids = source1_stations_ids.difference(existing_station_ids)
        update_station_ids = source1_stations_ids.intersection(existing_station_ids)

        new_stations = list()

        stations_to_update = {station.id: station for station in FuelStation.objects.filter(
            id__in=update_station_ids
        )}

        for station in stations_data:
            additional_services = station.pop("additional_services")
            station["coordinate_x"], station["coordinate_y"] = station.pop("coordinates")
            station_id = station["id"]
            if station_id in create_station_ids:
                new_stations.append(
                    FuelStation(**station)
                )
            elif station_id in update_station_ids:
                db_station = stations_to_update[station_id]
                for attr, value in station.items():
                    setattr(db_station, attr, value)

        FuelStation.objects.bulk_create(new_stations)
        FuelStation.objects.bulk_update(
            list(stations_to_update.values()),
            ["coordinate_x", "coordinate_y", "number", "address", "image_urls"]
        )

    time.sleep(5)


@shared_task()
def load_data_from_source_2():
    # Получение данных по ценам на топливо
    time.sleep(5)
