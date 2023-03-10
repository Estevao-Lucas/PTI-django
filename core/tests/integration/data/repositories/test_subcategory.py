from core.data.repositories.subcategory import SubCategoryRepository
from core.models import SubCategory
import pytest


@pytest.fixture
@pytest.mark.django_db
def set_up_subcategory():
    SubCategory.objects.all().delete()
    SubCategory.objects.create(
        name="Test Subcategory", description="Test Description", id=1
    )
    SubCategory.objects.create(
        name="Test Subcategory 2", description="Test Description 2", id=2
    )


@pytest.mark.django_db
def test_get_subcategory(set_up_subcategory):
    subcategory = SubCategoryRepository().get(id=1)
    assert subcategory["name"] == "Test Subcategory"
    assert subcategory["description"] == "Test Description"


@pytest.mark.django_db
def test_get_subcategory_not_found(set_up_subcategory):
    with pytest.raises(SubCategory.DoesNotExist) as e:
        SubCategoryRepository().get(id=4)
    assert e.value.args[0] == "SubCategory matching query does not exist."


@pytest.mark.django_db
def test_create_subcategory():
    created_subcategory = SubCategoryRepository().create(
        data={"name": "Teste Create", "description": ""}
    )
    assert created_subcategory["message"] == "SubCategory created successfully"


@pytest.mark.django_db
def test_update_subcategory(set_up_subcategory):
    updated_subcategory = SubCategoryRepository().update(
        data={"id": 1, "name": "Teste Update", "description": ""}
    )
    assert updated_subcategory["name"] == "Teste Update"


@pytest.mark.django_db
def test_list_subcategory(set_up_subcategory):
    subcategories = SubCategoryRepository().list()
    assert len(subcategories) == 2
    for subcategory in subcategories:
        assert subcategory["name"] in ["Test Subcategory", "Test Subcategory 2"]
        assert subcategory["description"] in ["Test Description", "Test Description 2"]


@pytest.mark.django_db
def test_delete_subcategory(set_up_subcategory):
    subcategory = SubCategoryRepository()
    subcategory.delete(data=1)
    subcategories = subcategory.list()
    assert len(subcategories) == 1
    assert subcategories[0]["name"] == "Test Subcategory 2"
