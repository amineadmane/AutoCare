from django.urls import path

from .views import stats_etat_vehicules,stats_etat_vehicules_per_modele,MarqueList,pourcentage_vehicules_per_marque,pourcentage_vehicules_per_modele,pourcentage_conducteurs_per_score, MarqueDetail,ModeleList,ModeleDetail,VehiculeList, ConducteurList, MissionList, VehiculeDetail, ConducteurDetail, MissionDetail

urlpatterns = [

    #GET marque list , POST new marque
    path('marque/', MarqueList.as_view()),
    #GET marque detail
    path('marque/<int:pk>/', MarqueDetail.as_view()),


    #GET modele list , POST new modele
    path('modele/', ModeleList.as_view()),
    #GET modele detail
    path('modele/<int:pk>/', ModeleDetail.as_view()),


    #GET vehicule list , POST new vehicule
    path('vehicule/', VehiculeList.as_view()),
    #GET vehicule detail
    path('vehicule/<int:pk>/', VehiculeDetail.as_view()),

    #GET conducteur list , POST new conducteur
    path('conducteur/', ConducteurList.as_view()),
    #GET conducteur detail
    path('conducteur/<int:pk>/', ConducteurDetail.as_view()),


    #GET mission list , POST new mission
    path('mission/', MissionList.as_view()),
    #GET mission detail
    path('mission/<int:pk>/', MissionDetail.as_view()),


    path('stats/conducteur/', pourcentage_conducteurs_per_score),

    path('stats/vehicule/', pourcentage_vehicules_per_marque),

    path('stats/vehicule/<int:marque>/', pourcentage_vehicules_per_modele),


    path('stats/vehicule/etats/', stats_etat_vehicules),

    path('stats/vehicule/etats/<int:marque>/', stats_etat_vehicules_per_modele),


   
]
