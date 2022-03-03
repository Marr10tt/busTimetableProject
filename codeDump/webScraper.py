from bs4 import BeautifulSoup
import csv
import requests
import os

def webScrape():
    print("get urls from bustimes.org or the first bus website - other urls may not be compatible")
    url = input("Input exact URL to obtain timetable data:")
    urlRequest = requests.get(url)   
    soup = BeautifulSoup(urlRequest.content, 'html5lib')

    fileName = input("Input File Name:")+'.txt'
    pathName = ('/Users/mackenziemarriott/Documents/GitHub/busTimetableProject/codeDump/testFiles/txtTests')
    completeFileName = os.path.join(pathName, fileName)

    tdValue = 0
    tdContainer = soup.findAll('td')
    for td in tdContainer:
        with open(completeFileName, 'a') as openFile:
            openFile.write((tdContainer[tdValue].text+'\n'))
        openFile.close()
        tdValue+=1

webScrape()