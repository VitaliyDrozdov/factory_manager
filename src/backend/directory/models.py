from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Factory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=255, unique=True)
    factory = models.ForeignKey(
        Factory, related_name="sections", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    sections = models.ManyToManyField(Section, related_name="equipment")

    def __str__(self) -> str:
        return self.name
