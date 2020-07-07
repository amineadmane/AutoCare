from django.urls import path
from users.views import  AdminSign , UsersList , UserDetail, ObtainAuthToken

urlpatterns = [
    
    #List of users
    path('', UsersList.as_view()),
    
    #Detail of an user 
    path('<int:pk>/', UserDetail.as_view()),

    #User Login 
    path('login/', ObtainAuthToken.as_view(), name="login"),

    #Admin user create an accounts
    path('adminsign/', AdminSign.as_view()),
]
