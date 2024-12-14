from rest_framework import generics, viewsets

from genetic_tests.tests.models import Test
from genetic_tests.tests.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (Token)
