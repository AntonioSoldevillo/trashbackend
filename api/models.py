# models.py
from django.db import models

class ClassificationResult(models.Model):
    label = models.CharField(max_length=100)
    confidence = models.FloatField()

    def __str__(self):
        return f"{self.label} ({self.confidence})"

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
