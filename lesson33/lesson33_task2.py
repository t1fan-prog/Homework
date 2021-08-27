import concurrent.futures
import requests
import json


def file_manager(file_name: str, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


def upload_data(url, file_name):
    resp = requests.get(url)
    comments_list = json.loads(resp.text)
    comments_list['data'] = sorted(comments_list['data'], key=lambda k: k['retrieved_on'])

    file_manager(file_name, comments_list)


with concurrent.futures.ProcessPoolExecutor() as executor:
        p = executor.submit(upload_data, 'https://api.pushshift.io/reddit/comment/search/', 'comments.json')