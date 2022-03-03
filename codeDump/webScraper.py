from bs4 import BeautifulSoup
import csv
import requests

url = "https://www.firstbus.co.uk/doncaster/plan-journey/timetables/?day=1&source_id=2&service=72%2F72x%2F73%2F73x&routeid=23935110&operator=34&source=sp"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

allData=[]
i = 0
divContainer = soup.findAll('td')
for td in divContainer:
    allData.append(divContainer[i].text)
    i+=1

#table = soup.find('table')