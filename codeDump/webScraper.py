from bs4 import BeautifulSoup
import csv
import requests
import os

#gets and requests data from the url
url = "https://www.firstbus.co.uk/doncaster/plan-journey/timetables/?day=1&source_id=2&service=72%2F72x%2F73%2F73x&routeid=23935110&operator=34&source=sp"
urlRequest = requests.get(url)   
soup = BeautifulSoup(urlRequest.content, 'html5lib')

#configures file and path naming
fileName = input("Input File Name:")+'.txt'
pathName = ('/Users/mackenziemarriott/Documents/GitHub/busTimetableProject/codeDump/testFiles/txtTests')
completeFileName = os.path.join(pathName, fileName)

#main web scraping function - finds all needed data and writes to text file
def webScrape():
    #finds all elements with tag 'td' and writes them into the text file
    tdValue = 0
    tdContainer = soup.findAll('td')
    # goes through each td in the list and writes each value to a new line on the text file
    for td in tdContainer:
        with open(completeFileName, 'a') as openFile:
            openFile.write((tdContainer[tdValue].text+'\n'))
        tdValue+=1
    openFile.close()

#function to find the height of a first bus table - not including notes row
def tableHeight():
    totalHeight = 0
    tableHeightContainer = soup.findAll('tr', attrs={"class": "table_alt"})
    for tr in tableHeightContainer:
        totalHeight+=1
        print(totalHeight)
    tableHeightContainer = soup.findAll('tr', attrs={"class" : "table_alt"})
    for tr in tableHeightContainer:
        totalHeight+=1
        print(totalHeight)

#finds total amount of tables on a page
def totalTables():
    totalTableCount = 0
    tableCount = soup.findAll("tr", attrs={"class":"bodytextbold"})
    for tr in tableCount:
        totalTableCount+=1
        print(totalTableCount)

def lineCount():
    with open(completeFileName, 'r') as openFile:
    fileLength = len(openFile.readlines())