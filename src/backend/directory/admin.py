from directory.models import Equipment, Factory, Section
from django.contrib import admin


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "display_sections")
    search_fields = ("name",)
    ordering = ("name",)

    @admin.display(description="Sections")
    def display_sections(self, obj):
        return ", ".join([sectino.name for sectino in obj.sections.all()])


class EquipmentInline(admin.TabularInline):
    model = Section.equipment.through
    extra = 2


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "factory", "display_equipment")
    search_fields = (
        "name",
        "factory__name",
    )
    list_filter = ("factory",)
    ordering = ("name",)
    list_editable = (
        "name",
        "factory",
    )
    inlines = (EquipmentInline,)

    @admin.display(description="Equipment")
    def display_equipment(self, obj):
        return ", ".join([equipment.name for equipment in obj.equipment.all()])


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("sections",)
    ordering = ("name",)
