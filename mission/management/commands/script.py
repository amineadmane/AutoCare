from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from mission.models import Vehicule

class Command(BaseCommand):
    """
        Script to collect data from youtube,
        execute python manage.py script
        
    """

    def handle(self, *args, **options):
        #every 24h check all "vehicules"
        vehicules = Vehicule.objects.all()
        for vehicule in vehicules:
            dateProchaineRevision = vehicule.dateProchaineRevision
            today = datetime.now()
            d1 = datetime.strptime(dateProchaineRevision, "%Y-%m-%d")
            d2 = datetime.strptime(today, "%Y-%m-%d")
            diff = abs((d2 - d1).days) / 30
            if diff <= 9:
                vehicule.update(etat="MAUVAIS")
            elif diff <= 18:
                vehicule.update(etat="MOYEN")
            else:
                vehicule.update(etat="BON")
