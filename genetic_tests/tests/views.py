from urllib import response
from rest_framework.views import Response, APIView
from rest_framework import generics, viewsets
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from django_rest_aggregation.mixins import AggregationMixin

from genetic_tests.tests.models import Test
from genetic_tests.tests.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet, AggregationMixin):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['animal_name', 'species']

class StatistickView(APIView):
    def get(self, request):
        total_tests = Test.objects.all().annotate(Count('animal_name'))
        return Response({'statistics': TestSerializer(total_tests, many=True).data})
 