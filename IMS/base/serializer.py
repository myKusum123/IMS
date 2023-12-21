from rest_framework import serializers
from .models import*
class ComapanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
