from django.urls import path

from . import views

urlpatterns = [
    path("fuel-stations", views.FuelStationsListView.as_view())
]
