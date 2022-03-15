from turtle import width
from bs4 import BeautifulSoup
import requests
import os

tableDict=[]
totalTableCount=0
widthPerTable=[]
totalHeight = 0
heightPerTable = 0

dimensionArray=[]

fileLength = 0

#gets and requests data from the url
url = "https://www.firstbus.co.uk/doncaster/plan-journey/timetables/?day=1&source_id=2&service=72%2F72x%2F73%2F73x&routeid=23935110&operator=34&source=sp"
urlRequest = requests.get(url)
soup = BeautifulSoup(urlRequest.content, 'html5lib') 

#configures file and path naming
fileName = "countTest.txt"
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
	global totalHeight
	tableHeightContainer = soup.findAll('tr', attrs={"class": "table_alt"})
	for tr in tableHeightContainer:
		totalHeight+=1
	tableHeightContainer = soup.findAll('tr', attrs={"class" : "table_alt"})
	for tr in tableHeightContainer:
		totalHeight+=1

#counts the total number of columns in each table
def tableWidth():
	global widthPerTable
	total=0
	firstRow = soup.find("tr", attrs={"class":"table_main"})
	for td in firstRow:
		total+=1
	widthPerTable.append(total-3)

#finds total amount of tables on a page
def totalTables():
	global totalTableCount
	totalTableCount = 0
	tableCount = soup.findAll("tr", attrs={"class":"bodytextbold"})
	for tr in tableCount:
		totalTableCount+=1

#creates dictionary of dimensions for all tables on a page
def tableInput():
	global tableDict
	global totalTableCount
	global heightPerTable

	tableDict = []
	tableHeight=0

	lineTracker = 0
	file = open(completeFileName)
	fileContent = file.readlines()
	firstColumns = soup.findAll("td", attrs={"class":"first-column"})

	#makes array 3D for amount of tables
	for i in range(0,totalTableCount):
		tableDict.append([])
	for td in firstColumns:
		tableHeight+=1
	
	#calculates the height of each table
	heightperTable=int(tableHeight/totalTableCount)
	#makes the smaller arrays, one for each table line
	for i in range(0, totalTableCount):
		for x in range(0,heightperTable):
			tableDict[i].append([])
			for b in range(0,11):
				tableDict[i][x].append(fileContent[lineTracker])
				while lineTracker != fileLength-1:
					lineTracker+=1
					break

#counts total lines of data in a given text file
def lineCount():
	global fileLength
	with open(completeFileName, 'r') as openFile:
		fileLength = len(openFile.readlines())
		print(fileLength)

#makes empty arrays to function as dimensions for each table
def tableDimensions():
	global dimensionArray
	global heightPerTable
	for i in range(0, totalTableCount):
		dimensionArray.append([])
		dimensionArray[i].append(widthPerTable)
		dimensionArray[i].append(heightPerTable)
	print(dimensionArray)

lineCount()
totalTables()
tableInput()
tableHeight()
tableWidth()
tableDimensions()