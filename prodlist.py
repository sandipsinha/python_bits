def findnum(int_list):

    products_of_all_ints_before_index = [None] * len(int_list)
    lookahead_of_all_ints_after_iindex = [None] * len(int_list)
    # for each integer, find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in xrange(len(int_list)):
        products_of_all_ints_before_index[i] = product_so_far
        product_so_far *= int_list[i]
    look_ahead = 1
    j = len(int_list) - 1 
    while j >= 0:
        #print 'the value of j is ' , j , 'And', products_of_all_ints_before_index[j], 'And', look_ahead
        products_of_all_ints_before_index[j] *= look_ahead
        look_ahead *= int_list[j]
        j -= 1
            


    return products_of_all_ints_before_index

##test_array = [3, 1, 2, 5, 6, 4]

test_array = [1, 2, 6, 5, 9]
print findnum(test_array)
