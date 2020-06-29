from django.urls import path

from .views import PieceList, PieceDetail, Guide_constructureList, Guide_constructureDetail, Guide_personnelList, Guide_personnelDetail

urlpatterns = [

    #GET marque list , POST new marque
    path('piece/', PieceList.as_view()),
    #GET marque detail
    path('piece/<slug:pk>/', PieceDetail.as_view()),


    #GET Guide_constructure list , POST new Guide_constructure
    path('guide_constructeur/', Guide_constructureList.as_view()),
    #GET Guide_constructure detail
    path('guide_constructeur/<int:pk>/', Guide_constructureDetail.as_view()),

   

    #GET Guide_personnel list , POST new Guide_personnel
    path('guide_personnel/', Guide_personnelList.as_view()),
    #GET Guide_constructure detail
    path('guide_personnel/<int:pk>/', Guide_personnelDetail.as_view()),

   
]
