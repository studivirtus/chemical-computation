#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Michael
#
# Created:     09/03/2014
# Copyright:   (c) Michael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
import pdb
import matplotlib.pyplot as plt


def main():
    pass


def getVariables(lineOfText):
    variables = []
    variable = str()
    whiteCount = 0
    #print(lineOfText)
    isVariable = True
    insideParenthasis = False
    for i in lineOfText:
        #print (i)
        if i == ' ' and not insideParenthasis:
            if whiteCount == 0:
                variables.append(variable)
                variable = str('')
            isVariable = False
            whiteCount += 1
            if whiteCount == 2:
                isVariable = True
        elif i == '(':
            insideParenthasis = True
        elif i == ')':
            insideParenthasis = False
            whiteCount -=1
        if isVariable == True and i != ' ' and i != ')' and not insideParenthasis:
            whiteCount = 0
            variable = str(variable) + str(i)
            #print(variable)
    return variables

def convertToNum(num):
    power10 = len(num) - 1
    total = 0
    for i in num:
        total += i * (10**power10)
        power10 -= 1
    return total

def getNums(lineOfText):
    nums = []
    number = []
    num = []
    lineOfText.seek(0)
    for i, line in enumerate(lineOfText):
        if i > 1:
            #print(line[0])
            if line[0] =="S":
                number=[]
                for i in line:
                    if i.isdigit():
                        num.append(int(i))
                    #print(num)
                    if i ==',' or i == ']' and num:
                            number.append(convertToNum(num))
                            num = []
            if number:
                nums.append(number)
                number=[]
        #print(nums)
    return nums


def getVariInitalNums(readFile):
    readFile.seek(0)
    varNames = []
    varVals = []
    for i, line in enumerate(readFile):
        if i == 1:
            varNames = getVariables(line)
            #print(varNames)
    print("THIS IS A TEST STATMENT")
    varVals = getNums(readFile)
    #print(varVals)
    return( varNames,  varVals)

def collate(data):
    dataVals = data[1]
    reOrderedData=[]
    d = []
    print(dataVals)

    print(len(dataVals[0]))
    print(len(dataVals))

    i = 0
    j = 0
    print(len(dataVals))
    while j < len(dataVals[i]):
        while i < len(dataVals):
            d.append(dataVals[i][j])
            i += 1
        reOrderedData.append(d)
        d = []
        i = 0
        j += 1
    print(reOrderedData)
    return reOrderedData


def lineTypeColor(lineColor, lineType):
    lColor = 'nil'
    lType = 'nil'
    if (lineColor == 0):
        lColor = 'b'
    elif (lineColor == 1):
        lColor = 'g'
    elif (lineColor == 2):
        lColor = 'r'
    elif (lineColor == 3):
        lColor = 'c'
    elif (lineColor == 4):
        lColor = 'm'
    elif (lineColor == 5):
        lColor = 'y'
    elif (lineColor == 6):
        lColor = 'k'
    elif (lineColor == 7):
        lColor = 'w'

    if (lineType == 0):
        lType = '-'
    elif (lineType == 1):
        lType = '--'
    elif (lineType == 2):
        lType = '-.'
    elif (lineType == 3):
        lType = ':'
    elif (lineType == 4):
        lType = '.'
    elif (lineType == 5):
        lType = ','
    elif (lineType == 6):
        lType = 'o'
    elif (lineType == 7):
        lType = 'v'
    elif (lineType == 8):
        lType = '^'
    elif (lineType == 9):
        lType = '<'
    elif (lineType == 10):
        lType = '>'
    elif (lineType == 11):
        lType = '1'
    elif (lineType == 12):
        lType = '2'
    elif (lineType == 13):
        lType = '3'
    elif (lineType == 14):
        lType = '4'
    elif (lineType == 15):
        lType = 's'
    elif (lineType == 16):
        lType = 'p'
    elif (lineType == 17):
        lType = '*'
    elif (lineType == 18):
        lType = 'h'
    elif (lineType == 19):
        lType = 'H'
    elif (lineType == 20):
        lType = '+'
    elif (lineType == 21):
        lType = 'x'
    elif (lineType == 22):
        lType = 'D'
    elif (lineType == 23):
        lType = 'd'
    elif (lineType == 24):
        lType = '|'
    elif (lineType == 25):
        lType = '_'
    return lColor + lType


if __name__ == '__main__':
    main()

#import fileinput
#for line in fileinput.input():
    #fileName = line
#fileName = fileName.replace("\n", "")

fileName = "14-03-14_00:24:54:468648548"


directory = "/home/adminuser/Dropbox/EE5393/Assignments/homework1-problem2/"
DirectoryFile = directory + fileName
print("1")


outPutFile = open(DirectoryFile + ".outpt", mode='r')
for line in outPutFile:
    #print(line)
    i = 2
data = getVariInitalNums(outPutFile)
print(data)
pdb.set_trace()
reData = collate(data)
print(reData)
print(lineTypeColor(7,25))
pdb.set_trace()

#line_chart = pygal.Line()
#line_chart.title = 'Number of Molicules'
#line_chart.x_labels = map(str, range(0, len(reData[0])))
i = 0
lineType = 0 # for cycling through matplotlib line types
lineColor = 0 #for cycling through matplotlib line colors
#    print(len(reData[i]))
#    print (len(data[0][31]))
while i < len(reData):
    print('data', len(data[0]))
    print('reData', len(reData))
    print ('i', i)
    print (len(reData))
    print (len(data[0][i]))
    #line_chart.add(data[0][i], reData[i])

    plt.plot(reData[i], marker='o', linestyle='--', color='r', label=data[0][i])
    i += 1
#line_chart.render_to_file(DirectoryFile + ".svg")
plt.show()
i = 0
