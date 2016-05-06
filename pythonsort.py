import random
def qsort(sortis):
    if len(sortis) < 2:
        return sortis
    else:
        anynumber = random.choice(sortis)
        qsmall = [i for i in sortis if i < anynumber]
        qmiddle = [i for i in sortis if i == anynumber]
        qbig = [i for i in sortis if i > anynumber]
        return (qsort(qsmall) + qmiddle + qsort(qbig))


def bubblesort(sortis):

    for i in xrange(len(sortis)):
        for j in xrange(i+1, len(sortis)):
            if sortis[i] > sortis[j]:
                sortis[i], sortis[j] = sortis[j], sortis[i]
    return sortis
                    
    



n = input("Enter a number")
x = []
for j in xrange(n):
    x.append(random.randint(1,n))

print x
print qsort(x)
print bubblesort(x)

    
                 
