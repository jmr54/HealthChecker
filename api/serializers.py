from rest_framework.serializers import ModelSerializer
from .models import Symptoms

class SymptomSerializer(ModelSerializer):
    class Meta:
        model = Symptoms
        fields = '__all__'