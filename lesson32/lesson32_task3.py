import requests


def check_info():
    lang = input('Choose language: 1 for English, 2 for Ukrainian, 3 for Russian\n')
    if lang not in ['1', '2', '3']:
        raise Exception("Don't type anything except 1, 2 or 3")

    if lang == '1':
        city = input('Enter city\n')
        return 'en', city
    elif lang == '2':
        city = input('Введiть мiсто\n')
        return 'ua', city
    else:
        city = input('Введите город\n')
        return 'ru', city


class WeatherChecker:
    city = None
    lang = None

    def request(self):
        resp = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&lang={self.lang}&units=metric&appid=fd6f9beb714daf7ed24bd3c56b911512')
        dict_response = resp.json()
        temp_info = dict_response['main']
        return temp_info

    def get_current_weather(self):
        info = self.request()
        curent_temp = info["temp"]
        feels_like = info["feels_like"]
        return curent_temp, feels_like


class WeatherCheckerUa(WeatherChecker):
    def __init__(self, city):
        self.lang = 'ua'
        self.city = city.title()

    def return_current_weather(self):
        temp, feels_like = self.get_current_weather()
        return f'Поточна температура в мiстi {self.city} становить {temp}, відчуває як {feels_like}'


class WeatherCheckerRu(WeatherChecker):
    def __init__(self, city):
        self.lang = 'ru'
        self.city = city.title()

    def return_current_weather(self):
        temp, feels_like = self.get_current_weather()
        return f'Текущая температура в городе {self.city}: {temp}, чувствуется как {feels_like}'


class WeatherCheckerEn(WeatherChecker):
    def __init__(self, city):
        self.lang = 'en'
        self.city = city.title()

    def return_current_weather(self):
        temp, feels_like = self.get_current_weather()
        return f'Current temperature in {self.city} is {temp}, feels like {feels_like}'


lang, city = check_info()

if lang == 'ua':
    print(WeatherCheckerUa(city).return_current_weather())
elif lang == 'ru':
    print(WeatherCheckerRu(city).return_current_weather())
else:
    print(WeatherCheckerEn(city).return_current_weather())

