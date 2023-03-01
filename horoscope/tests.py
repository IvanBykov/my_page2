from django.test import TestCase

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(200, response.status_code)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(200, response.status_code)
        self.assertIn(' Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())

    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7/')
        self.assertEqual(302, response.status_code)
        self.assertIn('/horoscope/libra/', response.url)

    def test_number_redirect(self):
        zodiacs = list(zodiac_dict)
        for i in range(1, 13):
            response = self.client.get(f'/horoscope/{i}/')
            self.assertEqual(302, response.status_code)
            self.assertIn(f'/horoscope/{zodiacs[i - 1]}', response.url)

    def test_signs(self):
        for sign in zodiac_dict:
            # print(sign)
            # print(zodiac_dict[sign])
            response = self.client.get(f'/horoscope/{sign}/')
            self.assertEqual(200, response.status_code)
            self.assertIn(zodiac_dict[sign], response.content.decode())
