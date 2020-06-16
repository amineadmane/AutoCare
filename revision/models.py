from django.db import models
from piece.models import Piece
from mission.models import Vehicule
# Create your models here.


class Revision(models.Model):
    discription = models.TextField(null=True, blank=True)
    matricule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, null=True, blank=True)
    pieces = models.ManyToManyField(Piece)
