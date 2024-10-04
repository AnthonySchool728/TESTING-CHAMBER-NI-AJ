from week1 import eee111String, sum12, hypotenuse, getHypo

def test_EEE111():
    assert (eee111String == 'EEE111')

def test_cast2int():
    assert (sum12 == 333)

def test_mathFunctions():
    assert(hypotenuse(30, 40) == 50)
    assert(hypotenuse(500, 1200) == 1300)

def test_funcAssign():
    assert(getHypo(30, 40) == 50)
    assert(getHypo(500, 1200) == 1300)
