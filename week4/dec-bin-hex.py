def isValidBinInput (sBinInput):
    for i in sBinInput:
        if i in "01_":
            continue
        else:
            return False
    return True
def isValidDecInput (sDecInput):
    for i in sDecInput:
        if i in "1234567890":
            continue
        else:
            return False
    return True
def isValidHexInput (sHexInput):
    for i in sHexInput:
        if i.upper() in "1234567890ABCDEF_":
            continue
        else:
            return False
    return True
def bin2dec (sBinInput):
    counter=len(sBinInput)-1
    decimal= 0
    for char in sBinInput:
        decimal+=int(char)*(2**counter)
        counter -= 1
    return decimal
def bin2hex (sBinInput):
    a="_"+sBinInput[::-1]
    ref = len(sBinInput)//4
    med = ""
    if int(len(sBinInput)%4) != 0:
        for i in range(ref):
            group = a[1+(4*i):5+(4*i)]
            new = "0123456789ABCDEF"[bin2dec(group[::-1])%16]
            med = med+new
        group = a[1+(4*ref):]
        med = med + "0123456789ABCDEF"[bin2dec(group[::-1])%16]
        med = med[::-1]
    else:
        for i in range(ref):
            group = a[1+(4*i):5+(4*i)]
            new = "0123456789ABCDEF"[bin2dec(group[::-1])%16]
            med = med+new
    return med
def processBin(sInputNum): #input input w/o prefix
    if isValidBinInput(sInputNum):
        decNumber = str(bin2dec(sInputNum))
        binNumber = f'0b{sInputNum}'
        hexNumber = f'0x{bin2hex(sInputNum)}'
        result = (decNumber, binNumber, hexNumber)
        return result
    else:
        result = (None, "Invalid Input", None)
        return result
def dec2bin(sDecInput):
    a=int(sDecInput)
    b=""
    for i in (range(32))[::-1]:
        if a%(2**i) != a:
            b = b+"1"
            a = a-(2**i)
        else:
            b = b+"0"
    return b[b.find("1"):]
def dec2hex (sDecInput):
    return bin2hex(dec2bin(sDecInput))
def processDec (sInputNum):
    if (isValidDecInput(sInputNum) and len(num)>0 )and int(sInputNum) <= (2**32-1):
        decNumber = str(sInputNum)
        binNumber = f'0b{dec2bin(sInputNum)}'
        hexNumber = f'0x{dec2hex(sInputNum)}'
        result = (decNumber, binNumber, hexNumber)
        return result
    else:
        result = ("Invalid Input", None, None)
        return result
def hex2bin(sHexInput):
    return(dec2bin(hex2dec(sHexInput)))
def hex2dec(sHexInput):
    dec,count = 0,0
    for i in sHexInput:
        count += 1
        dec+=int(("1234567890ABCDEF".find(i.upper()))*(16**(len(sHexInput)-(count))))
    return dec
def processHex (sInputNum):
    if isValidHexInput(sInputNum):
        decNumber = str(hex2dec(sInputNum))
        binNumber = f'0b{hex2bin(sInputNum)}'
        hexNumber = f'0x{sInputNum}'
        result = (decNumber, binNumber, hexNumber)
        return result 
    else:
        result = (None, None, "Invalid Input")
        return result 
def printResult (dbhTuple):
    return print(f'dec : {dbhTuple[0]} \nbin : {dbhTuple[1]} \nhex : {dbhTuple[2]} \n')
def startProcess (sInputNum):
    processed = sInputNum[2:]
    processed = processed.replace("_","")
    processed = processed.lstrip("0")
    print()
    print(f"num : {num}")
    if num.startswith('0b') and (len(processed) > 0 and len(processed) <= 32):
        result=processBin(processed)
    elif num.startswith('0x') and (len(processed) > 0 and len(processed) <= 8):
        result=processHex(processed)
    else: 
        result=processDec(num) 
    return result
stopper = "0"    
while stopper.lower() != "q":
    print(f"{"DECIMAL : D..D, where D is 0-9   ".center(50," ")} \n{"BINARY : 0bB..B, where 5 is 0-1".center(50," ")} \n{"HEXADECIMAL : 0xS..S, where 5 is 0-9, A-F".center(50," ")} \n")
    num = input("Enter a number using the notation above: ")
    printResult(startProcess(num))