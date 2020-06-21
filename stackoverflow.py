import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs?q=python'

def getLastPage():
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', {'class':"s-pagination"}) 
    pageLink = pagination.find_all('a', {'class':'s-pagination--item'})
    print(pageLink)