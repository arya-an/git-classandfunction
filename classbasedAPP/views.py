from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import GeekForm


class MyView(View):
    def get(self,request):
        return HttpResponse('result') 

class GeekCreate(CreateView):
    model = GeekModel
    fields = ['title','description']
    sucess_url = '/'
    

class GeeksList(ListView):
    model = GeekModel

class GeeksDetailView(DetailView):
    model = GeekModel

class GeeksUpadateView(UpdateView):
    model = GeekModel
    fields = [
        "title",
        "description",
    ]
    success_url = "/"

class GeeksDeleteView(DeleteView):
    model = GeekModel
    success_url = "/"

class GeeksFormView(FormView):
    form_class = GeekForm
    template_name = "classbased/geeksmodel_form.html"
    success_url = "/"



    
 