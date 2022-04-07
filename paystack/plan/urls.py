from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatePlan

routers = DefaultRouter()

routers.register(r"create-plan", CreatePlan, basename="create-plan")


urlpatterns = [
    path("", include(routers.urls)),
]
