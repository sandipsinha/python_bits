def find_max_value(cakes,capacity):
    max_value = 0
    current_max_value = 0
    max_capacity_array = [0]* (capacity+1)
    for weight in xrange(1, capacity+1):
        for cake_w, cake_v in cakes:
            if cake_w <= weight:
                max_value_using_cake = cake_v + max_capacity_array[weight - cake_w]
                current_max_value = max(current_max_value, max_value_using_cake)

        max_capacity_array[weight] = current_max_value

    return max_capacity_array[-1]

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20
print find_max_value(cake_tuples, capacity)
        

        
        
