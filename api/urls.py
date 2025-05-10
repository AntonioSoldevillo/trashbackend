# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/items/', views.create_item, name='create_item'),
    path('api/classification-results/', views.create_classification_result, name='create_classification_result'),
]
