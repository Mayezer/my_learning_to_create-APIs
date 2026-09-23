from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializers

class EnterpriseListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializers


class EnterpriseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializers
