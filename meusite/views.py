from django.shortcuts import render

# Create your views here.

def index(request):
      
    conext = {

    }
    return render(request,'meusite/index.html',conext)