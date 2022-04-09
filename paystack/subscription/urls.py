from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateSubscription

routers = DefaultRouter()

routers.register(r"create-subscription", CreateSubscription, basename="create-subscription")


urlpatterns = [
    path("", include(routers.urls)),
]
