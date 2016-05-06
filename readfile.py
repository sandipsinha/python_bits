with open('test1.csv') as f:
    lines = f.read().splitlines()

betterarray=[item for item in lines if item > ' ']

print len(lines)

print len(betterarray)

print 'first line', lines[0]

print 'second line', lines[1]

print 'first line', betterarray[0]

print 'second line', betterarray[1]

    
