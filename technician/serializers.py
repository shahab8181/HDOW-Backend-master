from rest_framework import serializers
from .models import Technician
# from core.serializers import UserSerializer

class TechnicianSerializer(serializers.ModelSerializer):
    # account_set = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Technician
        fields = '__all__'

