from core.models import Symptom, SubCategory, Substance, SubCategory
from django.db import transaction


class SymptomRepository:
    def _get_substance_or_subcategory(self, data, symptom, is_update=None):
        for key, value in data.items():
            if key == "sub_category":
                for sub_category in value:
                    _sub_category = SubCategory.objects.get_or_create(
                        id=sub_category["id"],
                        defaults={
                            "name": sub_category.get("name", ""),
                            "description": sub_category.get("description", ""),
                        },
                    )
                    symptom.sub_category.add(_sub_category[0])
            elif key == "substances":
                for substance in value:
                    _substance = Substance.objects.get_or_create(
                        id=substance["id"],
                        defaults={
                            "name": substance["name"],
                            "abbreviation": substance["abbreviation"],
                        },
                    )
                    symptom.substance.add(_substance[0])
            else:
                if is_update:
                    for key, value in data.items():
                        setattr(symptom, key, value)

    def get(self, id):
        symptom = Symptom.objects.get(id=id)

        return {
            "id": symptom.id,
            "name": symptom.name,
            "nature": symptom.nature,
            "category": symptom.name,
            "sub_category": [
                {
                    "id": sub_category.id,
                    "name": sub_category.name,
                    "description": sub_category.description,
                }
                for sub_category in symptom.sub_category.all()
            ],
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

        return {"message": "Symptom created successfully"}

    @transaction.atomic
    def update(self, data):
        try:
            id = data["id"]
            symptom = Symptom.objects.get(id=id)
        except:
            return {"message": "Symptom not found"}
        else:
            self._get_substance_or_subcategory(data, symptom, is_update=True)

            symptom.save()
            return {
                "id": symptom.id,
                "name": symptom.name,
                "nature": symptom.nature,
                "category": symptom.name,
                "sub_category": [
                    {
                        "id": sub_category.id,
                        "name": sub_category.name,
                        "description": sub_category.description,
                    }
                    for sub_category in symptom.sub_category.all()
                ],
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
        return list(Symptom.objects.all().values("id", "name", "nature"))


class SubstanceRepository:
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


class SubCategoryRepository:
    def get(self, id):
        sub_category = SubCategory.objects.get(id=id)

        return {
            "id": sub_category.id,
            "name": sub_category.name,
            "description": sub_category.description,
        }

    def list(self):
        return list(SubCategory.objects.all().values("id", "name", "description"))

    @transaction.atomic
    def update(self, data):
        id = data.pop("id")
        sub_category = SubCategory.objects.get(id=id)
        for key, value in data.items():
            setattr(sub_category, key, value)

        return {
            "id": sub_category.id,
            "name": sub_category.name,
            "description": sub_category.description,
        }

    @transaction.atomic
    def delete(self, data):
        sub_category = SubCategory.objects.get(id=data)
        sub_category.delete()
        return {"message": "SubCategory has been deleted successfully"}

    @transaction.atomic
    def create(self, data):
        SubCategory.objects.create(name=data["name"], description=data["description"])

        return {"message": "SubCategory created successfully"}
