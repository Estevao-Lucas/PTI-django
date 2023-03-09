from django.urls import path
from core.app.api.views.patient_view import PatientAPIView, PatientsAPIView
from core.app.api.views.subcategory_view import SubCategoriesAPIView, SubCategoryAPIView
from core.app.api.views.symptom_view import SymptomAPIView, SymptomsAPIView
from core.app.api.views.substance_view import SubstanceAPIView, SubstancesAPIView

urlpatterns = [
    path("symptoms/<int:id>", SymptomAPIView.as_view(), name="symptom"),
    path("symptoms", SymptomsAPIView.as_view(), name="symptoms"),
    path("substances", SubstancesAPIView.as_view(), name="substances"),
    path("substances/<int:id>", SubstanceAPIView.as_view(), name="substance"),
    path("sub-categories", SubCategoriesAPIView.as_view(), name="sub-categories"),
    path(
        "sub-categories/<int:id>",
        SubCategoryAPIView.as_view(),
        name="sub-category",
    ),
    path("patients", PatientsAPIView.as_view(), name="patients"),
    path("patients/<int:id>", PatientAPIView.as_view(), name="patient"),
]
