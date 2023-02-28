from django.contrib import admin
from core.models import Symptom, Category, SubCategory, Nature, Substance


class SymptomAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "nature", "weight")


admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Nature)
admin.site.register(Substance)
