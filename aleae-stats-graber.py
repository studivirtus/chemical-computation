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
import matplotlib
matplotlib.use('Agg')

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
            whiteCount -= 1
        if isVariable == True and i != ' ' and i != ')' and not insideParenthasis:
            whiteCount = 0
            variable = str(variable) + str(i)
            #print(variable)
    return variables


def  convertToNum(num):
    power10 = len(num) - 1
    total = 0
    for i in num:
        total += i * (10 ** power10)
        power10 -= 1
    return total


def  getNums(lineOfText):
    nums = []
    number = []
    num = []
    lineOfText.seek(0)
    for i, line in enumerate(lineOfText):
        if i > 1:
            #print(line[0])
            if line[0] == "S":
                number = []
                for i in line:
                    if i.isdigit():
                        num.append(int(i))
                    #print(num)
                    if i == ',' or i == ']' and num:
                            number.append(convertToNum(num))
                            num = []
            if number:
                nums.append(number)
                number = []
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
    return(varNames,  varVals)


def collate(data):
    dataVals = data[1]
    reOrderedData = []
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


def setLineMarker(lMaker):
    lm = 'nil'
    if (lMaker == 0):
        lm = '.'
    elif (lMaker == 1):
        lm = ','
    elif (lMaker == 2):
        lm = 'o'
    elif (lMaker == 3):
        lm = 'v'
    elif (lMaker == 4):
        lm = '^'
    elif (lMaker == 5):
        lm = '<'
    elif (lMaker == 6):
        lm = '>'
    elif (lMaker == 7):
        lm = '1'
    elif (lMaker == 8):
        lm = '2'
    elif (lMaker == 9):
        lm = '3'
    elif (lMaker == 10):
        lm = '4'
    elif (lMaker == 11):
        lm = 's'
    elif (lMaker == 12):
        lm = 'p'
    elif (lMaker == 13):
        lm = '*'
    elif (lMaker == 14):
        lm = 'h'
    elif (lMaker == 15):
        lm = 'H'
    elif (lMaker == 16):
        lm = '+'
    elif (lMaker == 17):
        lm = 'x'
    elif (lMaker == 18):
        lm = 'D'
    elif (lMaker == 19):
        lm = 'd'
    elif (lMaker == 20):
        lm = '|'
    elif (lMaker == 21):
        lm = '_'
    return lm


def setLineType(lType):
    lt = "nil"
    if (lType == 0):
        lt = '-'
    elif (lType == 1):
        lt = '--'
    elif (lType == 2):
        lt = '-.'
    return lt


def setLineColor(lColor):
    lc = 'nil'
    if (lColor == 0):
        lc = 'b'
    elif (lColor == 1):
        lc = 'g'
    elif (lColor == 2):
        lc = 'r'
    elif (lColor == 3):
        lc = 'c'
    elif (lColor == 4):
        lc = 'm'
    elif (lColor == 5):
        lc = 'y'
    elif (lColor == 6):
        lc = 'k'
    return lc


def  incLineMarker(lm):
    lm += 1
    if lm > 21:
        lm = 0
    return lm


def  incLineType(lt):
    lt += 1
    if lt > 2:
        lt = 0
    return lt


def  incLineColor(lc):
    lc += 1
    if lc > 6:
        lc = 0
    return lc


if __name__ == '__main__':
    main()

#import fileinput
#for line in fileinput.input():
    #fileName = line
#fileName = fileName.replace("\n", "")

fileName = "14-03-14_02:05:12:523723551"


directory = "output/"
DirectoryFile = directory + fileName
print("1")


outPutFile = open(DirectoryFile + ".outpt", mode='r')
for line in outPutFile:
    #print(line)
    i = 2
data = getVariInitalNums(outPutFile)
print(data)
#pdb.set_trace()
reData = collate(data)
print(reData)
#pdb.set_trace()

i = 0  # counter to cycle through the data list
lineMarker = 0  # for cycling through matplotlib line markers
lineType = 0  # for cycling through matplotlib line types
lineColor = 0  # for cycling through matplotlib line colors

while i < len(reData):
    print(('data', len(data[0])))
    print(('reData', len(reData)))
    print(('i', i))
    print((len(reData)))
    print((len(data[0][i])))

    lMarker = setLineMarker(lineMarker)
    lType = setLineType(lineType)
    lColor = setLineColor(lineColor)

    #  multi line parenthasis: '(plt.plot...'
    (plt.plot(
        reData[i],
        marker=lMarker,
        linestyle=lType,
        color=lColor,
        label=data[0][i],
        linewidth=3
        ))

    i += 1
    lineMarker = incLineColor(lineMarker)
    lineType = incLineType(lineType)
    lineColor = incLineColor(lineColor)


plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig(DirectoryFile)
i = 0