from django.urls import path
from . import views

urlpatterns = [
    path('api/classification-results/', views.classification_results, name='classification_results'),
]
