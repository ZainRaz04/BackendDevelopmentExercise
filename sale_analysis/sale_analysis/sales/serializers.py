from rest_framework import serializers

class RepPerformanceDataSerializer(serializers.Serializer):
    rep_id = serializers.CharField()
class PerformanceTrendDataSerializer(serializers.Serializer):
    time_period = serializers.CharField()

class TeamPerformanceDataSerializer(serializers.Serializer):
    pass

class QuerySerializer(serializers.Serializer):
    representative_id = serializers.IntegerField(required=False)
    
