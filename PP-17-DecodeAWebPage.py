"""
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup
def get_html_titles():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, features="html.parser")
    for link in soup.find_all('h2', attrs={'class':'story-heading'}):
        print(link.text.strip())

get_html_titles()
