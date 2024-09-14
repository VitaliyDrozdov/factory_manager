from directory.models import Equipment, Factory, Section
from rest_framework import serializers


class EquipmentSerializer(serializers.ModelSerializer):
    sections = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Equipment
        fields = ["id", "name", "sections"]


class SectionWriteSerializer(serializers.ModelSerializer):
    equipment = serializers.PrimaryKeyRelatedField(
        queryset=Equipment.objects.all(), many=True
    )
    factory = serializers.PrimaryKeyRelatedField(queryset=Factory.objects.all())

    class Meta:
        model = Section
        fields = ["id", "name", "factory", "equipment"]


class SectionReadSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ["id", "name", "equipment"]


class SectionReadShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            "id",
            "name",
        ]


class FactoryReadSerializer(serializers.ModelSerializer):

    sections = SectionReadSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ["id", "name", "sections"]


class FactoryReadShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = ["id", "name"]


class FactoryWriteSerializer(serializers.ModelSerializer):

    sections = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), many=True
    )

    class Meta:
        model = Factory
        fields = ["id", "name", "sections"]
