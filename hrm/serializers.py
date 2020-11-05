from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('logo', 'description', 'name', 'location', 'contact')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('logo', 'description', 'name', 'location', 'contact')