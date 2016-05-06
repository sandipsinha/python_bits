with open('alphabet.txt') as f:
    p = f.readline()
    while p:
        print p
        p = f.readline()
