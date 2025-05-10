from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassificationResultViewSet

router = DefaultRouter()
router.register(r'classification-results', ClassificationResultViewSet, basename='classificationresult')

urlpatterns = [
    path('api/', include(router.urls)),
]
