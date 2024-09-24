def isValidBinInput(sBinInput):
    valid = True
    if sBinInput == '':
        valid = False
        return valid
    validcharacters = ("0", "1")
    if sBinInput[0:2] != "0b":
        valid = False
        return valid
    for char in sBinInput [2:]:
        if char.lower() not in validcharacters or len(sBinInput[2:])>32:
            valid = False
            break
    return valid
 
def isValidDecInput(sDecInput):
    valid = True
    if sDecInput == '':
        valid = False
        return valid
    validcharacters = "0123456789"
    for char in sDecInput:
        if char not in validcharacters or int(sDecInput)>4294967295:
            valid = False
            break
    return valid
 
def isValidHexInput(sHexInput):
    valid = True
    if sHexInput == '':
        valid = False
        return valid
    validcharacters = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
    if sHexInput[0:2] != "0x":
        valid = False
        return valid
    for char in sHexInput [2:]:
        if char.lower() not in validcharacters or len(sHexInput)>32:
            valid = False
            break
    return valid
      
def bin2dec(sBinInput):
    pwr=len(sBinInput[2:])-1 
    decNumber = 0 
    for char in sBinInput[2:]:
        decNumber += int(char)*(2**pwr) 
        pwr -= 1
    return str(decNumber)

def bin2hex(sBinInput):
    return dec2hex(bin2dec(sBinInput))  
  
def dec2bin(sDecInput):
    binNumber = ""
    sDecInput = int(sDecInput)
    while sDecInput > 1:
        binNumber += str(sDecInput % 2)
        sDecInput //= 2
    binNumber += str(sDecInput)
    return binNumber [::-1]

def dec2hex(sDecInput):
    hex = "0123456789ABCDEF"
    hexNumber = ""
    sDecInput = int(sDecInput)
    while sDecInput > 0:
        remainder = sDecInput % 16
        hexNumber += str(hex[remainder])
        sDecInput //= 16
    return hexNumber[::-1]

def hex2dec(sHexInput):
    decNumber = 0
    hexnum ="0123456789abcdef"
    pwr = len(sHexInput[2:])-1
    for char in sHexInput[2:]:
        decNumber += int(hexnum.find(char.lower()))*(16**pwr)
        pwr -= 1
    return decNumber

def hex2bin(sHexInput):
    return dec2bin(hex2dec(sHexInput))

def processBin(sInputNum): 
    if isValidBinInput(sInputNum):
        decNumber = str(bin2dec(sInputNum))
        binNumber = sInputNum
        hexNumber = "0x" + (bin2hex(sInputNum))
        result = (decNumber, binNumber, hexNumber)
        return result
    else:
        result = ("None", "Invalid Format", "None")
        return result
   
def processDec(sInputNum): 
    if isValidDecInput(sInputNum):
        decNumber = str(sInputNum)
        binNumber = "0b" + (dec2bin(sInputNum))
        hexNumber = "0x" + (dec2hex(sInputNum))
        result = (decNumber, binNumber, hexNumber)
        return result
    else:
        result = ("Invalid Format", "None", "None")
        return result
    
def processHex(sInputNum): 
    if isValidHexInput(sInputNum):
        decNumber = str(hex2dec(sInputNum))
        binNumber = "0b" + (hex2bin(sInputNum))
        hexNumber = sInputNum
        result = (decNumber, binNumber, hexNumber)
        return result
    else:
        result = ("None", "None", "Invalid Format")
        return result

def printResult(dbhTuple):
    return print(f"dec : {dbhTuple[0]} \nbin : {dbhTuple[1]} \nhex : {dbhTuple[2]}")

user = "0"
while user.upper() != "Q":
    print ("")
    print ("          DECIMAL  :  D..D, where D is 0-9")
    print ("           BINARY  :  0bB..B, where D is 0-1")
    print ("      HEXADECIMAL  :  0xS..S, where S is 0-9, A-F")
    print ("")
    number = (input("Enter a number using the notation above : "))
    x = number.replace("_","")
    print("")
    print(f"num : {x}")
    validchar = ("0123456789")
    if x[0:2] == "0b" and len(x[2:]) <= 32:
        result=processBin(x)
    elif x[0:2] == "0x" and len(x[2:]) <= 8:
        result=processHex(x)
    elif x[0:2] == "0b" and len(x[2:]) > 32:
        result=("None", "Invalid Format", "None")
    elif x[0:2] == "0x" and len(x[2:]) > 8:
        result=("None", "None", "Invalid Format")
    else:
        result=processDec(x)
    printResult(result)
    print("")
    user = str(input("Press any key to continue or Q/q to quit  :  "))
