import string
import random

def passwordgen():
    pickupd = {0:'alpha1',1:'alphau',2:'signs',3:'numbers'}
    alpha1 =  dict(zip(range(1,27), string.ascii_lowercase))
    alpha2 =  dict(zip(range(1,27), string.ascii_uppercase))
    signs = {0:'!',1:'?',2:'~',3:'&'}

    passcode = ''
    for i in xrange(8):
        j = random.randint(0,3)
        if j == 0:
            passcode += alpha1.get(random.randint(0,25))
        elif j == 1:
            passcode += alpha2.get(random.randint(0,25))
        elif j == 2:
            passcode += str(signs.get(random.randint(0,2)))
        else:
            passcode += str(random.randint(0,9))
    return passcode

for j in xrange(9): 
    print 'The password is ' + str(j) + passwordgen()

                    
        
    



