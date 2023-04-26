from core.models import Substance
from django.db import transaction
from core.domain.abstract_repositories import ABCRepository


class SubstanceRepository(ABCRepository):
    @transaction.atomic
    def get(self, id):
        substance = Substance.objects.get(id=id)

        return {
            "id": substance.id,
            "name": substance.name,
            "abbreviation": substance.abbreviation,
        }

    def list(self):
        return list(Substance.objects.all().values("id", "name", "abbreviation"))

    @transaction.atomic
    def update(self, data):
        id = data.pop("id")
        substance = Substance.objects.get(id=id)
        for key, value in data.items():
            setattr(substance, key, value)
        substance.save()
        return {
            "id": substance.id,
            "name": substance.name,
            "abbreviation": substance.abbreviation,
        }

    @transaction.atomic
    def delete(self, data):
        substance = Substance.objects.get(id=data)
        substance.delete()
        return {"message": "Substance has been deleted successfully"}

    @transaction.atomic
    def create(self, data):
        Substance.objects.create(name=data["name"], abbreviation=data["abbreviation"])

        return {"message": "Substance created successfully"}
