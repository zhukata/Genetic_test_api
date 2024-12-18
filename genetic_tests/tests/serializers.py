from rest_framework import serializers

from genetic_tests.tests.models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


# class StatisticksSerializer(serializers.ModelSerializer):
#     total_tests=
#     avg_milk_yield=
#     max_milk_yield=
#     good_health_percentage=
    
#     class Meta:
#         model = Test
#         fields = ()