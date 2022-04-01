from .serializers import SettlementSerializer
from rest_framework import viewsets
from paystackapi.paystack import Paystack
from decouple import config

paystack = Paystack(config('PAYSTACK_SECRET_KEY'))

class SettlementFetch(viewsets.ModelViewSet):
    serializer_class = SettlementSerializer

    def retrieve(self, request, *args, **kwargs):
        settlement = paystack.settlement.fetch(kwargs['pk'])
        return self.serializer_class(settlement).data
