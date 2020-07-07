from django.urls import path

from .views import (RapportSignalProblemeList, RapportSignalProblemeDetail,InValidateRapportSignalProbleme,ValidateRapportSignalProbleme,
                    RapportSignalChauffeurList, RapportSignalChauffeurDetail,
                    RapportSignalSinistreList, RapportSignalSinistreDetail) 

urlpatterns = [

    #GET RapportSignalProbleme list , POST new RapportSignalProbleme
    path('signalprobleme/', RapportSignalProblemeList.as_view()),
    #GET RapportSignalProbleme detail
    path('signalprobleme/<int:pk>/', RapportSignalProblemeDetail.as_view()),

    #PATCH  VALIDER RapportSignalProbleme 
    path('signalprobleme/<int:pk>/valider/', ValidateRapportSignalProbleme.as_view()),
    #PATCH  VALIDER RapportSignalProbleme 
    path('signalprobleme/<int:pk>/invalider/', InValidateRapportSignalProbleme.as_view()),


    #GET RapportSignalChauffeur list , POST new RapportSignalChauffeur
    path('signalchauffeur/', RapportSignalChauffeurList.as_view()),
    #GET RapportSignalChauffeur detail
    path('signalchauffeur/<int:pk>/', RapportSignalChauffeurDetail.as_view()),


    #GET RapportSignalSinistre list , POST new RapportSignalSinistre
    path('signalsinistre/', RapportSignalSinistreList.as_view()),
    #GET RapportSignalSinistre detail
    path('signalsinistre/<int:pk>/', RapportSignalSinistreDetail.as_view()),


   
]
