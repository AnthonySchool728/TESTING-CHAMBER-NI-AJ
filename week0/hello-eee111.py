<<<<<<< HEAD
course = 'EEE111'
message = 'Hello'

# Hello EEE111 !!!
helloString = message +' '+ course + ' !!!'
print(helloString)

helloString = f'{message} {course} !!!'
print(helloString)

def test_helloString():

    """ simple test """
    
=======
course = 'EEE111'
message = 'Hello'

# Hello EEE111 !!!
helloString = message +' '+ course + ' !!!'
print(helloString)

helloString = f'{message} {course} !!!'
print(helloString)

def test_helloString():

    """ simple test """
    
>>>>>>> e7217ce0d926c387758e0484a8164991810cf7e1
    assert (helloString == 'Hello EEE111 !!!')