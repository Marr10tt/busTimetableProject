from bs4 import BeautifulSoup
import csv
import requests

url = "https://bustimes.org/services/22-worksop-doncaster-3"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

def firstBusWebScrape():
    i = 0
    divContainer = soup.findAll('td')
    for td in divContainer:
        with open('test.txt', 'a') as f:
            f.write((divContainer[i].text+'\n'))
        i+=1

firstBusWebScrape()

#table = soup.find('table')