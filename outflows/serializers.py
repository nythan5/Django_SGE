from .models import Outflow
from rest_framework.serializers import ModelSerializer


class OutflowSerializer(ModelSerializer):
    class Meta:
        model = Outflow
        fields = '__all__'
