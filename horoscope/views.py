from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_elements(request, element: str):
    # element_znaks = list(types)
    resp = ''
    zodiacs = types.get(element)
    for z in zodiacs:
        redirect_path = reverse('horoscope-name', args=[z])
        resp += f"<li> <a href='{redirect_path}' >{z} </a> <?li>"
    resp = f"<ol> {resp} </ol>"
    return HttpResponse(resp)


def get_types(request):
    li_elem = ''
    for t in list(types):
        redirect_path = reverse('type-name', args=[t])
        li_elem += f"<li> <a href='{redirect_path}'>{t} </a> </li>"
    resp = f"<ol> {li_elem} </ol>"
    return HttpResponse(resp)


def index(request):
    zodiacs = list(zodiac_dict)
    # li_elements = ''
    # for sign in zodiac:
    #     redirect_path = reverse("horoscope-name", args=[sign])
    #     li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    # response = f"""
    # <ol>
    #     {li_elements}
    # </ol>
    # """
    # return HttpResponse(response)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    #zodiacs = list(zodiac_dict)
    # if description:
    #    return HttpResponse(description)
    # else:
    #   return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")
    # response = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(response)
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_urls = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_urls)


def get_info_about_sign_zodiac_by_date(request, month: int, day: int):
    # return HttpResponse(f"месяц{month} день{day}")
    day = month * 30 + day
    index = (day - 80) // 30
    name_zodiac = list(zodiac_dict)[index - 1]
    redirect_urls = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_urls)

def get_kianu(request):
    data = {
        'year_born': 1978,
        'city_born': 'London',
        'movie_name': 'Apocalypsis'
    }
    return render(request, 'horoscope/kianu_html.html', context=data)

def get_beautiful_table(request):
    return render(request, 'horoscope/beautiful.html')

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'horoscope/guinnessworldrecords.html', context=context)
