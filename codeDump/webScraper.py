from bs4 import BeautifulSoup
import csv
import requests

def webScrape():
    url = "https://bustimes.org/services/22-worksop-doncaster-3"
    r = requests.get(url)   
    soup = BeautifulSoup(r.content, 'html5lib')

    fileName = input("Input File Name:")

    i = 0
    divContainer = soup.findAll('td')
    for td in divContainer:
        with open(fileName+'.txt', 'a') as f:
            f.write((divContainer[i].text+'\n'))
        i+=1

webScrape()