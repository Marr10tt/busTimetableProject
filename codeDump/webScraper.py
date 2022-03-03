from bs4 import BeautifulSoup
import csv
import requests

def webScrape():
    print("get urls from bustimes.org or the first bus website - other urls may not be compatible")
    url = input("Input exact URL to obtain timetable data:")
    urlRequest = requests.get(url)   
    soup = BeautifulSoup(urlRequest.content, 'html5lib')

    fileName = input("Input File Name:")

    tdValue = 0
    tdContainer = soup.findAll('td')
    for td in tdContainer:
        with open(fileName+'.txt', 'a') as openFile:
            openFile.write((tdContainer[tdValue].text+'\n'))
        tdValue+=1

webScrape()