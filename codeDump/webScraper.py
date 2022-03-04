from bs4 import BeautifulSoup
import csv
import requests
import os

#main web scraping function
def webScrape():
    #gets and requests data from the url
    print("get urls from bustimes.org or the first bus website - other urls may not be compatible")
    url = input("Input exact URL to obtain timetable data:")
    urlRequest = requests.get(url)   
    soup = BeautifulSoup(urlRequest.content, 'html5lib')

    #configures file and path naming
    fileName = input("Input File Name:")+'.txt'
    pathName = ('/Users/mackenziemarriott/Documents/GitHub/busTimetableProject/codeDump/testFiles/txtTests')
    completeFileName = os.path.join(pathName, fileName)

    #finds all elements with tag 'td' and writes them into the text file
    tdValue = 0
    tdContainer = soup.findAll('td')
    # goes through each td in the list and writes each value to a new line on the text file
    for td in tdContainer:
        with open(completeFileName, 'a') as openFile:
            openFile.write((tdContainer[tdValue].text+'\n'))
        openFile.close()
        tdValue+=1