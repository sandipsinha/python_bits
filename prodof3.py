def highest_prod_of_3(testar):
    highest_prod_of_two = testar[0] * testar[1]
    lowest_prod_of_two = testar[0] * testar[1]
    highest_prod_of_three = testar[0] * testar[1]*  testar[2]
    highestnum = max(testar[0],testar[1],testar[2])
    lowestnum = min(testar[0],testar[1],testar[2])


    for items in xrange(1, len(testar)):
        highest_prod_of_two = max(highest_prod_of_two, testar[items]*highestnum)
        lowest_prod_of_two = min(lowest_prod_of_two, testar[items]* lowestnum)
        highest_prod_of_three = max(highest_prod_of_three, testar[items]*highest_prod_of_two)
        highest_prod_of_three = max(highest_prod_of_three, testar[items]*lowest_prod_of_two)

    return highest_prod_of_three

list_of_ints = [1, 10, -5, 1, -100]

print 'the highest product of three is', highest_prod_of_3(list_of_ints)
        
        
