from directory.models import Equipment, Factory, Section
from rest_framework import serializers


class EquipmentSerializer(serializers.ModelSerializer):
    sections = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), many=True
    )

    class Meta:
        model = Equipment
        fields = ["id", "name", "sections"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["sections"] = [section.id for section in instance.sections.all()]
        return representation


class SectionSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True, read_only=True)
    factory = serializers.PrimaryKeyRelatedField(queryset=Factory.objects.all())

    class Meta:
        model = Section
        fields = ["id", "name", "factory", "equipment"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["factory"] = instance.factory.id

        return representation


class FactorySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ["id", "name", "sections"]
