
from rest_framework import viewsets
from paystackapi.paystack import Paystack
from rest_framework.response import Response
from decouple import config
from paystack.plan.serializers import CreatePlanSerializer

paystack = Paystack(secret_key="sk_test_1ca1d9f3f5278d5014396d126483ace85f2c3afb")


class CreatePlan(viewsets.ModelViewSet):
    serializer_class = CreatePlanSerializer
    http_method_names = ["post"]

    def create(self,request, *args, **kwargs):
        kwargs = self.serializer_class(data=self.request.data)
        kwargs.is_valid(raise_exception=True)
        kwargs.save()
        
        response = paystack.subscription.create(**kwargs.data)
        
        return Response(response)