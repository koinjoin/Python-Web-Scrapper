import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def extractPages():
    response = requests.get(URL, auth=('user', 'pass'))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('ul', {"class":"pagination-list"}) 
    pageLink = pagination.find_all('a')
    pages = []
    for link in pageLink[:-1]:
        pages.append(int(link.string))
    last_page = pages[-1]
    return last_page
    
def extractJobs(last_page):
    for page in range(last_page):
        print(f'start={page*LIMIT}')

