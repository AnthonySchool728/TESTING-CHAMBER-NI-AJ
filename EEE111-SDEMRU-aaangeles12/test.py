words = ["apple", 'apple', 'banana', 'orange', 'apple', 'banana']
a=[]
for word in words:
    if word in a:
        continue
    print(f'{word}: {words.count(word)}')
    a.append(words)

