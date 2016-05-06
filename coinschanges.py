def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      print 'Cents', cents 
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
          print 'value of j', j
          print 'Value of minCoins', minCoins
          if minCoins[cents-j] + 1 < coinCount:
              coinCount = minCoins[cents-j]+1
              print 'coinCount is now', coinCount
          
      minCoins[cents] = coinCount
      print 'value of Array', minCoins
   return minCoins[change]

clist = [1,5,10,21,25]
amt = 40
print dpMakeChange(clist, amt,[0]*41)

