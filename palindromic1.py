def drawtriangle(lines):
    for n in xrange(1, lines+1):
        line = ''
        for x in xrange(1,n+1):
            line += str(x)
        if n > 1:
            s = n -1 
            #print 'the value of s is', s
            while s > 0:
                line += str(s)
                s -= 1
        print line

drawtriangle(5)
