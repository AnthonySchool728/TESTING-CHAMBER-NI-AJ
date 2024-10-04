def test_cards():
    testColor = {'H': 'Hearts', 'D' : 'Diamonds', 'C' : 'Clubs', 'S' : 'Spades'}
    testRanks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    displayAllCards(testColor, testRanks)
    testCards = genCardDict(testColor, testRanks)
    goldenCards = {'H1': ('Ace', 'Hearts'), 'H2': ('Two', 'Hearts'), 'H3': ('Three', 'Hearts'), 'H4': ('Four', 'Hearts'), 'H5': ('Five', 'Hearts'), 'H6': ('Six', 'Hearts'), 'H7': ('Seven', 'Hearts'), 'H8': ('Eight', 'Hearts'), 'H9': ('Nine', 'Hearts'), 'H10': ('Ten', 'Hearts'), 'H11': ('Jack', 'Hearts'), 'H12': ('Queen', 'Hearts'), 'H13': ('King', 'Hearts'), 'D1': ('Ace', 'Diamonds'), 'D2': ('Two', 'Diamonds'), 'D3': ('Three', 'Diamonds'), 'D4': ('Four', 'Diamonds'), 'D5': ('Five', 'Diamonds'), 'D6': ('Six', 'Diamonds'), 'D7': ('Seven', 'Diamonds'), 'D8': ('Eight', 'Diamonds'), 'D9': ('Nine', 'Diamonds'), 'D10': ('Ten', 'Diamonds'), 'D11': ('Jack', 'Diamonds'), 'D12': ('Queen', 'Diamonds'), 'D13': ('King', 'Diamonds'), 'C1': ('Ace', 'Clubs'), 'C2': ('Two', 'Clubs'), 'C3': ('Three', 'Clubs'), 'C4': ('Four', 'Clubs'), 'C5': ('Five', 'Clubs'), 'C6': ('Six', 'Clubs'), 'C7': ('Seven', 'Clubs'), 'C8': ('Eight', 'Clubs'), 'C9': ('Nine', 'Clubs'), 'C10': ('Ten', 'Clubs'), 'C11': ('Jack', 'Clubs'), 'C12': ('Queen', 'Clubs'), 'C13': ('King', 'Clubs'), 'S1': ('Ace', 'Spades'), 'S2': ('Two', 'Spades'), 'S3': ('Three', 'Spades'), 'S4': ('Four', 'Spades'), 'S5': ('Five', 'Spades'), 'S6': ('Six', 'Spades'), 'S7': ('Seven', 'Spades'), 'S8': ('Eight', 'Spades'), 'S9': ('Nine', 'Spades'), 'S10': ('Ten', 'Spades'), 'S11': ('Jack', 'Spades'), 'S12': ('Queen', 'Spades'), 'S13': ('King', 'Spades')}
    assert (goldenCards == testCards)

def displayAllCards(paramColorDict, paramRanksList):
    for index,value in enumerate(paramRanksList):
        for color in list(paramColorDict.keys()):
            temp_= color+str(index+1) if len(color+str(index+1)) == 3 else f' {color+str(index+1)}'
            print(f"{temp_} : {value} of {paramColorDict[color]}",end="\t")
        print()

def genCardDict(paramColorDict, paramRanksList):
    cardsDict = {}
    for color in list(paramColorDict.keys()):
        for index,value in enumerate(paramRanksList):
            cardsDict.update({color+str(index+1):(value,paramColorDict[color])})    
    return cardsDict

def parseInputCards(inString):
    # Hint : you can use strip() and split() functions
    cardList = inString.strip().split()
    print(cardList)
    return cardList

def isValidInput(parsedInput):
    return len(parsedInput)==len(set(parsedInput))==5 and all([card in cards.keys() for card in (parsedInput)])

def displayCards(cardList):
    print(f'\nYour cards are the following : {cardList}')
    for card in cardList:
        temp_= card if len(card) == 3 else f' {card}'
        print(f'{temp_} : {cards[card][0]} of {cards[card][1]}',)
    print("")

def printDivider(divLength):
    print(f'{"*"*divLength}')
def printTitle(title, margin):
    print(f'{"*"*margin} {title} {"*"*margin}')
def printMenu():
    printDivider(95)
    printTitle('P O K E R   H A N D S', 36)
    printDivider(95)
    displayAllCards(colors, ranks)
    print("")
    printDivider(95)




def removextra(cardList, sett = 1):
    if sett == 1:
        num = [int(a[1:]) for a in cardList]
        num.sort()
        return num
    return [a[0] for a in cardList]
def isFlush (cardList):
    return (len(set(removextra(cardList,0))) == 1)

def isStraight (cardList):
    num,royalStraight = removextra(cardList), [1,10,11,12,13]
    if num == royalStraight or num == [a for a in range(min(num),min(num)+5)]:
        return True
    return False

def isRoyalFlush (cardList):
    num,broadway = (removextra(cardList)), [1,10,11,12,13]
    if isFlush(cardList) and num == broadway:
        return True
    return False

def isStraightFlush (cardList):
    if isFlush(cardList) and isStraight(cardList) and not(isRoyalFlush):
        return True
    return False

def isFourOfaKind (cardList):
    a = removextra(cardList)
    if len(set(a[:4])) == 1 or len(set(a[1:])) == 1:
        return True
    return False

def isThreeOfaKind (cardList):
    if all(removextra(cardList).count(b) != 2 for b in removextra(cardList)):
        if any(removextra(cardList).count(a) == 3 for a in removextra(cardList)):
            return True
    return False

def isFullHouse(cardList):
    if any(removextra(cardList).count(b) == 2 for b in removextra(cardList)):
        if any(removextra(cardList).count(a) == 3 for a in removextra(cardList)):
            return True
    return False

def isTwoPair(cardList):
    Count = [removextra(cardList).count(b) for b in removextra(cardList)]
    if Count.count(2) == 4:
        return True
    return False

def isPair (fiveCards):
    Count = [removextra(fiveCards).count(b) for b in removextra(fiveCards)]
    if Count.count(2) == 2:
        return True
    return False

def isHighCard (fiveCards):
    Count = [removextra(fiveCards).count(b) for b in removextra(fiveCards)]
    if not(isFlush(fiveCards)) and Count.count(1) == 5:
        return True
    return False

def checkall (a):
    # print(f'Royal Flush: {isRoyalFlush(a)}')
    # print(f'Flush: {isFlush(a)}') 
    # print(f'Straight: {isStraight(a)}')
    # print(f'StraightFlush: {isStraightFlush(a)}')
    # print(f'Four of A Kind: {isFourOfaKind(a)}')
    # print(f'Three of a A Kind: {isThreeOfaKind(a)}')
    # print(f'Two Pair: {isTwoPair(a)}')
    # print(f'Pair: {isPair(a)}')
    # print(f'HighCard: {isHighCard(a)}')
    if isRoyalFlush(a):
        return (f'You have a Royal Flush')
    elif isStraightFlush(a):
        return (f'You have a Straight Flush')

    
# Global
colors = {'H': 'Hearts', 'D' : 'Diamonds', 'C' : 'Clubs', 'S' : 'Spades'}
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
cards = genCardDict(colors, ranks)

def main():
    while True:
        printMenu()
        userInput = input('\nSelect 5 cards separated by space. e.g. H11 S13 C2 D3 H7 : ')
        inputCards = parseInputCards(userInput)

        if isValidInput(inputCards):
            displayCards(inputCards)
            checkall(inputCards)
        else:
            print(f'\nInvalid input !!! : {inputCards}')
            print('\nPlease select a valid card. e.g. H1 S13 C2 D3 D7')

        tryAgain = input('\nPress any key to continue or Q/q to quit : ')
        if (tryAgain.upper() == 'Q'):
            break

if __name__ == "__main__":
    main()