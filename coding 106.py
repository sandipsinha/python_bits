def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        print 'pline is', p_line
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        print 'line is ', line
        line.insert(0,1)
        print 'line is after insert ', line
        line.append(1)
        print 'line is after append ', line
    return line

print(pascal(6))
