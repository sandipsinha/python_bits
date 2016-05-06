from random import randint
y = 21533456
uniques = []
for i in range(y):  
    x1 = str(randint(500, 5000))
    x2 = str(randint(500, 5000))
    x3 = str(randint(500, 5000))
    x4 = str(randint(500, 5000))
    x = (x1 + ", " + x2 + ", " + x3 + ", " + x4)
    if x in uniques:
        raise Exception('We duped the sequence %d at iteration number %d' % (x, i))
    else:
        raise Exception('Couldn\'t find a repeating sequence in %d iterations' % (y))
    uniques.append(x)
