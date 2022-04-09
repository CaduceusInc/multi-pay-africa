from click import password_option
from .serializers import (
    CreateSubAccountSerializer,
    FetchSubAccountSerializer,
    ListSubaccountSerializer,
    UpdateSubAccountSerializer,
)
from rest_framework import viewsets
from paystackapi.paystack import Paystack
from rest_framework.response import Response
from decouple import config

paystack = Paystack(secret_key="sk_test_1ca1d9f3f5278d5014396d126483ace85f2c3afb")


class CreateSubAccount(viewsets.ModelViewSet):

    serializer_class = CreateSubAccountSerializer

    http_method_names = ["post"]

    def create(self, *args, **kwargs):
        kwargs = self.serializer_class(data=self.request.data)
        kwargs.is_valid(raise_exception=True)
        response = paystack.subaccount.create(**kwargs.data)
        return Response(response)


class ListSubAccount(viewsets.ModelViewSet):

    serializer_class = ListSubaccountSerializer

    http_method_names = ["post"]

    def create(self, *args, **kwargs):
        kwargs = self.serializer_class(data=self.request.data)
        kwargs.is_valid(raise_exception=True)
        response = paystack.subaccount.list(**kwargs.data)
        return Response(response)


class FetchSubAccount(viewsets.ModelViewSet):

    serializer_class = FetchSubAccountSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        id_or_code = serializer.validated_data.get("id_or_code")
        response = paystack.subaccount.fetch(id_or_code)
        return Response(response)


class UpdateSubAccout(viewsets.ModelViewSet):
    
        serializer_class = UpdateSubAccountSerializer
        http_method_names = ["post"]
    
        def create(self, request, *args, **kwargs):
            kwargs = self.serializer_class(data=self.request.data)
            kwargs.is_valid(raise_exception=True)
            id_or_code = kwargs.validated_data.get("id_or_code")
            response = paystack.subaccount.update(id_or_code, **kwargs.validated_data)
            return Response(response)
