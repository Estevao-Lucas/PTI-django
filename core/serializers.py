from rest_framework import serializers


class RetrieverSubCategorySerializer(serializers.Serializer):
    name = serializers.CharField()


class RetrieverCategorySerializer(serializers.Serializer):
    name = serializers.CharField()


class RetrieverSubstanceSerializer(serializers.Serializer):
    name = serializers.CharField()
    abbreviation = serializers.CharField()


class SymptomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    category = RetrieverCategorySerializer(required=False)
    sub_category = RetrieverSubCategorySerializer(required=False)
    nature = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    substances = serializers.ListField(
        child=RetrieverSubstanceSerializer(), required=False
    )
