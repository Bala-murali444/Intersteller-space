from django.shortcuts import render
from .models import Astronuts

# Create your views here.
def inter(request):
    astros = Astronuts.objects.all()
    return render(request,"inter.html",{'astros':astros})