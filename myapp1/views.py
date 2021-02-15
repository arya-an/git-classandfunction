from django.shortcuts import render,redirect
from classbasedAPP.models import GeekModel
from .forms import GeekForm

def createview(request):
    context={}
    form = GeekForm(request.POST)
    if form.is_valid():
        form.save()
        redirect('/')
    context['form']=form
    return render(request,'myapp1/createview.html',context)

