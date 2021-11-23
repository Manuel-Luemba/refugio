from django.urls import path

from apps.mascota import views
from apps.mascota.views import index, mascota_add

urlpatterns = [
    path('',index,name='index'),
    path('novo/',mascota_add,name='mascota_add'),
]
