def array123(nums, strtocomp):
    print 'the original num ' , nums
    string1 = [str(item) for item in nums]
    stringtest = ','.join(string1)
    print 'the string test  is', stringtest
    return strtocomp in stringtest

a=[1, 1, 3, 3, 1]
print 'The test is', array123(a,'1,2,3')
