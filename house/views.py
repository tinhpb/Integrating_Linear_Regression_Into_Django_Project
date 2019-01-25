from django.shortcuts import render
from .models import Houses, Train
from .form import DemoForm, ContactForm
from .fusioncharts import FusionCharts
from collections import OrderedDict
from .linear_regression import main

### Home View
def home_page(request):
    count = Houses.objects.all().count()
    min = Houses.objects.all().order_by('askprice')[0]
    max = Houses.objects.all().order_by('-askprice')[0]
    return render(request, 'home.html',{'count':count, 'min':min, 'max':max})

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

def chart_page(request):
  return render(request, 'others/chart.html',{})

### Predict View
def predict(request):
    form=DemoForm(request.POST)
    if form.is_valid():
      obj = Train.objects.all().order_by('-score')[0] #sap xep theo score tu cao den thap, va lay thang dau tien
      dochinhxac=int(obj.score*100) #ep kieu de hien thi cho dep thoi
      saiso=int(obj.rmse) #ep kieu de hien thi cho dep thoi

      sophong=form.cleaned_data['sophong']
      sopt=form.cleaned_data['sophongtam']
      sopn=form.cleaned_data['sophongngu']
      dt=form.cleaned_data['dientich']
      namxd=form.cleaned_data['namxaydung']
      kc_trungtam=form.cleaned_data['kc_trungtam']
      kc_sanbay=form.cleaned_data['kc_sanbay']
      kc_taudienngam=form.cleaned_data['kc_taudienngam']
      gia=(int(sophong)*obj.coef_num_room)+(int(sopt)*obj.coef_num_bath)+(int(sopn)*obj.coef_num_bed)+(float(dt)*obj.coef_living_area)+(int(namxd)*obj.coef_year_built)+(float(kc_trungtam)*obj.coef_distance_to_citycenter)+(float(kc_sanbay)*obj.coef_distance_to_airport)+(float(kc_taudienngam)*obj.coef_distance_to_station) + obj.intercept

    context = {'form':form,'sophong':sophong, 'sopt':sopt, 'sopn':sopn, 'dt':dt, 'namxd':namxd, 'kc_trungtam':kc_trungtam, 'kc_sanbay':kc_sanbay, 'kc_taudienngam':kc_taudienngam, 'gia':int(gia), 'dochinhxac':dochinhxac, 'saiso':saiso}
    return render(request, 'predict.html', context)

def train(request):
  # khi co 1 request no se goi ham main() trong file linear_regression.py de train model, ket qua lay ra se duoc luu vao models Train
    train=Train(coef_distance_to_citycenter=main()[0][0],
      coef_distance_to_airport=main()[0][1],
      coef_distance_to_station=main()[0][2],
      coef_year_built=main()[0][3],
      coef_num_room=main()[0][4],
      coef_num_bed=main()[0][5],
      coef_num_bath=main()[0][6],
      coef_living_area=main()[0][7],
      intercept=main()[1],
      rmse=main()[2],
      score=main()[3],
      )
    train.save()
    obj=Train.objects.all().order_by('-score') #sap xep theo score tu cao den thap roi show len
    return render(request, 'others/train.html', {'obj':obj})
