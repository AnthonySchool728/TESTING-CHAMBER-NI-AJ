<<<<<<< HEAD
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
=======
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
>>>>>>> e7217ce0d926c387758e0484a8164991810cf7e1
        assert(expectedLines[index] == printedLines[index])