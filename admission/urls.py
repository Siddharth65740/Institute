from .views import create_view,admissionListView,admissionUpdateView,detail_student,delete_student,chartdemo1,get1
from django.urls import path

urlpatterns=[
    path("new/",create_view.as_view(),name="admission-create"),
    path("list/",admissionListView.as_view(),name="admission-list"),
    path("<int:pk>/update", admissionUpdateView.as_view(), name="admission-update"),
    path("detail/<int:pk>",detail_student.as_view(),name="admission-detail"),
    path("delete/<int:pk>", delete_student.as_view(), name="admission-delete"),
    path("chart/", chartdemo1, name="chart"),
    path("get_chart_Data/",get1,name="get-chart")
]