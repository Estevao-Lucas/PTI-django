from django.db import models


class Substance(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Symptom(models.Model):
    name = models.CharField(max_length=255)
    sub_category = models.ManyToManyField(SubCategory, null=True, blank=True)
    nature = models.CharField(max_length=100)
    weight = models.IntegerField()
    substance = models.ManyToManyField(Substance)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name
