from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model as user_model
User = user_model()
from .models import SupervisorProfile, Department
from apps.manager.models import ManagerProfile

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('logo', 'description', 'name', 'location', 'contact')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar', 'username', 'name', 'email', 'contact')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('avatar', 'name', 'email', 'contact', 'address')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','email','is_admin','is_teammanager','is_manager','is_employee',)

class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = ManagerProfile
        fields = '__all__'


class TeamManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeamManagerProfile
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    teammanager = TeamManagerSerializer()

    class Meta:
        model = Team
        fields = '__all__'

class LeaveSerializer(serializer.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'

