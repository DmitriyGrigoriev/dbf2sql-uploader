from django.db import models


class ExtBase(models.Model):
    """Extending base model table by additional fields"""
    # g07x = models.CharField(max_length=32, primary_key=True)
    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
            abstract = True
            managed = False
            unique_together = (('g071', 'g072', 'g073'),)


class ExtBaseG32(models.Model):
    """Extending base model table by additional fields"""
    # g07x = models.CharField(max_length=32, primary_key=True)
    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
            abstract = True
            managed = False
            unique_together = (('g071', 'g072', 'g073', 'g32'),)


class ExtBaseK32(models.Model):
    """Extending base model table by additional fields"""
    # g07x = models.CharField(max_length=32, primary_key=True)
    g071 = models.CharField(max_length=8, primary_key=True)

    class Meta:
            abstract = True
            managed = False
            unique_together = (('g071', 'g072', 'g073', 'k32'),)
