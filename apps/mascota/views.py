from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from apps.mascota.forms import MascotaForm


def index(request):
    return render(request,'mascota/index.html')


def mascota_add (request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index ')
    else:
        form = MascotaForm()
    return render(request, 'mascota/add.html',{'form':form})
