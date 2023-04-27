import pytest
from core.models import Symptom, Substance, SubCategory
from django.core.exceptions import ObjectDoesNotExist
from core.data.repositories.symptom import SymptomRepository


@pytest.fixture
def sub_category():
    sub_category = SubCategory.objects.create(
        name="Test SubCategory", description="Test SubCategory Description"
    )
    return sub_category


@pytest.fixture
def substance():
    substance = Substance.objects.create(name="Test Substance", abbreviation="TS")
    return substance


@pytest.fixture
def symptom(sub_category, substance):
    symptom = Symptom.objects.create(
        name="Test Symptom", nature="Test Nature", weight=1
    )
    symptom.sub_category = sub_category
    symptom.substance.add(substance)
    symptom.save()
    return symptom


@pytest.fixture
def symptom_repository():
    return SymptomRepository()


@pytest.fixture
def updated_symptom_data(sub_category, substance):
    return {
        "id": 6,
        "name": "updated_symptom_name",
        "nature": "updated_symptom_nature",
        "weight": 20,
        "sub_category": {
            "id": sub_category.id,
            "name": "updated_sub_category_name",
            "description": "updated_sub_category_description",
        },
        "substances": [
            {
                "id": substance.id,
                "name": substance.name,
                "abbreviation": "updated_substance_abbr",
            }
        ],
    }


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data, expected_output",
    [
        (
            {
                "name": "Test Create Symptom",
                "nature": "Test Nature",
                "weight": 1,
                "sub_category": {
                    "id": 1,
                    "name": "Test SubCategory",
                    "description": "Test SubCategory Description",
                },
                "substances": [
                    {"id": 1, "name": "Test Substance", "abbreviation": "TS"}
                ],
            },
            {"message": "Symptom created successfully"},
        ),
        (
            {
                "name": "Test Create Symptom without SubCategory and Substance",
                "nature": "Test Nature",
                "weight": 1,
            },
            {"message": "Symptom created successfully"},
        ),
    ],
)
def test_create_symptom(symptom_repository, data, expected_output):
    output = symptom_repository.create(data)
    assert output == expected_output
    symptom = Symptom.objects.get(name=data["name"])
    assert symptom.nature == data["nature"]
    assert symptom.weight == data["weight"]
    if "sub_category" in data:
        sub_category = SubCategory.objects.get(id=data["sub_category"]["id"])
        assert symptom.sub_category == sub_category
    if "substances" in data:
        substances = Substance.objects.filter(
            id__in=[substance["id"] for substance in data["substances"]]
        )
        assert set(symptom.substance.all()) == set(substances)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "id, expected_output",
    [
        (
            3,
            {
                "id": 3,
                "name": "Test Symptom",
                "nature": "Test Nature",
                "category": "Test Symptom",
                "sub_category": {
                    "id": 2,
                    "name": "Test SubCategory",
                    "description": "Test SubCategory Description",
                },
                "weight": 1,
                "substances": [
                    {"id": 1, "name": "Test Substance", "abbreviation": "TS"}
                ],
            },
        ),
        (9, {"message": "Symptom not found"}),
    ],
)
def test_get_symptom(symptom_repository, symptom, id, expected_output):
    if id == 3:
        print(symptom.id)
        output = symptom_repository.get(id=id)
        assert output == expected_output
    else:
        with pytest.raises(ObjectDoesNotExist):
            symptom_repository.get(id)


@pytest.mark.django_db
def test_list_symptom(symptom_repository, symptom):
    output = symptom_repository.list()
    assert len(output) == 1
    assert output[0]["id"] == symptom.id
    assert output[0]["name"] == symptom.name
    assert output[0]["nature"] == symptom.nature
    assert output[0]["weight"] == symptom.weight


@pytest.mark.django_db
def test_update_symptom(symptom_repository, updated_symptom_data):
    Symptom.objects.create(name="symptom_name", nature="symptom_nature", weight=10)
    result = symptom_repository.update(updated_symptom_data)
    assert result["name"] == updated_symptom_data["name"]
    assert result["nature"] == updated_symptom_data["nature"]
    assert result["weight"] == updated_symptom_data["weight"]
    assert (
        result["sub_category"]["name"] == updated_symptom_data["sub_category"]["name"]
    )
    assert (
        result["substances"][0]["abbreviation"]
        == updated_symptom_data["substances"][0]["abbreviation"]
    )


@pytest.mark.django_db
def test_delete_symptom(symptom_repository, symptom):
    result = symptom_repository.delete(symptom.id)
    assert result == {"message": "Symptom has been deleted successfully"}
