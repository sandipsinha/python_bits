# Enter your code here. Read input from STDIN. Print output to STDOUT
x=raw_input('Enter the length of the array: ')
y=raw_input('Enter the array in question: ')
entlist=[int(x) for x in y.split(' ')]
diff = entlist[1] - entlist[0]
diff1 = entlist[-1] - entlist[-2]
diffs = diff if diff1 > diff else diff1
z=[items for items in xrange(entlist[0],entlist[-1]+diffs,diffs)]
print 'The missing number is', sum(z) - sum(entlist)

