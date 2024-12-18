from rest_framework.views import Response, APIView
from rest_framework import status
from django.db.models import Count, Avg, Max, Q


from genetic_tests.tests.models import Test
from genetic_tests.tests.serializers import TestSerializer


class TestsView(APIView):
    def get(self, request):
        species = request.query_params.get('species', None)
        tests = Test.objects.filter(species=species) if species else Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            test = serializer.save()
            return Response({"message": "Данные успешно добавлены", "id": test.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatisticsView(APIView):
    def get(self, request):
        stats = []
        species_data = Test.objects.values('species').annotate(
            total_tests=Count('id'),
            avg_milk_yield=Avg('milk_yield'),
            max_milk_yield=Max('milk_yield'),
            good_health_count=Count('id', filter=Q(health_status="good")),
        )
        for data in species_data:
            stats.append({
                "species": data['species'],
                "total_tests": data['total_tests'],
                "avg_milk_yield": data['avg_milk_yield'],
                "max_milk_yield": data['max_milk_yield'],
                "good_health_percentage": round((data['good_health_count'] / data['total_tests']) * 100, 2),
            })
        return Response({"statistics": stats}, status=status.HTTP_200_OK)