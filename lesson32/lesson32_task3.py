import requests
import json


class WeatherChecker:
    def __init__(self):
        lang = input('Choose language: 1 for English, 2 for Ukrainian, 3 for Russian\n')
        if lang not in ['1', '2', '3']:
            raise Exception("Don't type anything except 1, 2 or 3")
        else:
            self.lang = lang

    def check_info(self):
        if self.lang == '1':
            city = input('Enter city\n')
            return 'en', city
        elif self.lang == '2':
            city = input('Введiть мiсто\n')
            return 'ua', city
        else:
            city = input('Введите город\n')
            return 'ru', city

    def request(self):
        lang, city = self.check_info()
        resp = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&units=metric&appid=fd6f9beb714daf7ed24bd3c56b911512')
        dict_response = json.loads(resp.text)
        temp_info = dict_response['main']
        return temp_info


w = WeatherChecker()
info = w.request()

if w.lang == '1':
    print(f'Current temperature is {info["temp"]}, feels like {info["feels_like"]}')
elif w.lang == '2':
    print(f'Поточна температура становить {info["temp"]}, відчуває як {info["feels_like"]}')
else:
    print(f'Текущая температура {info["temp"]}, чувствуется как {info["feels_like"]}')
