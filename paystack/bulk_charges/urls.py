from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register(r"initialize-charge-bulk",InitiateBulkCharge,basename="initialize-charge-bulk" )

urlpatterns = [
    path('', include(routers.urls)),
    # path(
    #     "initialize-charge/bulk/",
    #     InitiateBulkCharge.as_view({"post": "list"}),
    #     name="initialize-charge-bulk",
    # ),
]
