from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')


def get_rectangle_area1(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')

def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width * width}')

def get_square_area1(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')

def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {round(radius * radius * pi, 2)}')

def get_circle_area1(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')

