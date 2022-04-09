from rest_framework import serializers
from paystack.models import Subaccount


class CreateSubAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subaccount
        fields = "__all__"


class ListSubaccountSerializer(serializers.Serializer):
    perPage = serializers.IntegerField(default=10)
    page = serializers.IntegerField(default=1)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)

    def validate(self, attrs):
        """
        Validate that the start date is not greater than the end date

        :param attrs: The dictionary of the data that was sent with the request
        :return: The serializer returns a dictionary with the question text, the start date, the end date,
        and the id of the question.
        """
        if attrs.get("start_date") > attrs.get("end_date"):
            raise serializers.ValidationError(
                "Start date cannot be greater than end date"
            )
        return attrs


class FetchSubAccountSerializer(serializers.Serializer):
    # This is a custom field that is used to validate the id or code of the subaccount.
    id_or_code = serializers.CharField(max_length=50, required=True)


class UpdateSubAccountSerializer(serializers.ModelSerializer):

    id_or_code = serializers.CharField(max_length=50, required=True)
    active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Subaccount
        fields = "__all__"
