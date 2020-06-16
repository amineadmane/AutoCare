from django.db import models
from users.models import User
# Create your models here.

class Vehicule(models.Model):
    matriculeInterne = models.CharField(max_length = 30, null=True, blank=True)
    matriculeExcterne = models.CharField(max_length = 30, null=True, blank=True)
    marque = models.CharField(max_length = 30, null=True, blank=True)
    kilometrage = models.IntegerField(blank=True,null=True)
    modele_id = models.IntegerField(blank=True,null=True)
    date_aq = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)
    REGION_CHOICES = (
        (1, 'region-1'),
        (2, 'region-2'),
        (3, 'region-3'),
        (4, 'region-4'),
        (5, 'region-5'),
        (6, 'region-6'),

    )
    region = models.PositiveSmallIntegerField(choices=REGION_CHOICES)
    unite = models.CharField(max_length = 30, null=True, blank=True)
    service = models.CharField(max_length = 30, null=True, blank=True)
    CATEGORIE_CHOICES = (
        ('A', 'Categorie A'),
        ('B', 'Categorie B'),
        ('C', 'Categorie C'),
    )
    categorie = models.CharField(max_length = 1, choices=CATEGORIE_CHOICES)
    ETAT_CHOICES = (
        ('HDS', 'HORS DE SERVICE'),
        ('MAUVAIS', 'MAUVAIS'),
        ('MOYEN', 'MOYEN'),
        ('BON', 'BON'),
    )
    etat = models.CharField(max_length = 30, choices=ETAT_CHOICES)
    dateProchaineRevision = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)


class Conducteur(models.Model):
    nss = models.IntegerField()
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    dateNaissance = models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)
    tel = models.CharField(max_length = 30, null=True, blank=True)
    grade = models.CharField(max_length = 30, null=True, blank=True)
    dateEmbauche = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    REGION_CHOICES = (
        (1, 'region-1'),
        (2, 'region-2'),
        (3, 'region-3'),
        (4, 'region-4'),
        (5, 'region-5'),
        (6, 'region-6'),

    )
    region = models.PositiveSmallIntegerField(choices=REGION_CHOICES)
    unite = models.CharField(max_length = 30, null=True, blank=True)
    service = models.CharField(max_length = 30, null=True, blank=True)
    SCORE_CHOICES = zip( range(1,101), range(1,101) )
    score = models.IntegerField(default=100,choices=SCORE_CHOICES)
    photo = models.CharField(max_length = 255, null=True, blank=True)


    def __str__(self):
        return self.nom + " " + self.prenom



class Mission(models.Model):
    redacteur = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    vehicule = models.ForeignKey(Vehicule,on_delete=models.CASCADE, null=False)
    conducteur = models.ForeignKey(Conducteur,on_delete=models.CASCADE, null=False)
    point_depart = models.CharField(max_length = 30)
    point_arrive = models.CharField(max_length = 30)
    dateMission = models.DateField(auto_now=False,auto_now_add=False)
    distance = models.IntegerField()
    commentaire = models.TextField()
    heureDepart = models.TimeField(auto_now=False,auto_now_add=False)
    heureArrive = models.TimeField(auto_now=False,auto_now_add=False)
