from .serializers import FetchSettlementSerializer
from rest_framework import viewsets
from paystackapi.paystack import Paystack
from rest_framework.response import Response
from decouple import config

paystack = Paystack(secret_key="sk_test_1ca1d9f3f5278d5014396d126483ace85f2c3afb")


class SettlementFetch(viewsets.ModelViewSet):
    serializer_class = FetchSettlementSerializer

    http_method_names = ["post"]

    def create(self, *args, **kwargs):
        kwargs = self.serializer_class(data=self.request.data)
        kwargs.is_valid(raise_exception=True)
        response = paystack.settlement.fetch(**kwargs.data)
        return Response(response)
