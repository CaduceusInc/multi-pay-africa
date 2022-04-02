from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateSubAccount

routers = DefaultRouter()

routers.register(r"create-subaccount", CreateSubAccount, basename="create-subaccount")


urlpatterns = [
    path("", include(routers.urls)),
]
