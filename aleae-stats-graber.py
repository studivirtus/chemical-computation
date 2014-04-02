#-------------------------------------------------------------------------------
# Name:        PYTHON STATS GRABBER
# Purpose:     for use with Dr. Marc Ridels ALEAE program for chemical
#              simulation
#
# Author:      Michael Mullen
#
# Created:     03/03/2014
# Copyright:   Open Source - HAVE FUN!
# Licence:     Open source! please give credit if used
#-------------------------------------------------------------------------------
import matplotlib
import pdb
#matplotlib.use('Agg')

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
    #print("THIS IS A TEST STATMENT")
    varVals = getNums(readFile)
    #print(varVals)
    return(varNames, varVals)


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


def setLineMarker(lMarker):
    lm = 'nil'
    if (lMarker == 0):
        lm = '.'
    elif (lMarker == 1):
        lm = ','
    elif (lMarker == 2):
        lm = 'o'
    elif (lMarker == 3):
        lm = 'v'
    elif (lMarker == 4):
        lm = '^'
    elif (lMarker == 5):
        lm = '<'
    elif (lMarker == 6):
        lm = '>'
    elif (lMarker == 7):
        lm = '1'
    elif (lMarker == 8):
        lm = '2'
    elif (lMarker == 9):
        lm = '3'
    elif (lMarker == 10):
        lm = '4'
    elif (lMarker == 11):
        lm = 's'
    elif (lMarker == 12):
        lm = 'p'
    elif (lMarker == 13):
        lm = '*'
    elif (lMarker == 14):
        lm = 'h'
    elif (lMarker == 15):
        lm = 'H'
    elif (lMarker == 16):
        lm = '+'
    elif (lMarker == 17):
        lm = 'x'
    elif (lMarker == 18):
        lm = 'D'
    elif (lMarker == 19):
        lm = 'd'
    elif (lMarker == 20):
        lm = '|'
    elif (lMarker == 21):
        lm = '_'
    #print(lMarker)
    #print(lm)
    #pdb.set_trace()
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
#  Comment the following lines to test ALEAE-STATS-GRABBER by itself
import fileinput
for line in fileinput.input():
    fileName = line
fileName = fileName.replace("\n", "")
# END COMMENTED SECTION FOR TESTING

#fileName = "demo" # USED FOR TESTING ALEAE-STATS-GRABBER BY ITSELF


directory = "output/"
DirectoryFile = directory + fileName


outPutFile = open(DirectoryFile + ".outpt", mode='r')
for line in outPutFile:
    #print(line)
    i = 2
data = getVariInitalNums(outPutFile)
#print(data)
#pdb.set_trace()
reData = collate(data)
#print(reData)
#pdb.set_trace()

i = 0  # counter to cycle through the data list
lineMarker = 0  # for cycling through matplotlib line markers
lineType = 0  # for cycling through matplotlib line types
lineColor = 0  # for cycling through matplotlib line colors

while i < len(reData):
    #print(('data', len(data[0])))
    #print(('reData', len(reData)))
    #print(('i', i))
    #print((len(reData)))
    #print((len(data[0][i])))

    lMarker = setLineMarker(lineMarker)
    lType = setLineType(lineType)
    lColor = setLineColor(lineColor)

    #  multi line parenthasis: '(plt.plot...)'
    (plt.plot(
        reData[i],
        marker=lMarker,
        linestyle=lType,
        color=lColor,
        label=data[0][i],
        linewidth=2
        ))

    i += 1
    lineMarker = incLineMarker(lineMarker)
    lineType = incLineType(lineType)
    lineColor = incLineColor(lineColor)

i = 0
print((data[0]))
print(data[len(data)-1][len(data[len(data)-1])-1])
while i < (len(data[0])-1):
    print(data[0][i])
    print(data[len(data)-1][len(data[len(data)-1])-1][i])
    i += 1


plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig(DirectoryFile)
i = 0