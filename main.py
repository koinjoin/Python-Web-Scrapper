import requests

result_indeed = requests.get('https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&as_src&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=aeed01dbd68defa8', auth=('user', 'pass'))
print(result_indeed.status_code)
print(result_indeed.headers['content-type'])
print(type(result_indeed))
print(result_indeed)
print(result_indeed.text)