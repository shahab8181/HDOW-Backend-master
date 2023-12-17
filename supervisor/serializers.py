from rest_framework import serializers
from .models import Supervisor
from core.serializers import UserSerializer


class SupervisorSerializer(serializers.ModelSerializer):
    account_set = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Supervisor
        fields = '__all__'
