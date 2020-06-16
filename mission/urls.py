from django.urls import path

from .views import MarqueList,MarqueDetail,ModeleList,ModeleDetail,VehiculeList, ConducteurList, MissionList, VehiculeDetail, ConducteurDetail, MissionDetail

urlpatterns = [

    #GET marque list , POST new marque
    path('marque/', MarqueList.as_view()),
    #GET marque detail
    path('marque/<int:pk>/', MarqueDetail.as_view()),


    #GET modele list , POST new modele
    path('modele/', ModeleList.as_view()),
    #GET modele detail
    path('modele/<int:pk>/', ModeleDetail.as_view()),


    #GET conducteur list , POST new conducteur
    path('conducteur/', ConducteurList.as_view()),
    #GET conducteur detail
    path('conducteur/<int:pk>/', ConducteurDetail.as_view()),


    #GET mission list , POST new mission
    path('mission/', MissionList.as_view()),
    #GET mission detail
    path('mission/<int:pk>/', MissionDetail.as_view()),


   
]
