from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    # return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')
    return render(request, 'geometry/rectangle.html')


def get_rectangle_area1(request, width: int, height: int):
    return HttpResponseRedirect(reverse('rectangle-name', args=[width, height]))


def get_square_area(request, width: int):
    #return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width * width}')
    return render(request, 'geometry/square.html')


def get_square_area1(request, width: int):
    return HttpResponseRedirect(reverse('square-name', args=[width]))


def get_circle_area(request, radius: int):
    #return HttpResponse(f'Площадь круга радиусом {radius} равна {round(radius * radius * pi, 2)}')
    return render(request, 'geometry/circle.html')


def get_circle_area1(request, radius: int):
    return HttpResponseRedirect(reverse('circle-name', args=[radius]))
