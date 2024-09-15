from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers


class TreeRequestSerializer(serializers.Serializer):
    type = serializers.CharField(help_text="Тип объекта (factory, section, equipment)")
    id = serializers.IntegerField(help_text="ID объекта")
    level = serializers.IntegerField(
        default=1, help_text="Уровень родителя или дочернего объекта"
    )


tree_post_docs = swagger_auto_schema(
    operation_description="Получение родительских или дочерних объектов",
    request_body=TreeRequestSerializer,
    responses={
        200: openapi.Response(
            description="Пример успешного ответа",
            examples={
                "application/json": {
                    "factory": {"id": 1, "name": "Factory 1"},
                    "section": [
                        {"id": 1, "name": "Section 1"},
                        {"id": 2, "name": "Section 2"},
                    ],
                }
            },
        ),
        400: openapi.Response(description="Ошибка в запросе"),
        404: openapi.Response(description="Объект не найден"),
    },
)
