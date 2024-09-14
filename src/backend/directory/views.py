from directory.models import Equipment, Factory, Section
from directory.serializers import (
    EquipmentSerializer,
    FactoryReadSerializer,
    FactoryWriteSerializer,
    SectionReadSerializer,
    SectionWriteSerializer,
)
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return FactoryReadSerializer
        return FactoryWriteSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SectionReadSerializer
        return SectionWriteSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    paginate_by = 10
