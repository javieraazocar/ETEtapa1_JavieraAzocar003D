from .forms import ProovedorForm
from django.shortcuts import render, redirect
from .models import Proovedor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ver(request):
    return render(request, 'ver.html')

def crearProovedor(request):
    if request.method == 'POST':
      proovedor_form = ProovedorForm(request.POST)
      if proovedor_form.is_valid():
         proovedor_form.save()
         return redirect('index')
    else:
        proovedor_form = ProovedorForm()
    return render(request, 'index.html',{'proovedor_form': proovedor_form })

def Ver(request):
    proovedor=Proovedor.objects.all()
    return render (request, 'ver.html', context={'datos':proovedor})

def form_ModProovedor(request,id):
    pro=Proovedor.objects.get(id=id)
    
    datos ={
        'form':ProovedorForm(instance=pro)
    }
    if request.method == 'POST':
        formulario = ProovedorForm(data=request.POST, instance= pro)
        if formulario.is_valid:
         formulario.save()
         return redirect('ver')
    return render(request,'form_ModProovedor.html', datos)

def form_delProovedor(request, id):
    pro= Proovedor.objects.get(id=id)
    pro.delete()
    return redirect('ver')