def findmin(coinarray,change, minCoins):
    for cents in range(change+1):
        mincoin = cents
        for j in [c for c in coinarray if c <= cents]:
            if minCoins[cents-j]+1 < mincoin:
                mincoin = minCoins[cents-j]+1
        minCoins[cents] = mincoin

    return minCoins[change]

clist = [1,5,10,21,25]
amt = 40
print findmin(clist, amt,[0]*41)
