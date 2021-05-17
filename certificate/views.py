from django.shortcuts import render
from .models import Certificate
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
# Create your views here.
class newcourse(CreateView):
    model=Certificate
    fields = '__all__'


class listview(ListView):
        model = Certificate
        fields='__all__'
        context_object_name = "Certificate"

class update_view(UpdateView):
    model = Certificate
    fields = '__all__'


class delete_view(DeleteView):
    model = Certificate
    success_url = '/certificate/list'


class detail_view(DetailView):
    model = Certificate
