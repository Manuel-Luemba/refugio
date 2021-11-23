from django.urls import path
from apps.adopcao.views import index_adopcao

urlpatterns = [
    path('',index_adopcao, name='adopcao'),
]
