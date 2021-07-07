import requests


def file_manager(file_name: str, data):
    with open(file_name, 'w') as f:
        f.write(data)


resp = requests.get('https://en.wikipedia.org/wiki/Robot')

file_manager('robots.txt', resp.text)
