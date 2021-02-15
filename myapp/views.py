from django.shortcuts import render,redirect
from .models import blog
from .forms import BlogForm

def createview(request):
    context={}
    form=BlogForm(request.POST)
    if form.is_valid():
        form.save()
        redirect('/')
    context['form']=form
    return render(request,'myapp/createview.html',context)
