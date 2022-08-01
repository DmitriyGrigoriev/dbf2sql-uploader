from django.db import models

class DefaultModel(models.Model):
    """Abstract dfefault model"""
    is_global = True

    class Meta:
        abstract = True
