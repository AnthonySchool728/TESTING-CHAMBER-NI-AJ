def genAllCards (s,v):
    a =[]
    for i in s:
        for j in v:
            a.append(f'{j}-{i}')
    return a
suits = ['C','D','H','S']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cards = genAllCards(suits,values)

print(cards,len(cards))

firstHalf = cards[:26]
secondHalf = cards[26:]

def shuffle (Fh,Sh):
    a = []
    for o in range(0,25):
        a.append(Fh[o])
        a.append(Sh[o])
    return a

shuffled = shuffle(firstHalf,secondHalf)
print(shuffled)

def isEq (c,sc):
    return all(a in c for a in sc)

print(isEq(cards,shuffled))