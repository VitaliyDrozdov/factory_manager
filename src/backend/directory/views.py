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


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
