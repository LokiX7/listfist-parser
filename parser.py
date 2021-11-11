import requests
from bs4 import BeautifulSoup 
import json

HOST = 'https://listfist.com/'
URL = 'https://listfist.com/list-of-one-piece-manga-chapters'
HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }


def get_html(url, headers):
    req = requests.get(url, headers=headers, params='')
    return req


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('tbody')
    episodes = []

    for item in items:
        episodes.append(
                {
                'Number': item.find('td', class_='col-1 odd').get_text(),
                'Name': item.find('td', class_='col-2 even').get_text(),
                'Date': item.find('td', class_='col-3 odd').get_text()
                }
            )
    return episodes


def save_data(data, path, name):
    with open(path + name, 'w') as file:
        json.dump(data, file)


def parser(url, headers, file_name, path_to_save=''):
    html = get_html(url, headers)
    if html.status_code == 200:
        episodes = get_content(html.text)
        save_data(episodes, path_to_save, file_name)
        print('Done!')
    else:
        print(f'Error. Status code: {html.status_code}')


if __name__ == '__main__':
    url = input('url page: ')
    parser(url, HEADERS, 'episodes_json')
    input()
