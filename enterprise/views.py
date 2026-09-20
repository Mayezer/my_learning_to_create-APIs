from rest_framework import generics
from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializers

class EnterpriseListCreateView(generics.ListCreateAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializers


class EnterpriseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializers
