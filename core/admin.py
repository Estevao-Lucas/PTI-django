from django.contrib import admin
from core.models import Symptom, SubCategory, Substance


class SymptomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nature", "weight")


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class SubstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "abbreviation")


admin.site.register(Symptom, SymptomAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Substance, SubstanceAdmin)
