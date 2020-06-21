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
    last_page = int(pageLink[-2].string)
    return last_page
    
def extractJobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping {page+1}')
        response = requests.get(f'{URL}&start={page*LIMIT}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        jobList = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
        for job in jobList:
            jobs.append(extractData(job))
        print(f'Total: {len(jobs)} jobs extracted')

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

def startScrap():
    extractJobs(extractPages())