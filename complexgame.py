import math
def create_complex_tuple(i,d):
    return complex(i, d)

def calculate(n1, n2):

    s3 = n1 + n2

    print str(int(s3.real)) + '+' + str(int(s3.imag)) + 'i'

    print n1 - n2

    print n1 * n2

    print n1 / n2

    print n1 * n2

    sq_real = n1.real**2

    sq_imag = n1.imag**2

    print math.sqrt(   sq_real +    sq_imag)

    sq_real = n2.real**2

    sq_imag = n2.imag**2

    print math.sqrt(   sq_real +    sq_imag)
 


lista = [int(items) for items in raw_input().split()]

fcomp1 = create_complex_tuple(lista[0], lista[1])

listb = [int(items) for items in raw_input().split()]
fcomp2 = create_complex_tuple(listb[0], listb[1])

calculate(fcomp1, fcomp2)

                    
    
