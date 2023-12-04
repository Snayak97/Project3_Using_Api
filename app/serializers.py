from rest_framework import serializers

from app.models import *
class Details_Model_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields='__all__'