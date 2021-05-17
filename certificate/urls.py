from django.urls import path
from .views import newcourse,listview,update_view,delete_view,detail_view

urlpatterns=[
    path("new/",newcourse.as_view(),name="certificate-new"),
    path("list/",listview.as_view(),name="certificate-list"),
    path("update/<int:pk>",update_view.as_view(),name="certificate-update"),
    path("view/<int:pk>",detail_view.as_view(),name="certificate-view"),
    path("delete/<int:pk>",delete_view.as_view(),name="certificate-delete"),
    ]