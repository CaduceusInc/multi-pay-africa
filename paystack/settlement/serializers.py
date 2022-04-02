from rest_framework import serializers


class FetchSettlementSerializer(serializers.Serializer):
    # query parameters
    perPage = serializers.IntegerField(default=10)
    page = serializers.IntegerField(default=1)

    # optional parameters
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    subaccount = serializers.CharField(max_length=255, required=False)


class FetchSettlementTransactionSerializer(serializers.Serializer):
    # query parameters
    perPage = serializers.IntegerField(default=10)
    page = serializers.IntegerField(default=1)

    # optional parameters
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
