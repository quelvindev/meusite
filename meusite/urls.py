from django.urls import path
from meusite import views


app_name = "meusite"


urlpatterns = [
    path('', views.index,name="index"),
   
]

