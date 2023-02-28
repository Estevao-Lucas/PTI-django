from django.urls import path, include
from core import views

urlpatterns = [
    path("symptoms/<int:id>", views.SymptomsAPIView.as_view(), name="symptom"),
]
