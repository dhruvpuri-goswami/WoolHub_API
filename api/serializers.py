from rest_framework import serializers
from .models import RawWoolData

class RawWoolDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawWoolData
        fields = '__all__'
