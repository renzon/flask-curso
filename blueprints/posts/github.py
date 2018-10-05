import requests


def avatar(name):
    resp = requests.get(f'https://api.github.com/users/{name}')
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(avatar('renzon'))
