
'''
Given an amount, return a list of the minimum number of coins that could add up to that
amount
'''
def get_min_coins(amount_rem):
    coin_combinations = [1,5,10,25]
    coin_list = []
    
    for coin_val in sorted(coin_combinations,reverse=True):
        coin_count = amount_rem/coin_val
        coin_list += [coin_val,] * coin_count
        amount_rem -= coin_val * coin_count 
        
    return coin_list
if __name__ == '__main__':
    
    total_amount = 53 # unit: US cents = $1.06
    print get_min_coins(total_amount)
