import requests
from bs4 import BeautifulSoup

indeed = requests.get('https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&as_src&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=aeed01dbd68defa8', auth=('user', 'pass'))
# print(indeed.status_code)
# print(indeed.headers['content-type'])
# print(type(indeed))
# print(indeed)
# print(indeed.text) 
# all the html...

indeed_html = indeed.text
indeed_soup = BeautifulSoup(indeed_html, 'html.parser')
indeed_pagination = indeed_soup.find('ul', {"class":"pagination-list"}) 
indeed_pages = indeed_pagination.find_all('a')
indeed_pageNumber = indeed_pagination.find_all('span', {"class":"pn"})[:-1] #마지막은 제외
print(indeed_pageNumber)

