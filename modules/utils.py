import requests
from bs4 import BeautifulSoup

class Utils:

    def __init__(self):
        pass

    def get_episode_escuchas(self, episode):
        url = episode['url']
        print(f'url: {url}')
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        html_tag = soup.select('div.cont-text span.icon-sound')
        text_value = html_tag[0].getText().strip()
        if text_value != '':
            episode['escuchas'] = int(text_value)
        else:
            episode['escuchas'] = None
        return episode