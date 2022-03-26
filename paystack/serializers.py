from rest_framework import serializers
from .models import (Wallet, Invoice, Refund, Subaccount, VirtualAccounts, 
                     Subscription, Plan, Transaction)



class WalletSerializer(serializers.Serializer):
    
    class Meta:
        model = Wallet
        fields = '__all__'
        

class InvoiceSerializer(serializers.Serializer):
    
    class Meta:
        model = Invoice
        fields = '__all__'
        

class RefundSerializer(serializers.Serializer):
    
    class Meta:
        model = Refund
        fields = '__all__'
        

class SubaccountSerializer(serializers.Serializer):
    
    class Meta:
        model = Subaccount
        fields = '__all__'
        
class VirtualAccountSerializer(serializers.Serializer):
    
    class Meta:
        model = VirtualAccounts
        fields = '__all__'
        

class SubscriptionSerializer(serializers.Serializer):
    
    class Meta:
        model = Subscription
        fields = '__all__'
        
class PlanSerializer(serializers.Serializer):
    
    class Meta:
        model = Plan
        fields = '__all__'
        

class TransactionSerializer(serializers.Serializer):
    
    class Meta:
        model = Transaction
        fields = '__all__'
