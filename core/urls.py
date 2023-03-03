from django.urls import path, include
from core import views

urlpatterns = [
    path("symptoms/<int:id>", views.SymptomAPIView.as_view(), name="symptom"),
    path("symptoms", views.SymptomsAPIView.as_view(), name="symptoms"),
    path("substances", views.SubstancesAPIView.as_view(), name="substances"),
    path("substances/<int:id>", views.SubstanceAPIView.as_view(), name="substance"),
    path("sub-categories", views.SubCategoriesAPIView.as_view(), name="sub-categories"),
    path(
        "sub-categories/<int:id>",
        views.SubCategoryAPIView.as_view(),
        name="sub-category",
    ),
]
