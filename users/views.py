from django.shortcuts import render
from students.models import student

def home(request):
    return render(request,'users/layout1.html',{
        "scount":student.objects.count()
    })

def login(request):
    return render(request,"users/sign-in.html")
# Create your views here.
