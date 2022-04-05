from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SettlementFetch

routers = DefaultRouter()

routers.register(r"settlement-fetch", SettlementFetch, basename="settlement")


urlpatterns = [
    path("", include(routers.urls)),
]
