from django.urls import path
from .views import crearProovedor, index,ver

urlpatterns = [
    path('', index, name='index'),
    path('ver', ver, name='ver'),
    path('crearProovedor', crearProovedor, name="crearProovedor"),

]