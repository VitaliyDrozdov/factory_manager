import random

from directory.models import Equipment, Factory, Section
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Создание тестовых данных"

    def handle(self, *args, **options):
        equipment_pool = []
        for _ in range(10):
            equipment = Equipment.objects.create(name=fake.ean13())
            equipment_pool.append(equipment)
        for _ in range(5):
            factory = Factory.objects.create(name=fake.company())

            for _ in range(3):
                section = Section.objects.create(name=fake.bs(), factory=factory)
                equipment_add = random.sample(equipment_pool, random.randint(2, 5))
                section.equipment.add(*equipment_add)
        self.stdout.write(self.style.SUCCESS("Данные успешно созданы!"))
