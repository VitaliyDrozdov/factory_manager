from directory.models import Equipment, Factory, Section
from django.contrib import admin


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "factory")
    search_fields = ("name", "factory__name")
    list_filter = ("factory",)
    ordering = ("name",)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("sections",)
    ordering = ("name",)
