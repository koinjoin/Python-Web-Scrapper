import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs?q=python'

def getLastPage():
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', {'class':"s-pagination"}) 
    pageLink = pagination.find_all('a', {'class':'s-pagination--item'})
    last_page = int(pageLink[-2].find('span').string)
    return last_page

def extractJobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping {page+1}')
        response = requests.get(f'{URL}&pg={page+1}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        jobList = soup.find_all('div', {'class':'-job'})
        for job in jobList:
            jobs.append(extractData(job))
        # for job in jobList:
        #     jobs.append(extractData(job))
        print(f'Total: {len(jobs)} jobs extracted')

def extractData(jobSoup):
    titleLink = jobSoup.find('a',{'class':'s-link'})
    title = titleLink['title']
    company = jobSoup.find('h3', {'class':'mb4'})
    compName = company.find('span').get_text(strip=True)
    location = company.find('span',{'class':'fc-black-500'}).get_text(strip=True)
    job_id = jobSoup['data-result-id']
    return {'title':title, 'company':compName, 'location':location, 'link':f'https://stackoverflow.com/jobs/{job_id}'}

def startScrap():
    last_page = getLastPage()
    extractJobs(last_page)

