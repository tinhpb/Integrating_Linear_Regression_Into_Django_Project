from django.shortcuts import render, redirect
from .models import Houses
from .form import DemoForm, ContactForm
from django.urls import reverse

### Home View
def home_page(request):
    house = Houses.objects.all()
    return render(request, 'home.html', {'house':house})

### About View
def about_page(request):
    return render(request, 'about.html', {})

### Contact view
def contact_page(request):
    return render(request, 'contact.html', {})

### Demo View
def demo_page(request):
    form=DemoForm()
    return render(request, 'demo.html', {'form':form})

### Predict View
def predict(request):
    form=DemoForm(request.POST)
    if form.is_valid():
        tongsp=form.cleaned_data['tongsophong']
        sopt=form.cleaned_data['sophongtam']
        sopn=form.cleaned_data['sophongngu']
        dt=form.cleaned_data['dientich']
        namxd=form.cleaned_data['namxaydung']
        gia=int(tongsp)*9205.00150399+int(sopt)*107011.67927086+int(sopn)*7125.6624795+float(dt)*1093.17116684+int(namxd)*-539.99163851 + 1120349.4349
    context = {'form':form, 'tongsp':tongsp, 'sopt':sopt, 'sopn':sopn, 'dt':dt, 'namxd':namxd,'gia':int(gia)}
    return render(request, 'predict.html', context)

### Load Data View
def load_house_data(request):
    house=Houses.objects.all()
    return render(request, 'others/load_house_data.html', {'house':house})
