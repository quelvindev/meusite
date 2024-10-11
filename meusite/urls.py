from django.urls import path
from meusite import views
from django_distill import distill_path


app_name = "meusite"

def get_index():
    return None

urlpatterns = [
    distill_path('', views.index,name="index", distill_func=get_index),
   
]

