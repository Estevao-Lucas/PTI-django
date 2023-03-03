from core.models import Symptom, SubCategory, Substance
from django.db import transaction


class SymptomRepository:
    def get(self, id):
        symptom = Symptom.objects.get(id=id)

        return {
            "id": symptom.id,
            "name": symptom.name,
            "nature": symptom.nature,
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
        return {"message": "Symptom has been deleted successfully"}

    @transaction.atomic
    def create(self, data):
        sub_category = SubCategory.objects.get_or_create(
            name=data["sub_category"]["name"],
            defaults={"description": data["sub_category"]["description"]},
        )

        Symptom.objects.create(
            name=data["name"],
            sub_category=sub_category[0],
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
                if key == "sub_category":
                    for sub_catagory in value:
                        sub_category = SubCategory.objects.get_or_create(
                            name=sub_catagory["name"],
                            defaults={"description": sub_catagory["description"]},
                        )
                        symptom.sub_category.add(sub_category[0])
                elif key == "substances":
                    for substance in value:
                        _substance = Substance.objects.get_or_create(
                            name=substance["name"],
                            defaults={"abbreviation": substance["abbreviation"]},
                        )
                        symptom.substance.add(_substance[0])
                else:
                    setattr(symptom, key, value)
            symptom.save()
            return {
                "id": symptom.id,
                "name": symptom.name,
                "nature": symptom.nature,
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
