from django.shortcuts import render
from students.models import student
from course.models import course_master
from admission.models import admission
from payment.models import payment_info
from inquiry_table.models import inquiry
import datetime
def home(request):
    return render(request,'users/layout1.html',{
        "studcount":student.objects.count(),
        "coursecount":course_master.objects.count(),
        "admissioncount":admission.objects.count(),
        "paymentcount":payment_info.objects.count(),
        "inquirycount":inquiry.objects.count()
    })

def login(request):
    return render(request,"users/sign-in.html")
# Create your views here.
