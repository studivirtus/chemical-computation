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
#import pygal
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
            d.append( dataVals[i][j])
            i += 1
        reOrderedData.append(d)
        d = []
        i = 0
        j += 1
    print(reOrderedData)
    return reOrderedData


if __name__ == '__main__':
    main()
'''
import fileinput
for line in fileinput.input():
	fileName = line
fileName = fileName.replace("\n","")
directory = "/home/adminuser/Dropbox/EE5393/Assignments/homework1-problem2/"
DirectoryFile = directory+fileName
print("1")
'''
DirectoryFile = "C:\\Users\Michael\\Dropbox\\EE5393\\Assignments\\homework1-problem2\\14-03-14_00_32_34_900405008"


outPutFile = open (DirectoryFile+".outpt", mode='r')
for line in outPutFile:
    #print(line)
    i = 2
data = getVariInitalNums(outPutFile)
#print(data)
reData = collate(data)
#line_chart = pygal.Line()
#line_chart.title = 'Number of Molicules'
#line_chart.x_labels = map(str, range(0, len(reData[0])))
i = 0
#    print(len(reData[i]))
#   print (len(data[0][31]))
while i < len(reData):
    print('data', len(data[0]))
    print('reData', len(reData))
    print ('i', i)
    print('data', data)
    print (len(data[0][i]))
    #line_chart.add(data[0][i], reData[i])
    i += 1
#line_chart.render_to_file(DirectoryFile+".svg")

i = 10
