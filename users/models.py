from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save 
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'admin'),
        (1, 'Chef de service'),
        (2, 'Chef de parc'),
        (3, 'Responsable de maintencance'),
        (4, 'Conduteur'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    profile_id = models.IntegerField(default=0,blank=True,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_type']


    def __str__(self):
        return self.username
 
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        
class ChefService(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class ChefParc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class RespMaintencance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Conducteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):   
    if created:
        if(instance.user_type == 0):
            admin = Admin(user=instance)
            admin.save()
            instance.profile_id = admin.id
            instance.save()
        elif(instance.user_type == 1):
            chefservice = ChefService(user=instance)
            chefservice.save()
            instance.profile_id = chefservice.id
            instance.save()
        elif(instance.user_type == 2):
            chefparc = ChefParc(user=instance)
            chefparc.save()
            instance.profile_id = chefparc.id
            instance.save()
        elif(instance.user_type == 3):
            respmaintencance = RespMaintencance(user=instance)
            respmaintencance.save()
            instance.profile_id = respmaintencance.id
            instance.save()
        elif(instance.user_type == 4):
            conducteur = Conducteur(user=instance)
            conducteur.save()
            instance.profile_id = conducteur.id
            instance.save()