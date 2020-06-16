from django.contrib import admin

# Register your models here.
from .models import RapportSignalProbleme, RapportSignalChauffeur, RapportSignalSinistre
# Register your models here.
admin.site.register(RapportSignalProbleme)
admin.site.register(RapportSignalChauffeur)
admin.site.register(RapportSignalSinistre)