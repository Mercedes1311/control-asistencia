from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_asistencia, name='registrar_asistencia'),
     path('asistencia_exitosa', views.asistencia_exitosa, name='asistencia_exitosa'),
    
]
