from django.db import models


class Factory(models.Model):
    """
    Реализация справочника уровня фабрики.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    """
    Реализация справочника уровня участка.
    """

    name = models.CharField(max_length=255, unique=True)
    factory = models.ForeignKey(
        Factory, related_name="sections", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):
    """
    Реализация справочника уровня оборудования.
    """

    name = models.CharField(max_length=255, unique=True)
    sections = models.ManyToManyField(Section, related_name="equipment")

    def __str__(self) -> str:
        return self.name
