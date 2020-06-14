from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'admin'),
        (1, 'Operationnel'),
        (2, 'Regional'),
        (3, 'Central'),
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

class OperationnelUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class RegionalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class CentralUser(models.Model):
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
            operationnel = OperationnelUser(user=instance)
            operationnel.save()
            instance.profile_id = operationnel.id
            instance.save()
        elif(instance.user_type == 2):
            regional = RegionalUser(user=instance)
            regional.save()
            instance.profile_id = regional.id
            instance.save()
        elif(instance.user_type == 3):
            central = CentralUser(user=instance)
            central.save()
            instance.profile_id = central.id
            instance.save()
