from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

day_dict = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}


def get_info_about_days(request, days: str):
    if days == 'monday':
        return HttpResponse("Провести понедельник")
    elif days == 'tuesday':
        return HttpResponse("Провести вторник")
    elif days == 'wednesday':
        return HttpResponse("Провести среду")
    elif days == 'thursday':
        return HttpResponse("Провести четверг")
    elif days == 'friday':
        return HttpResponse("Провести пятницу")
    elif days == 'saturday':
        return HttpResponse("Провести субботу")
    elif days == 'sunday':
        return HttpResponse("Провести воскресенье")
    else:
        return HttpResponseNotFound(f"неизвестный день недели {days}")


def get_info_about_days_by_number(request, days: int):
    #days_list = list(day_dict)
    if len(day_dict) < days:
        return HttpResponseNotFound(f'Неправильный номер дня недели {days}')
    #name_day = days_list[days-1]
    return HttpResponseRedirect(f'/todo_week/{day_dict.get(days)}/')

