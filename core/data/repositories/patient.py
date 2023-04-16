from core.models import Symptom, Patient, Substance
from django.db import transaction
from core.domain.abstract_repositories import ABCRepository
from django.db.models.functions import Coalesce


class PatientRepository(ABCRepository):
    def list(self):
        return list(Patient.objects.all().values())

    def get(self, data):
        patient = Patient.objects.get(id=data)
        return {
            "id": patient.id,
            "name": patient.name,
            "mothers_name": patient.mothers_name,
            "birth_date": patient.birth_date,
            "symptoms": [
                {
                    "id": symptom.id,
                    "name": symptom.name,
                    "nature": symptom.nature,
                    "weight": symptom.weight,
                    "sub_category": {
                        "id": symptom.sub_category.id,
                        "name": symptom.sub_category.name,
                        "description": symptom.sub_category.description,
                    }
                    if symptom.sub_category
                    else None,
                }
                for symptom in patient.symptoms.all()
            ],
            "substance_punctuation": self._get_punctuation(patient),
        }

    def _get_punctuation(self, patient):
        symptoms = patient.symptoms.all()
        substances = set(Substance.objects.filter(symptom__in=symptoms))

        result = [
            {
                "name": substance.name,
                "traeted_symptoms": list(
                    set(
                        symptoms.filter(substance=substance)
                        .annotate(category_name=Coalesce("sub_category__name", "name"))
                        .values_list("category_name", flat=True)
                    )
                ),
                "total_punctuation": sum(
                    symptoms.filter(substance=substance).values_list(
                        "weight", flat=True
                    )
                ),
            }
            for substance in substances
        ]

        return result

    def update(self, data):
        patient = Patient.objects.get(id=data["id"])
        symptoms = data.pop("symptoms", None)
        if symptoms:
            for symptom in symptoms:
                patient.symptoms.add(Symptom.objects.get(id=symptom["id"]))
        for key, value in data.items():
            setattr(patient, key, value)

        return {
            "id": patient.id,
            "name": patient.name,
            "mothers_name": patient.mothers_name,
            "birth_date": patient.birth_date,
            "symptoms": [
                {
                    "id": symptom.id,
                    "name": symptom.name,
                    "nature": symptom.nature,
                    "weight": symptom.weight,
                    "sub_category": {
                        "id": symptom.sub_category.id,
                        "name": symptom.sub_category.name,
                        "description": symptom.sub_category.description,
                    }
                    if symptom.sub_category
                    else None,
                }
                for symptom in patient.symptoms.all()
            ],
        }

    @transaction.atomic
    def delete(self, data):
        Patient.objects.get(id=data).delete()
        return {"message": "Patient has been deleted successfully"}

    def create(self, data):
        patient = Patient.objects.create(
            name=data["name"],
            mothers_name=data["mothers_name"],
            birth_date=data["birth_date"],
        )
        symptoms = data.pop("symptoms", None)

        if symptoms:
            for symptom in symptoms:
                patient.symptoms.add(Symptom.objects.get(id=symptom))

        return {"message": "Patient created successfully"}
