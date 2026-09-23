from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from disclosure.models import Disclosure
from disclosure.serializers import DisclosureSerializer


class DisclosureListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Disclosure.objects.all()
    serializer_class = DisclosureSerializer


class DisclosureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Disclosure.objects.all()
    serializer_class = DisclosureSerializer
