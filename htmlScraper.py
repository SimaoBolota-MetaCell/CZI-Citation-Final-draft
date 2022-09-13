from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup

def get_html(readme_link):
    html = requests.get(readme_link).text
    return BeautifulSoup(html, 'html5lib')
    

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
