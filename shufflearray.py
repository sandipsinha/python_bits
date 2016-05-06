import random
def get_all_combinations(a):
    test_array = []
    start_index = -1
    while True:
        slicing = random.randint(1,len(a))
        print 'slicing is', slicing
        if slicing < len(a) - (start_index+1):
            test_array.append(a[start_index+1:slicing])
        elif len(a) == start_index:
            break
        else:
            test_array.append(a[start_index+1:slicing])
            break
        start_index += slicing
        print 'start index is ', start_index
    return test_array

a = '123'

print get_all_combinations(a)
        
            
            
        
        
        
        
    
