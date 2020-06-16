from django.contrib import admin
from .models import Vehicule, Conducteur, Mission, Marque, Modele
# Register your models here.
admin.site.register(Marque)
admin.site.register(Modele)
admin.site.register(Vehicule)
admin.site.register(Conducteur)
admin.site.register(Mission)
