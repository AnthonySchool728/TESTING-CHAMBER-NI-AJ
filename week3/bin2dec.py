a = input("enter a binary number : ") #takes an input from user for binary number
b=a.replace("_","") #removes "_"

def isValidInput (smthn):
    if len(b)>5 or (b.count("1")+b.count("0")!=len(b)): #detects if greater than 5 bits OR has non binary digit
        return False
    else:
        return True

def bin2dec (bin):
    counter=len(b)-1 #serves as both counter and multiplier for conversion
    binary = 0 # will be the final result
    for char in b:
        binary+=int(char)*(2**counter) #converts each digit to it's decimal counterpart
        counter -= 1
    return binary
        
if isValidInput(a):
    print(b[::-1]) #String splicing, reverses the string
    print(f'{a} in decimal is {bin2dec(b)}') # final decimal output
else:
    print("Invalid Input")
#Final Output Ver 1