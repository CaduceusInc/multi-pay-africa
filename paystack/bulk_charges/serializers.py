from rest_framework import serializers


class BulkChargeSerializer(serializers.Serializer):
    # query parameters
    authorization = serializers.CharField(max_length=255, required=True)
    amount = serializers.IntegerField(required=True)
