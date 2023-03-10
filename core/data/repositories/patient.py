from core.models import Symptom, Patient
from django.db import transaction
from core.domain.abstract_repositories import ABCRepository


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
                    "sub_category": [
                        {
                            "id": sub_category.get("id"),
                            "name": sub_category.get("name"),
                            "description": sub_category.get("description"),
                        }
                        for sub_category in symptom.sub_category.all().values()
                    ],
                }
                for symptom in patient.symptoms.all()
            ],
        }

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
                    "sub_category": [
                        {
                            "id": sub_category.id,
                            "name": sub_category.name,
                            "description": sub_category.description,
                        }
                        for sub_category in symptom.sub_category.all()
                    ],
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
