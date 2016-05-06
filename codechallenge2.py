def findtotexchange(n,somearry):
    if n < 2:
        return 0
    totex = 0.0
    sumret = 0.0
    average = sum(somearry)/n
    print 'The per person expense is', average
    for x in xrange(n):
        if somearry[x] > average:
            totex += somearry[x] - average
            sumret +=  somearry[x] - average
        elif somearry[x] < average:
            totex = totex - (average - somearry[x])
        #print 'Item is', somearry[x], 'And the diff is', totex, 'and the tot', sumret

    return sumret

num_of_students = int(raw_input())
#assert(num_of_students is number)
expense_array=[]
for item in xrange(num_of_students):
    n = float(raw_input())
    expense_array.append(n)

print findtotexchange(num_of_students, expense_array )
    
    
    
