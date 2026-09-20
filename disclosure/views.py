from rest_framework import generics
from disclosure.models import Disclosure
from disclosure.serializers import DisclosureSerializer


class DisclosureListCreateView(generics.ListCreateAPIView):
    queryset = Disclosure.objects.all()
    serializer_class = DisclosureSerializer


class DisclosureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disclosure.objects.all()
    serializer_class = DisclosureSerializer
