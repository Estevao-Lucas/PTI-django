from django.contrib import admin
from core.models import Symptom, SubCategory, Substance, Patient


class SymptomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sub_category", "nature", "weight")


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class SubstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "abbreviation")


class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mothers_name", "birth_date")


admin.site.register(Patient, PatientAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Substance, SubstanceAdmin)
