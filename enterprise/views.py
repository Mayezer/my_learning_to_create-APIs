from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializers

class EnterpriseListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializers


class EnterpriseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializers
