from django.shortcuts import render
from .models import course_master
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import course_master
from django.http import HttpResponse


# Create your views here.

def chartdemo(request):
    return render(request,"course/course-chart.html")

class newcourse(LoginRequiredMixin,CreateView):
    model=course_master
    fields = '__all__'


class listview(LoginRequiredMixin,ListView):
        model = course_master
        fields='__all__'
        context_object_name = "course"
        authentication_classes = []
        permission_classes = []

def get(request):
            qs = course_master.objects.all()

            courses = []
            duration = []

            for item in qs:
                courses.append(item.name)
                duration.append(item.duration)

            data = {
                "course":courses,
                "dur":duration
            }
            print(data)
            return JsonResponse(data)


class update_view(LoginRequiredMixin,UpdateView):
    model = course_master
    fields = '__all__'


class delete_view(LoginRequiredMixin,DeleteView):
    model = course_master
    success_url = '/course/list'


class detail_view(LoginRequiredMixin,DetailView):
    model = course_master


def get_fees(request, course_id):
        course = course_master.objects.get(pk=course_id);
        return JsonResponse({'fees': course.fees});



