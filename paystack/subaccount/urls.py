from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateSubAccount, ListSubAccount, FetchSubAccount, UpdateSubAccout

routers = DefaultRouter()

routers.register(r"create-subaccount", CreateSubAccount, basename="create-subaccount")
routers.register(r"list-subaccount", ListSubAccount, basename="list-subaccount")
routers.register(r"fetch-subaccount", FetchSubAccount, basename="fetch-subaccount")
routers.register(r"update-subaccount", UpdateSubAccout, basename="update-subaccount")


urlpatterns = [
    path("", include(routers.urls)),
]
