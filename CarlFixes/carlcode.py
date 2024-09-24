def isValidBinInput(sBinInput):
    if sBinInput[0:2] == "0b":
        validChars = ('0', '1', '_')
        for char in sBinInput[2:]:
            if char not in validChars:
                return False
        return True
    return False
def isValidHexInput(sHexInput):
    if sHexInput[0:2] == '0x':
        validChars1 = ('a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_')
        for char in sHexInput[2:]:
            if char not in validChars1:
                return False
        return True
    return False
def isValidDecInput(sDecInput):
    for i in sDecInput:
        if i not in '0123456789_':
            return False
    return True
def bin2dec(n):
    decimal = 0
    power = 1
    n= n[2:]
    n=int(n)
    while n>0:
        tira = n%10
        n = n//10
        decimal += tira*power
        power = power*2
    return decimal
def bin2hex(n):
    return dec2hex(bin2dec(n))
def dec2bin(n):
    a = int(n)
    b = ""
    for i in (range(32))[::-1]:
        if a%(2**i) != a:
            b = b+"1"
            a = a-(2**1)
        else:
            b = b+"0"
    return b[b.find("1"):]
def dec2hex(n):
    hexchars = '0123456789ABCDEF'
    hexstring = ''
    if n == 0:
        return '0'
    while n > 0:
        remainder = n % 16
        hexstring = hexchars[remainder] + hexstring
        n //= 16
    return hexstring
def hex2bin(n):
    result = dec2hex(bin2dec(n))
    return result
def hex2dec(n):
   result = bin2hex(dec2bin(n))
   return result
def processBin(sInputNum):
    if isValidBinInput(sInputNum):
        binNumber = bin2dec(sInputNum)
        decNumber = f'{(sInputNum)}'
        hexNumber = f'0x{bin2hex(sInputNum)}'
        result = (binNumber, decNumber, hexNumber)
        return result
    else:
        return ("None", "Invalid Input", "None")
def processDec (sInputNum):
    if isValidDecInput(sInputNum) and int(sInputNum) <= (2**32-1):
        decNumber = str(sInputNum)
        binNumber = f'0b{dec2bin(sInputNum)}'
        hexNumber = f'0x{dec2hex(sInputNum)}'
        result = (decNumber, binNumber, hexNumber)
        return result
    else:
        result = ("Invalid Input", "None", "None")
        return result
def processHex (sInputNum):
    if isValidHexInput(sInputNum):
        decNumber = str(hex2dec(sInputNum))
        binNumber = f'0b{hex2bin(sInputNum)}'
        hexNumber = f'0x{sInputNum}'
        result = (decNumber, binNumber, hexNumber)
        return result 
    else:
        result = ("None", "None", "Invalid Input")
        return result 
def printResult (dbhTuple):
    return print(f'dec : {dbhTuple[0]} \nbin : {dbhTuple[1]} \nhex : {dbhTuple[2]} \n')
stopper = "0"    
while stopper.lower() != "q":
    print("DECIMAL : D..D, where D is 0-9   ".center(50," "))
    print("BINARY : 0bB..B, where 5 is 0-1".center(50," "))
    print("HEXADECIMAL : 0xS..S, where 5 is 0-9, A-F".center(50," "))
    print()
    num = input("Enter a number using the notation above: ")
    withoutadditional = num[2:]
    withoutadditional = withoutadditional.replace("_","")
    print()
    print(f"num : {num}")
    if num[0:2] == "0b" and len(withoutadditional) <= 32:
        result=processBin(num)
    elif num[0:2] == "0x" and len(withoutadditional) <= 8:
        result=processHex(withoutadditional)
    else: 
        result=processDec(num)
    printResult(result)
    stopper = input("Enter any key to continue or Q/q to stop: ")        