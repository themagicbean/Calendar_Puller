'''
Created on Mar 28, 2019

@author: darrenbean
'''
'''
Created on Mar 19, 2019

@author: darrenbean
'''
import PyPDF2, os, re

# merging all pdfs seems bad since diff courtrooms
# need to loop through pages and get all data


def pdfToText(filename):
    pdfFileObj = open(filename, 'rb')
    pdfToRead = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfToRead.getNumPages()
    # need to get through all pages
    
    i = 0
    calendarTextFile = open(filename+'TEXT.txt', 'w+')
    while i+1 <= pdfToRead.getNumPages():
        pageObj = pdfToRead.getPage(i) # zero based indexes for pages
        calendarTextFile.write(pageObj.extractText())
        i += 1 
    calendarTextFile.close    


# need to be exporting judge name, dept for comparison later
def getRelevantText(testText):
    #findJudgeName: 
    #should return -1 if none found
    judgeStart = testText.find('Hon.')
    judgeEnd = testText.find('Event', judgeStart, judgeStart+30)
    if judgeEnd == -1 or judgeStart == -1:
        print('Judge Error')
    else:
        print('Judge is ' + testText[judgeStart:judgeEnd])
    #works
    
    #find dept
    deptFind = re.compile(r'Dept. \d|Brawley Courtroom West|Brawley Courtroom East|Winterhaven Courtroom')
    deptNum = deptFind.search(testText) # matches only first found
    if deptNum: # works so long as deptNum is not nothing
        print('Department is '+deptNum.group())
    else:
        print('Department Error')
    #works
    
    
    # case find all (somewhat duplicative given caseIndex finder)
    allCaseFind = re.compile(r'JCF+\d+|SPV+\d+|ECM+\d+|BCM+\d+')
    #need to map to 1st index of each ECM and slice string there
    allCases = allCaseFind.findall(testText)
    print(allCases)
    
    # get indexes, slice string (this seems to make allCAseFind not needed? except as maybe a check?)
    caseIndex = [m.start() for m in re.finditer(r'People vs.', testText)]  
    for i in range (len(caseIndex)):
        caseIndex[i] -= 9 # gets back to beginning of case # 
    caseIndex.append(-1)
    print(caseIndex)
    
    def pullCaseText(string, index1, index2):
        return string[index1:index2]
    
    splitCaseText = []
    for i in range (len(caseIndex) - 1):
        splitCaseText.append(pullCaseText(testText, caseIndex[i], caseIndex[i+1]))
    # works, makes a list of case strings
    print(splitCaseText)
    
    #return(judge dept casenos casetext?)

print(os.getcwd())
os.chdir('Calendars')
print(os.getcwd())

for path, directories, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.pdf') == True:
            print(filename + ' is a pdf file in the folder')
            pdfToText(filename)
            getTextFile = open(filename + 'TEXT.txt')
            getText = getTextFile.read()
            print(getText)
            getRelevantText(getText)
            getTextFile.close()

# get filename
# iterate through files

# pdfToText('PublicCalendar-032819033837.pdf')

"""
testFile = open('PublicCalendar-032819033837.pdfTextFile.txt')
testText = testFile.read()
print(testText)
getRelevantText(testText)
"""


"""
for path, directories, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        print(filename)
        if filename.endswith('pdf') == True:
            pdfToText(filename)

"""