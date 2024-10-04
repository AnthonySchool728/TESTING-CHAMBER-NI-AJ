from bin2dec import isValidInput, bin2dec
import random

def bin2dec_RefModel(binaryString):
    decValue = int(binaryString, 2)
    return decValue

def test_isValidInput():
    assert(isValidInput('1010101_101010101'))
    for iter in range(20):
        testNum = random.randrange(0, 2**32)
        print(f'isValidInput({bin(testNum)[2:]})')
        assert(isValidInput(bin(testNum)[2:]))
# adsada
def test_bin2dec():
    for iter in range(20):
        testNum = random.randrange(0, 2**32)
        print(f'bin2dec({bin(testNum)[2:]})')
        print(f'expected : {bin2dec_RefModel(bin(testNum)[2:])}')
        print(f'actual   : {bin2dec(bin(testNum)[2:])}')
        assert(bin2dec(bin(testNum)[2:])==bin2dec_RefModel(bin(testNum)[2:]))