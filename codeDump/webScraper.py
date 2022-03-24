from bs4 import BeautifulSoup
import requests
import os

#table dimensions
tableDict=[]
totalTableCount=0
widthPerTable=[]
totalHeight = 0
heightPerTable = 0

#array to store dimensions
dimensionArray=[]

#length of a given text file with stop time data 
fileLength = 0

#declarations so values can be used later as globals in other functions
completeFileName = ""
soup = None

#main web scraping function - finds all needed data and writes to text file
def webScrape(routeURL, routeName):
	global completeFileName
	global soup

	#gets and requests data from the url
	url = routeURL
	urlRequest = requests.get(url)
	soup = BeautifulSoup(urlRequest.content, 'html5lib') 

	#configures file and path naming
	fileName = routeName+".txt"
	pathName = ('/Users/mackenziemarriott/Documents/GitHub/busTimetableProject/codeDump/testFiles/txtTests')
	completeFileName = os.path.join(pathName, fileName)
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
	global heightPerTable
	tableHeightContainer = soup.findAll('tr', attrs={"class": "table_alt"})
	for tr in tableHeightContainer:
		totalHeight+=1
	tableHeightContainer = soup.findAll('tr', attrs={"class" : "table_alt"})
	for tr in tableHeightContainer:
		totalHeight+=1

	#calculates the average height of each table
	firstColumns = soup.findAll("td", attrs={"class":"first-column"})
	for td in firstColumns:
		heightPerTable+=1
	heightPerTable=int(heightPerTable/totalTableCount)

#counts the total number of columns in each table
def tableWidth():
	global widthPerTable
	total=0
	firstRow = soup.find("span", attrs={"class":"magenta_on"})
	for i in range (1, (len(firstRow)+1)):
		total+=1
	total+=(totalTableCount)
	widthPerTable.append(total)

#finds total amount of tables on a page
def totalTables():
	global totalTableCount
	totalTableCount = 0
	tableCount = soup.findAll("tr", attrs={"class":"bodytextbold"})
	for tr in tableCount:
		totalTableCount+=1

#creates dictionary of dimensions for all tables on a page
def fileInput():
	global tableDict
	global totalTableCount
	global heightPerTable
	tableDict = []
	lineTracker = 0
	file = open(completeFileName)
	fileContent = file.readlines()
	#makes array 3D for amount of tables
	for i in range(0,totalTableCount):
		tableDict.append([])

	#makes the smaller arrays, one for each table line
	for i in range(0, totalTableCount):
		for x in range(0,heightPerTable):
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

#makes empty arrays to function as dimensions for each table
def tableDimensions():
	global dimensionArray
	global heightPerTable
	for i in range(0, totalTableCount):
		dimensionArray.append([])
		dimensionArray[i].append(widthPerTable)
		dimensionArray[i].append(heightPerTable)
	print(dimensionArray)

'''
#finds out overall data 
lineCount()
totalTables()

#calculates dimensions of timetables
tableHeight()
tableWidth()
tableDimensions()

#inputs timetable data to file and 3D array
fileInput()
'''

#^^functions were called to test - no longer needed to be called, messes with the program when importing module