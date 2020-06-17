import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

def extractPages():
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('ul', {'class':"pagination-list"}) 
    pageLink = pagination.find_all('a')
    pages = []
    for link in pageLink[:-1]:
        pages.append(int(link.string))
    last_page = pages[-1]
    return last_page
    
def extractJobs(last_page):
    for page in range(last_page):
        print(extractJob(f'{URL}&start={page*LIMIT}'))

def extractJob(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    jobList = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
    titleList = []
    compList = []
    for job in jobList:
        print(extractData(job))

def extractData(jobSoup):
    titleLink = jobSoup.find('h2', {'class':'title'}).find('a')
    title = titleLink['title']
    company = jobSoup.find('span',{'class':'company'})
    if company.string is None:
        compName = company.find('a').string
    else:
        compName = company.string
    compName = compName.strip()
    locationBox = jobSoup.find('div',{'class':'recJobLoc'})
    location = locationBox['data-rc-loc']
    job_id = jobSoup['data-jk']
    return {'title':title, 'company':compName, 'location':location, 'link':f'https://www.indeed.com/viewjob?jk={job_id}'}