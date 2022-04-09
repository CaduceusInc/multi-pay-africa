from rest_framework import serializers
from paystack.models import Plan


class CreatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"