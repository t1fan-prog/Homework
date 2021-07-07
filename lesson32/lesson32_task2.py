import requests
import json


def file_manager(file_name: str, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


resp = requests.get('https://api.pushshift.io/reddit/comment/search/')
comments_list = json.loads(resp.text)
comments_list['data'] = sorted(comments_list['data'], key=lambda k: k['retrieved_on'])

file_manager('comments.json', comments_list)
