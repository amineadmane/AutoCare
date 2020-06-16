from django.urls import path

from .views import VehiculeList, ConducteurList, MissionList, VehiculeDetail, ConducteurDetail, MissionDetail

urlpatterns = [

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


   
]
