from .views import *
from django.urls import path

urlpatterns = [
    path(
        "initialize-charge/bulk/",
        InitiateBulkCharge.as_view({"post": "list"}),
        name="initialize-charge-bulk",
    ),
]
