from week2 import printedLines

def test_arrowUp():
    expectedLines = []
    expectedLines.append('-----e-----')
    expectedLines.append('----eee----')
    expectedLines.append('---eeeee---')
    expectedLines.append('--eeeeeee--')
    expectedLines.append('-eeeeeeeee-')
    expectedLines.append('eeeeeeeeeee')
    expectedLines.append('----eee----\n'*5)

    for index in range(len(expectedLines)):
        print(expectedLines[index])
        print(printedLines[index])
        assert(expectedLines[index] == printedLines[index])