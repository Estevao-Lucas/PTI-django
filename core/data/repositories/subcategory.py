from core.models import SubCategory
from django.db import transaction
from core.domain.abstract_repositories import ABCRepository


class SubCategoryRepository(ABCRepository):
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
