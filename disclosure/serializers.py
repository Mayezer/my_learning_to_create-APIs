from rest_framework import serializers
from disclosure.models import Disclosure


class DisclosureSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Disclosure
        fields = '__all__'