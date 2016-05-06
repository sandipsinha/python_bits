
a='aaaaaaabbbcccccddddeeeeefffffgghiiiiiiijjjjj'

b=list(a)

c=set(b)

d=list(c)
max=0
run=0
prev=0
letters=''
for items in d:
    curr=b.count(items)
    if curr > max:
        max=curr
        letters=items
print max , ' is the number of occurance of this etter ', letters 
