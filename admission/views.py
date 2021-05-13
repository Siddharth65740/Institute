from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import admission
from django.http import JsonResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class create_view(LoginRequiredMixin,CreateView):
    model =admission
    fields = '__all__'


class admissionListView(LoginRequiredMixin,ListView):
    model=admission
    fields ="__all__"
    context_object_name = "admission_list"

class admissionUpdateView(LoginRequiredMixin,UpdateView):
    model = admission
    fields = '__all__'

class detail_student(LoginRequiredMixin,DetailView):
    model = admission

class delete_student(LoginRequiredMixin,DeleteView):
    model = admission
    success_url = '/admission/list'

def get1(request):

    qs =admission.objects.all()

    Student = []
    Days = []
    print("inside get1");
    for item in qs:
        Student.append(item.Student.first_name)
        Days.append(item.No_of_Days)

    print("student :",Student);
    print("Days:",Days);

    data = {
        "Student": Student,
        "Days": Days
    }
    return JsonResponse(data)

def chartdemo1(request):
    return render(request,"course/course-chart.html")




