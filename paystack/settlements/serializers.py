from rest_framework import serializers

class SettlementSerializer(serializers.Serializer):
    #query parameters
    per_page = serializers.IntegerField(default=10)
    page = serializers.IntegerField(default=1)
    
    #optional parameters
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    subaccount = serializers.DateTimeField()

