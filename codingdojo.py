# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
no_of_shoes = int(input())
shoe_size_array=[int(x) for x in raw_input().split()]
no_of_cust = int(input())
shoe_dict = {}
valuear = []
for items in xrange(no_of_cust):
    size, price = raw_input().split()
    valuear.append((int(size), int(price)))

total_money = 0
for items in valuear:
    if items[0] in shoe_size_array:
        shoe_size_array.remove(items[0])
        total_money += items[1]
print total_money
        
