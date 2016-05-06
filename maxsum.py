def msum(a):
	return [(sum(a[j:i]), (j,i)) for i in range(1,len(a)+1) for j in range(i)]

a=[1,2,-5,4,7,-2]
print 'the max sum is ', msum(a)
