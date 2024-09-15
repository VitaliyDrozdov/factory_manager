from directory.models import Equipment, Factory, Section
from directory.serializers import (
    EquipmentSerializer,
    FactoryReadSerializer,
    FactoryReadShortSerializer,
    FactoryWriteSerializer,
    SectionReadSerializer,
    SectionReadShortSerializer,
    SectionWriteSerializer,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return FactoryReadSerializer
        return FactoryWriteSerializer

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


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

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TreeAPIView(APIView):
    """
    Получение родительских или дочерних объектов на разных уровнях.
    """

    def post(self, request, *args, **kwargs):
        obj_type = request.data.get("type")
        obj_id = request.data.get("id")
        level = request.data.get("level", 1)
        obj = self._get_object(obj_type, obj_id)
        if not obj:
            return Response(
                {"error": f"{obj_type} не найден"}, status=HTTP_404_NOT_FOUND
            )
        return self._handle_obj(obj, obj_type, level)

    def _get_object(self, obj_type, obj_id):
        match obj_type:
            case "factory":
                return Factory.objects.filter(id=obj_id).first()
            case "section":
                return Section.objects.filter(id=obj_id).first()
            case "equipment":
                return Equipment.objects.filter(id=obj_id).first()
            case _:
                return Response(
                    {"error": "Некорректный тип объекта"},
                    status=HTTP_404_NOT_FOUND,
                )

    def _handle_obj(self, obj, obj_type, level):
        match (obj_type, level):
            case ("factory", 0):
                return Response({"factory": FactoryReadShortSerializer(obj).data})
            case ("factory", 1):
                sections = obj.sections.all()
                return Response(
                    {"section": SectionReadShortSerializer(sections, many=True).data}
                )
            case ("factory", 2):

                equipment = Equipment.objects.filter(sections__factory=obj).distinct()
                return Response(
                    {"equipment": EquipmentSerializer(equipment, many=True).data}
                )

            case ("section", 0):
                return Response({"section": SectionReadShortSerializer(obj).data})
            case ("section", 1):
                equipment = obj.equipment.all()
                factory = obj.factory
                return Response(
                    {
                        "factory": FactoryReadShortSerializer(factory).data,
                        "equipment": EquipmentSerializer(equipment, many=True).data,
                    }
                )

            case ("equipment", 0):
                return Response({"equipment": EquipmentSerializer(obj).data})
            case ("equipment", 1):
                sections = obj.sections.all()
                return Response(
                    {"section": SectionReadShortSerializer(sections, many=True).data}
                )
            case ("equipment", 2):
                factories = Factory.objects.filter(sections__equipment=obj).distinct()
                return Response(
                    {"factory": FactoryReadShortSerializer(factories, many=True).data}
                )

            case _:
                return Response(
                    {"error": "Введите корректный уровень и тип."},
                    status=HTTP_400_BAD_REQUEST,
                )
