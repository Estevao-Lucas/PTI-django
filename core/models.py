from django.db import models


class Substance(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Nature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Symptom(models.Model):
    category = models.OneToOneField(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    sub_category = models.OneToOneField(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    nature = models.ForeignKey(Nature, on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.IntegerField()
    substance = models.ManyToManyField(Substance)

    def __str__(self):
        return self.category.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    born_date = models.DateField()
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name
