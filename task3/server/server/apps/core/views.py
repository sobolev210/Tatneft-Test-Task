from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FuelStation
from .serializers import FuelStationSerializer


class FuelStationsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FuelStation.objects.all().order_by("id")
    serializer_class = FuelStationSerializer
