from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_adopcao (request):
    return render(request,'adopcao/index.html');
