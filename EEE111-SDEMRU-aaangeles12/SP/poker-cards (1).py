def test_cards():
    testColor = {'H': 'Hearts', 'D' : 'Diamonds', 'C' : 'Clubs', 'S' : 'Spades'}
    testRanks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    displayAllCards(testColor, testRanks)
    testCards = genCardDict(testColor, testRanks)
    goldenCards = {'H1': ('Ace', 'Hearts'), 'H2': ('Two', 'Hearts'), 'H3': ('Three', 'Hearts'), 'H4': ('Four', 'Hearts'), 'H5': ('Five', 'Hearts'), 'H6': ('Six', 'Hearts'), 'H7': ('Seven', 'Hearts'), 'H8': ('Eight', 'Hearts'), 'H9': ('Nine', 'Hearts'), 'H10': ('Ten', 'Hearts'), 'H11': ('Jack', 'Hearts'), 'H12': ('Queen', 'Hearts'), 'H13': ('King', 'Hearts'), 'D1': ('Ace', 'Diamonds'), 'D2': ('Two', 'Diamonds'), 'D3': ('Three', 'Diamonds'), 'D4': ('Four', 'Diamonds'), 'D5': ('Five', 'Diamonds'), 'D6': ('Six', 'Diamonds'), 'D7': ('Seven', 'Diamonds'), 'D8': ('Eight', 'Diamonds'), 'D9': ('Nine', 'Diamonds'), 'D10': ('Ten', 'Diamonds'), 'D11': ('Jack', 'Diamonds'), 'D12': ('Queen', 'Diamonds'), 'D13': ('King', 'Diamonds'), 'C1': ('Ace', 'Clubs'), 'C2': ('Two', 'Clubs'), 'C3': ('Three', 'Clubs'), 'C4': ('Four', 'Clubs'), 'C5': ('Five', 'Clubs'), 'C6': ('Six', 'Clubs'), 'C7': ('Seven', 'Clubs'), 'C8': ('Eight', 'Clubs'), 'C9': ('Nine', 'Clubs'), 'C10': ('Ten', 'Clubs'), 'C11': ('Jack', 'Clubs'), 'C12': ('Queen', 'Clubs'), 'C13': ('King', 'Clubs'), 'S1': ('Ace', 'Spades'), 'S2': ('Two', 'Spades'), 'S3': ('Three', 'Spades'), 'S4': ('Four', 'Spades'), 'S5': ('Five', 'Spades'), 'S6': ('Six', 'Spades'), 'S7': ('Seven', 'Spades'), 'S8': ('Eight', 'Spades'), 'S9': ('Nine', 'Spades'), 'S10': ('Ten', 'Spades'), 'S11': ('Jack', 'Spades'), 'S12': ('Queen', 'Spades'), 'S13': ('King', 'Spades')}
    assert (goldenCards == testCards)

def displayAllCards(paramColorDict, paramRanksList):
    sample = ''' H1 : Ace of Hearts      D1 : Ace of Diamonds    C1 : Ace of Clubs       S1 : Ace of Spades
 H2 : Two of Hearts      D2 : Two of Diamonds    C2 : Two of Clubs       S2 : Two of Spades
 H3 : Three of Hearts    D3 : Three of Diamonds  C3 : Three of Clubs     S3 : Three of Spades
 H4 : Four of Hearts     D4 : Four of Diamonds   C4 : Four of Clubs      S4 : Four of Spades
 H5 : Five of Hearts     D5 : Five of Diamonds   C5 : Five of Clubs      S5 : Five of Spades
 H6 : Six of Hearts      D6 : Six of Diamonds    C6 : Six of Clubs       S6 : Six of Spades
 H7 : Seven of Hearts    D7 : Seven of Diamonds  C7 : Seven of Clubs     S7 : Seven of Spades
 H8 : Eight of Hearts    D8 : Eight of Diamonds  C8 : Eight of Clubs     S8 : Eight of Spades
 H9 : Nine of Hearts     D9 : Nine of Diamonds   C9 : Nine of Clubs      S9 : Nine of Spades
H10 : Ten of Hearts     D10 : Ten of Diamonds   C10 : Ten of Clubs      S10 : Ten of Spades
H11 : Jack of Hearts    D11 : Jack of Diamonds  C11 : Jack of Clubs     S11 : Jack of Spades
H12 : Queen of Hearts   D12 : Queen of Diamonds C12 : Queen of Clubs    S12 : Queen of Spades
H13 : King of Hearts    D13 : King of Diamonds  C13 : King of Clubs     S13 : King of Spades
    '''
    print(sample)

def genCardDict(paramColorDict, paramRanksList):
    cardsDict = {}
    return cardsDict

def main():
    test_cards()

if __name__ == "__main__":
    main()
