from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import project

# Create your views here.
def index(request):
    my_portfolio = project.objects.all()
    return render(request,'index.html',{'profiles':my_portfolio})
