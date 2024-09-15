from directory.models import Equipment, Factory, Section
from rest_framework import serializers


class EquipmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели оборудования.
    """

    sections = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Equipment
        fields = ["id", "name", "sections"]


class SectionWriteSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели участка UNSAFE методов.
    """

    equipment = serializers.PrimaryKeyRelatedField(
        queryset=Equipment.objects.all(), many=True
    )
    factory = serializers.PrimaryKeyRelatedField(queryset=Factory.objects.all())

    class Meta:
        model = Section
        fields = ["id", "name", "factory", "equipment"]


class SectionReadSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели участка SAFE методов.
    """

    equipment = EquipmentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ["id", "name", "equipment"]


class SectionReadShortSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели участка SAFE методов (эндпоинт tree/).
    """

    class Meta:
        model = Section
        fields = [
            "id",
            "name",
        ]


class FactoryReadSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели фабрики SAFE методов.
    """

    sections = SectionReadSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ["id", "name", "sections"]


class FactoryReadShortSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели фабрики SAFE методов (эндпоинт tree/).
    """

    class Meta:
        model = Factory
        fields = ["id", "name"]


class FactoryWriteSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели фабрики UNSAFE методов.
    """

    sections = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), many=True
    )

    class Meta:
        model = Factory
        fields = ["id", "name", "sections"]
