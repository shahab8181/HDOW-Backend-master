from rest_framework import serializers
from core.serializers import UserSerializer
# from .models import Client
from core.models import User

class ClientSerializer(serializers.ModelSerializer):
    # account_set = UserSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['birthdate', 'gender', ' phone', 'address']
