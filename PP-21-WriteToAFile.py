"""
Take the code from the How To Decode A Website exercise (if you didn’t do it or
just want to play with some different code, use the code from the solution),
and instead of printing the results to a screen, write the results to a txt
file. In your code, just make up a name for the file you are saving to.
Extras:
    Ask the user to specify the name of the output file that will be saved.
"""


import requests
from bs4 import BeautifulSoup

def get_html_titles():
    result = ''
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, features="html.parser")
    for link in soup.find_all(class_="story-heading"):
        if link.a:
            result += '/' + str(link.a.text.strip())
        else:
            result += '/' + str(link.contents[0].strip())
    return result.replace('/', '\n')

file_name = input("Name of the file: \n")

with open(file_name + '.txt', 'w') as open_file:
    open_file.write(str(get_html_titles()))

# Different solution: Move loop to with statement.
