from django.urls import path
from blog import views
from django_distill import distill_path


app_name = "blog"

def get_index():
    return None

urlpatterns = [
    distill_path('', views.index,name="index", distill_func=get_index),
   
]

