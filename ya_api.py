import requests
from token_ya import token

def create_folder(name):
    headers_make_path = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'}

    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    path = name
    r = requests.put(f'{url}?path={path}', headers=headers_make_path)
    res = requests.get(f'{url}?path={path}', headers=headers_make_path)
    print(res)
    return res

create_folder("aaa")