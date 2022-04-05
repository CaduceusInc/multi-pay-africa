from .serializers import BulkChargeSerializer
from rest_framework import viewsets
from paystackapi.paystack import Paystack
from decouple import config

# paystack = Paystack(config('PAYSTACK_SECRET_KEY'))
paystack = Paystack('sk_test_1ca1d9f3f5278d5014396d126483ace85f2c3afb')


class InitiateBulkCharge(viewsets.ModelViewSet):
    serializer_class = BulkChargeSerializer(many=True)
    bulk_list = []

    def create(self, request, *args, **kwargs):
        # bulk charge intialization takes a list of dictionaries containing authorization, amount

        bulk_charge = paystack.bulk_charge.initialize(request.data)

        return bulk_charge.data
