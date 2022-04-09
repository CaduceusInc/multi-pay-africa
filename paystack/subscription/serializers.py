from rest_framework import serializers
from paystack.models import Subscription


class CreateSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"