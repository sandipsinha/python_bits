def findways(current_coin, target):
    if target % current_coin == 0:
        return 1

def findotherways(current_coin, denomination, target):
    if (target % current_coin) in denomination:
        return 1

def findthirdway(current_coin, denomination, target):
    if denomination:
        current_total = current_coin + denomination[0]
    if current_total == target:
        return 1
    elif current_total > target:
        if denomination[1:]:
            findthirdway(current_coind, denomination[1:], target)
        else:
            return 0
    else:
        
        


    
    
        
        
    

def create_recurring_array(coin_change, target):
    possible_ways = 0
    useful_ways  = 0
##    for coin in coin_change:
##        #print 'Now working with', coin
##        get_value = findways(coin, target)
##        #print 'Now getting', get_value 
##        possible_ways += get_value
    next_array = []
    next_array.extend(coin_change)
    for coin in coin_change:
        next_array.remove(coin)
        print 'now calling with', coin, next_array
        useful_ways += findotherways(coin, next_array, target)
    print 'The other way is', useful_ways 

    print 'the possible ways', possible_ways

create_recurring_array([1,2,3], 4)
        
        
