from django.urls import path, include
from core import views

urlpatterns = [
    path("symptoms/<int:id>", views.SymptomAPIView.as_view(), name="symptom"),
    path("symptoms", views.SymptomsAPIView.as_view(), name="symptoms"),
]
