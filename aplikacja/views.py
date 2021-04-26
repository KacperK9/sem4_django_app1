from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Car

def test_f(request):
    all_cars = Car.objects.all()
    length = len(all_cars)
    return render(request, 'filmy.html', {
        'cars' : all_cars,
        'cars_length' : length
    } )
