import requests
from bs4 import BeautifulSoup

LIMIT = 50
def getUrl(keyword):
    return f'https://www.indeed.com/jobs?q={keyword}&limit={LIMIT}'

def getLastPage(url):
    response = requests.get(getUrl("python"))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('ul', {'class':"pagination-list"}) 
    pageLink = pagination.find_all('a')
    last_page = int(pageLink[-2].string)
    return last_page
    
def extractJobs(url, last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping Indeed.com {page+1}')
        response = requests.get(f'{url}&start={page*LIMIT}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        jobList = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
        for job in jobList:
            jobs.append(extractData(job))
        print(f'Total: {len(jobs)} jobs extracted')
    return jobs

def extractData(jobSoup):
    titleLink = jobSoup.find('h2', {'class':'title'}).find('a')
    title = titleLink['title']
    company = jobSoup.find('span',{'class':'company'})
    if (company is None):
        compName = "None"
    elif (company.string is None):
        compName = company.find('a').string
    else:
        compName = company.string
    compName = compName.strip()
    locationBox = jobSoup.find('div',{'class':'recJobLoc'})
    location = locationBox['data-rc-loc']
    job_id = jobSoup['data-jk']
    return {'title':title, 'company':compName, 'location':location, 'link':f'https://www.indeed.com/viewjob?jk={job_id}'}

def startScrap(keyword):
    url = getUrl(keyword)
    last_page = getLastPage(url)
    return extractJobs(url, last_page)