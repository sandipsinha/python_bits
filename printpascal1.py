def create_sec_array(printarray):
    testa = []
    suma = 0
    for i in xrange(len(printarray) - 1 ):
        suma = printarray[i] +  printarray[i + 1]
        testa.append(suma)
    return testa
        

def draw_pascal(n):
    if n == 1:
        print n
        return
    for item in xrange(1,n+1):
        printarray = []

        for nums in xrange(1, item):
            if nums == 1:
                printarray.append(nums)
            else:
                arrice = 0
                totals = 0
                printarray = [1]
                #print 'the prevarray is ', prevarray
                #print 'the length is ', len(prevarray)
                if len(prevarray) > 2:
                    printarray.extend(testas)
                else:
                    printarray.append(2)
        printarray.append(1)
        testas = create_sec_array(printarray)
        #print 'the return array is ', testas
        theline = ' '.join(str(items) for items in printarray)
        prevarray = printarray
        
        
        print theline



draw_pascal(6)
            
