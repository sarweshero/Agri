from rest_framework import serializers
from .models import landprep, transplanting, fertilizer, harverst, packaging, Procurement, packing

class LandPrepSerializer(serializers.ModelSerializer):
    class Meta:
        model = landprep
        fields = '__all__'

class TransplantingSerializer(serializers.ModelSerializer):
    class Meta:
        model = transplanting
        fields = '__all__'

class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = fertilizer
        fields = '__all__'

class HarverstSerializer(serializers.ModelSerializer):
    class Meta:
        model = harverst
        fields = '__all__'

class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = packaging
        fields = '__all__'

class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'

class PackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = packing
        fields = '__all__'