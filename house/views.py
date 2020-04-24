from django.shortcuts import render
from .models import Train
from .form import DemoForm
from .linear_regression import main


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def demo_page(request):
    form = DemoForm()
    return render(request, 'demo.html', {'form': form})


def chart_page(request):
    return render(request, 'others/chart.html')


def predict(request):
    form = DemoForm(request.POST)
    if form.is_valid():
        obj = Train.objects.all().order_by('-score')[0]
        accuracy = int(obj.score * 100)
        error = int(obj.rmse)

        room_number_total = form.cleaned_data['room_number_total']
        bathroom_number = form.cleaned_data['bathroom_number']
        bedroom_number = form.cleaned_data['bedroom_number']
        acreage = form.cleaned_data['acreage']
        build_year = form.cleaned_data['build_year']
        dist_to_center = form.cleaned_data['dist_to_center']
        dist_to_airport = form.cleaned_data['dist_to_airport']
        dist_to_station = form.cleaned_data['dist_to_station']
        price = (int(room_number_total) * obj.coef_num_room) + \
                (int(bathroom_number) * obj.coef_num_bath) + \
                (int(bedroom_number) * obj.coef_num_bed) + \
                (float(acreage) * obj.coef_living_area) + \
                (int(build_year) * obj.coef_year_built) + \
                (float(dist_to_center) * obj.coef_distance_to_citycenter) + \
                (float(dist_to_airport) * obj.coef_distance_to_airport) + \
                (float(dist_to_station) * obj.coef_distance_to_station) + obj.intercept

    context = {
        'form': form,
        'room_number_total': room_number_total,
        'bathroom_number': bathroom_number,
        'bedroom_number': bedroom_number,
        'acreage': acreage,
        'build_year': build_year,
        'dist_to_center': dist_to_center,
        'dist_to_airport': dist_to_airport,
        'dist_to_station': dist_to_station,
        'price': int(price),
        'accuracy': accuracy,
        'error': error
    }
    return render(request, 'predict.html', context)


def train(request):
    train = Train(
        coef_distance_to_citycenter=main()[0][0],
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
    obj = Train.objects.all().order_by('-score')
    return render(request, 'others/train.html', {'obj': obj})
