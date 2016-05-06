def get_max_profit(stock_price):
    min_price = stock_price[0]
    max_price = stock_price[1]
    profit = max_price - min_price
    max_profit = 0
    for ind, i in enumerate(stock_price):
        min_price = min(min_price, i)
        #print 'The minimum price is ', min_price
        for sellprice in stock_price[ind+1:]:
            print 'The sell price is ', sellprice
            if sellprice > min_price:
                profit = sellprice-min_price
                max_profit = max(max_profit, profit)
    return max_profit


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print 'The max profit possible is ' , get_max_profit(stock_prices_yesterday)
    
