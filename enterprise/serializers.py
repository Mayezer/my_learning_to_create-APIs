from rest_framework import serializers
from enterprise.models import Enterprise


class EnterpriseSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Enterprise
        fields = '__all__'
