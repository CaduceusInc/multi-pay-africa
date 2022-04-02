from rest_framework import serializers
from paystack.models import Subaccount


class CreateSubAccountSerializer(serializers.Model):

    class Meta:
        model = Subaccount
        fields = '__all__'
        

