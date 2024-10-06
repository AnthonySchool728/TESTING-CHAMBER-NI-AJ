def drawLine(symbol, length):
    lineStr = str(symbol)*int(length)
    return lineStr 

printedLines = [] # ignore this line

def drawShape(pixelSymbol, spaceSymbol):
    nextLine = drawLine(spaceSymbol, 5) + drawLine(pixelSymbol, 1) + drawLine(spaceSymbol, 5)
    print(nextLine)
    printedLines.append(nextLine) # ignore this line
    nextLine = drawLine(spaceSymbol, 4) + drawLine(pixelSymbol, 3) + drawLine(spaceSymbol, 4)
    print(nextLine)
    printedLines.append(nextLine) # ignore this line
    nextLine = drawLine(spaceSymbol, 3) + drawLine(pixelSymbol, 5) + drawLine(spaceSymbol, 3)
    print(nextLine)
    printedLines.append(nextLine) # ignore this line
    nextLine = drawLine(spaceSymbol, 2) + drawLine(pixelSymbol, 7) + drawLine(spaceSymbol, 2)
    print(nextLine)
    printedLines.append(nextLine) # ignore this line
    nextLine = drawLine(spaceSymbol, 1) + drawLine(pixelSymbol, 9) + drawLine(spaceSymbol, 1)
    print(nextLine)
    printedLines.append(nextLine) # ignore this line
    nextLine = drawLine(spaceSymbol, 0) + drawLine(pixelSymbol, 11) + drawLine(spaceSymbol, 0)
    print(nextLine)
    printedLines.append(nextLine) # ignore this line
    nextLine = (drawLine(spaceSymbol, 4) + drawLine(pixelSymbol, 3) + drawLine(spaceSymbol, 4) + '\n') * 5
    print(nextLine)
    printedLines.append(nextLine) # ignore this line

drawShape('e',"-")
#Final Output - Commit Hash "Week 1 and 2"