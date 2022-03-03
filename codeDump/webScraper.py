from bs4 import BeautifulSoup
import csv
import requests

def webScrape():
    print("get urls from bustimes.org or the first bus website - other urls may not be compatible")
    url = input("Input exact URL to obtain timetable data:")
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