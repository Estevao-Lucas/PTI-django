from rest_framework import serializers


class RetrieverSubCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)


class RetrieverSubstanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    abbreviation = serializers.CharField(required=False)


class RetrieverSymptomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    sub_category = serializers.ListField(
        child=RetrieverSubCategorySerializer(), required=False
    )
    nature = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    substances = serializers.ListField(
        child=RetrieverSubstanceSerializer(), required=False
    )


class SymptomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    nature = serializers.CharField(required=False)


class RetrieverSubstancePunctuationSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    traeted_symptoms = serializers.ListField(
        child=serializers.CharField(), required=False
    )
    total_punctuation = serializers.IntegerField(required=False)


class RetrieverPatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    mothers_name = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    symptoms = serializers.ListField(child=RetrieverSymptomSerializer(), required=False)
    substance_punctuation = serializers.ListField(
        child=RetrieverSubstancePunctuationSerializer(), required=False
    )


class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    mothers_name = serializers.CharField(required=False)
