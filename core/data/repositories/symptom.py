from core.models import Symptom, Substance, SubCategory
from django.db import transaction
from core.domain.abstract_repositories import ABCRepository
from django.core.exceptions import ObjectDoesNotExist


class SymptomRepository(ABCRepository):
    def _get_substance_or_subcategory(self, data, symptom: Symptom, is_update=None):
        for key, value in data.items():
            if key == "sub_category":
                id = data[key].get("id", None)
                if id:
                    sub_category, _ = SubCategory.objects.update_or_create(
                        id=id,
                        defaults={
                            "name": data[key].get("name", ""),
                            "description": data[key].get("description", ""),
                        },
                    )
                    symptom.sub_category = sub_category
            elif key == "substances":
                for substance in value:
                    _substance, _ = Substance.objects.update_or_create(
                        id=substance["id"],
                        defaults={
                            "name": substance.get("name", ""),
                            "abbreviation": substance.get("abbreviation", ""),
                        },
                    )
                    symptom.substance.add(_substance)
            else:
                if is_update:
                    setattr(symptom, key, value)

    def get(self, id):
        symptom = Symptom.objects.get(id=id)

        return {
            "id": symptom.id,
            "name": symptom.name,
            "nature": symptom.nature,
            "category": symptom.name,
            "sub_category": {
                "id": symptom.sub_category.id,
                "name": symptom.sub_category.name,
                "description": symptom.sub_category.description,
            }
            if symptom.sub_category
            else None,
            "weight": symptom.weight,
            "substances": [
                {
                    "id": substance.id,
                    "name": substance.name,
                    "abbreviation": substance.abbreviation,
                }
                for substance in symptom.substance.all()
            ],
        }

    @transaction.atomic
    def delete(self, id):
        symptom = Symptom.objects.get(id=id)
        symptom.delete()
        return {"message": "Symptom has been deleted successfully"}

    @transaction.atomic
    def create(self, data):
        symptom = Symptom.objects.create(
            name=data["name"],
            nature=data["nature"],
            weight=data["weight"],
        )

        self._get_substance_or_subcategory(data, symptom)
        symptom.save()
        return {"message": "Symptom created successfully"}

    @transaction.atomic
    def update(self, data):
        try:
            id = data["id"]
            symptom = Symptom.objects.get(id=id)
        except ObjectDoesNotExist:
            return {"message": "Symptom not found"}
        else:
            self._get_substance_or_subcategory(data, symptom, is_update=True)

            symptom.save()
            return {
                "id": symptom.id,
                "name": symptom.name,
                "nature": symptom.nature,
                "category": symptom.name,
                "sub_category": {
                    "id": symptom.sub_category.id,
                    "name": symptom.sub_category.name,
                    "description": symptom.sub_category.description,
                }
                if symptom.sub_category
                else None,
                "weight": symptom.weight,
                "substances": [
                    {
                        "id": substance.id,
                        "name": substance.name,
                        "abbreviation": substance.abbreviation,
                    }
                    for substance in symptom.substance.all()
                ],
            }

    @transaction.atomic
    def list(self):
        def _data_structure(symptom):
            return {
                "id": symptom.id,
                "name": symptom.name,
                "nature": symptom.nature,
                "weight": symptom.weight,
                "sub_category": symptom.sub_category.name
                if symptom.sub_category
                else None,
            }

        return [_data_structure(symptom) for symptom in Symptom.objects.all()]
