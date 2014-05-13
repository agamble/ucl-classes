from bs4 import BeautifulSoup
import requests
import re

session = requests.Session()
r = session.get('http://www.ucl.ac.uk/prosp-students/study-abroad/phpinc/subject-index/index.php?-C=')
content = BeautifulSoup(r.content)

links = content.find_all('a')

degrees = {}

for link in links:
    print link['href']
    session.headers.update({'referer': link['href']})
    page = session.get('http://www.ucl.ac.uk/prosp-students/study-abroad/phpinc/subject/modules.php?-C=')
    degree_page = BeautifulSoup(page.content)

    courses = degree_page.find_all('table', class_="sag-modheader")
    
    modules = []
    for module in courses:
       this_module = {
               'code': module.find('td', class_="sag-modcode").string,
               'name': module.find('td', class_="sag-modtitle").string
       }
       modules.append(this_module)
    
    degrees[link.string] = modules

print degrees 

