from directory.models import Equipment, Factory, Section
from rest_framework import serializers


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            "name",
        ]


class SectionSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ["name", "equipment"]


class FactorySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ["name", "sections"]
