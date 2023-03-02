from core.models import Symptom
from django.db import transaction


class SymptomRepository:
    def get(self, id):
        symptom = Symptom.objects.get(id=id)

        return {
            "id": symptom.id,
            "name": symptom.name,
            "nature": symptom.nature.name,
            "category": symptom.name,
            "sub_category": [
                {
                    "name": sub_category.name,
                    "description": sub_category.description,
                }
                for sub_category in symptom.sub_category.all()
            ],
            "weight": symptom.weight,
            "substances": [
                {"name": substance.name, "abbreviation": substance.abbreviation}
                for substance in symptom.substance.all()
            ],
        }

    @transaction.atomic
    def delete(self, id):
        symptom = Symptom.objects.get(id=id)
        symptom.delete()

    @transaction.atomic
    def create(self, data):
        Symptom.objects.create(
            name=data["name"],
            sub_category=data["sub_category"],
            nature=data["nature"],
            weight=data["weight"],
            substance=data["substances"],
        )

        return {"message": "Symptom created successfully"}

    @transaction.atomic
    def update(self, data):
        try:
            id = data["id"]
            symptom = Symptom.objects.get(id=id)
        except:
            return {"message": "Symptom not found"}
        else:
            for key, value in data.items():
                setattr(symptom, key, value)
            symptom.save()
            return {"message": "Symptom updated successfully"}
