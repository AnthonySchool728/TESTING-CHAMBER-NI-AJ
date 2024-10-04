course = 'EEE111'
message = 'Hello'

# Hello EEE111 !!!
helloString = message +' '+ course + ' !!!'
print(helloString)

helloString = f'{message} {course} !!!'
print(helloString)

def test_helloString():

    """ simple test """
    
    assert (helloString == 'Hello EEE111 !!!')