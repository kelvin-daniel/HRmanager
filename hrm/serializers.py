from rest_framework import serializers
from django.contrib.auth import get_user_model as user_model
User = user_model()
from .models import SupervisorProfile, Department
from apps.manager.models import ManagerProfile


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
