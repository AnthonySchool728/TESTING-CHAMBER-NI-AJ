<<<<<<< HEAD
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

def main():
    test_cards()
# AAAAAA
if __name__ == "__main__":
    main()
=======
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

def main():
    test_cards()
# AAAAAA
if __name__ == "__main__":
    main()
>>>>>>> e7217ce0d926c387758e0484a8164991810cf7e1