from .bulk_charges.views import *
from django.urls import path

urlpatterns = [
    path('initialize-charge/bulk/', InitiateBulkCharge.as_view(), name='initialize-charge-bulk'),
]

