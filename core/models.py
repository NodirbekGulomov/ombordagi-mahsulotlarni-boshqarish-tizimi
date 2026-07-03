from django.db import models


# Create your models here.
class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100, unique=True)
    turi = models.CharField(max_length=50)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    soni = models.PositiveIntegerField()
    chegirma_foizi = models.PositiveIntegerField(default=0)
    tavsifi = models.TextField(blank=True)
    sotuvda = models.BooleanField(default=True)
