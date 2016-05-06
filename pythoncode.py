def getarrayelment(a):
    for items in a:
        yield items;
def inter(array1):
    b=[]
    for items in array1:
        b.append(getarrayelement(items))

    
        
