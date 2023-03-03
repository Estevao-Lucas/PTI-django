from django.contrib import admin
from core.models import Symptom, SubCategory, Substance


class SymptomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nature", "weight")


admin.site.register(Symptom, SymptomAdmin)
admin.site.register(SubCategory)
admin.site.register(Substance)
