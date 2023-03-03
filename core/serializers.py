from rest_framework import serializers


class RetrieverSubCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


class RetrieverSubstanceSerializer(serializers.Serializer):
    name = serializers.CharField()
    abbreviation = serializers.CharField()


class SymptomSerializer(serializers.Serializer):
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
