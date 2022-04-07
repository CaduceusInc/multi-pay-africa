from .bulk_charges.views import *
from django.urls import path, include


urlpatterns = [
    path("settlement/", include("paystack.settlement.urls")),
    path("subaccount/", include("paystack.subaccount.urls")),
    path('bulkcharge/', include('paystack.bulk_charges.urls')),
    path('subscription/', include('paystack.subscription.urls')),
    path('plan/', include('paystack.plan.urls')),
]
