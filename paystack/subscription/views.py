from click import password_option
from rest_framework import viewsets
from paystackapi.paystack import Paystack
from rest_framework.response import Response
from decouple import config
from paystack.subscription.serializers import CreateSubscriptionSerializer

paystack = Paystack(secret_key="sk_test_1ca1d9f3f5278d5014396d126483ace85f2c3afb")


class CreateSubscription(viewsets.ModelViewSet):
    serializer_class = CreateSubscriptionSerializer
    http_method_names = ["post"]

    def create(self,request, *args, **kwargs):
        kwargs = self.serializer_class(data=self.request.data)
        kwargs.is_valid(raise_exception=True)
        response = paystack.subscription.create(**kwargs.data)
        return Response(response)