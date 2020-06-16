from django.db import models
from mission.models import Vehicule, Conducteur
from users.models import User
# Create your models here.


class RapportSignalProbleme(models.Model):
    description = models.TextField(null=False, blank=False)
    vehicule = models.ForeignKey(Vehicule,on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now=False,auto_now_add=False, null=False, blank=False)
    redacteur = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    GRAVITE_CHOICES = (
        ('FAIBLE', 'FAIBLE'),
        ('MOYEN', 'MOYEN'),
        ('FORT', 'FORT'),
        ('CRITIQUE', 'CRITIQUE'),
    )
    gravite = models.CharField(max_length=20,choices=GRAVITE_CHOICES)
    TYPE_PROBLEME_CHOICES = (
        ('PANNE', 'PANNE'),
        ('JCP', 'JCP'),
    )
    type_probleme = models.CharField(max_length=30,choices=TYPE_PROBLEME_CHOICES)
    confirmed = models.BooleanField(default=False)



class RapportSignalChauffeur(models.Model):
    description = models.TextField(null=False, blank=False)
    conducteur = models.ForeignKey(Conducteur,on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now=False,auto_now_add=False, null=False, blank=False)
    redacteur = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    GRAVITE_CHOICES = (
        ('FAIBLE', 'FAIBLE'),
        ('MOYEN', 'MOYEN'),
        ('FORT', 'FORT'),
        ('CRITIQUE', 'CRITIQUE'),
    )
    gravite = models.CharField(max_length=20,choices=GRAVITE_CHOICES)


class RapportSignalSinistre(models.Model):
    description = models.TextField(null=False, blank=False)
    vehicule = models.ForeignKey(Vehicule,on_delete=models.CASCADE, null=False)
    conducteur = models.ForeignKey(Conducteur,on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now=False,auto_now_add=False, null=False, blank=False)
    redacteur = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    GRAVITE_CHOICES = (
        ('FAIBLE', 'FAIBLE'),
        ('MOYEN', 'MOYEN'),
        ('FORT', 'FORT'),
        ('CRITIQUE', 'CRITIQUE'),
    )
    gravite = models.CharField(max_length=20,choices=GRAVITE_CHOICES)
