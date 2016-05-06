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
                    for arrs in xrange(len(prevarray)-1):
                        totals = prevarray[arrice] + prevarray[arrice + 1]
                        printarray.append(totals)
                        #print 'The values are', prevarray[arrice], ' ', prevarray[arrice + 1]
                        arrice+=1
                else:
                    printarray.append(2)
        printarray.append(1)
        theline = ' '.join(str(items) for items in printarray)
        prevarray = printarray
        
        
        print theline



draw_pascal(6)
            
