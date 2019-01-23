from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects # This is how u grab the data from the DataBase
    return render(request,'jobs/home.html',{'jobs':jobs})
