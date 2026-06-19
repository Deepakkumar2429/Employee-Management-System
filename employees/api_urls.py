from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]