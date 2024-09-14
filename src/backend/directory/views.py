from directory.models import Equipment, Factory, Section
from directory.serializers import (
    EquipmentSerializer,
    FactorySerializer,
    SectionSerializer,
)
from rest_framework import viewsets


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    paginate_by = 10


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    paginate_by = 10


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    paginate_by = 10
