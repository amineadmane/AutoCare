from django.db import models
from mission.models import Modele
# Create your models here.


class Piece (models.Model):
    reference = models.CharField(max_length=30, primary_key=True)
    date_aq = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    Nombre = models.PositiveIntegerField(null=False, blank=False)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE,)


class Guide_constructure(models.Model):
    observation = models.TextField(null=True, blank=True)
    piece = models.ForeignKey(Piece,  on_delete=models.CASCADE)


class Guide_personnel(models.Model):
    observation = models.TextField(null=True, blank=True)
    piece = models.ForeignKey(Piece,  on_delete=models.CASCADE)
