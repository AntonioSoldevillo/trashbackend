from rest_framework import viewsets
from .models import ClassificationResult
from .serializers import ClassificationResultSerializer

class ClassificationResultViewSet(viewsets.ModelViewSet):
    queryset = ClassificationResult.objects.all()
    serializer_class = ClassificationResultSerializer
