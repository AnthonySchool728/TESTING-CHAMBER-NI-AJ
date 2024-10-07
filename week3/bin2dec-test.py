from bin2dec import isValidInput, bin2dec
import random

def bin2dec_RefModel(binaryString):
    decValue = int(binaryString, 2)
    return decValue

def test_isValidInput_Valid():
    assert(isValidInput('1_1101'))
    assert(isValidInput('00_10'))
    for iter in range(50):
        testNum = random.randrange(0, 2**5)
        print(f'isValidInput({bin(testNum)[2:]})')
        assert(isValidInput(bin(testNum)[2:]))

def test_bin2dec():
    for iter in range(50):
        testNum = random.randrange(0, 2**5)
        print(f'bin2dec({bin(testNum)[2:]})')
        print(f'expected : {bin2dec_RefModel(bin(testNum)[2:])}')
        print(f'actual   : {bin2dec(bin(testNum)[2:])}')
        assert(bin2dec(bin(testNum)[2:])==bin2dec_RefModel(bin(testNum)[2:]))

def test_isValidInput_Invalid():
    assert(not isValidInput('2_10101'))
    for iter in range(50):
        testNum = random.randrange(33, 50)
        print(f'isValidInput({bin(testNum)[2:]})')
        assert(not isValidInput(bin(testNum)[2:]))
        
test_bin2dec()