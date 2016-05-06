import collections
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    minnum = 0
    strind = 'N'
    print 'The type is ', type(args)
    for items in args:
        if items.isdigit():
            if minnum ==0 :
                minnum = items
            elif minnum > items:
                minnum = items
 
        else:
            strind = 'Y'
            if minnum == 0:
                minnum = ord(items)   
            if minnum > ord(items):
                minnum = ord(items)
            

    return minnum if strind == 'N' else chr(minnum) 


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    maxnum = 0
    if isinstance(args[0], collections.Iterable):
        for items in args:
            for row in items:
                if maxnum < row:
                    maxnum = row
            
    else:
        for items in args:
            print 'the non-iterables are ', items
            if items > maxnum:
                maxnum = items
    return maxnum
            


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
