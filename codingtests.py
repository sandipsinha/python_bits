
def sorto(a):
    for i1, e1 in enumerate(a):
        for i2, e2 in enumerate(a):
          #print 'before' , 'e1', e1, 'e2', e2
           if e2 > e1:
              e1 = a[i2]
              a[i2] = a[i1]
              a[i1] = e1
        print 'Now list is' , a  
    print 'The list is a', a

if __name__=="__main__":
    a=[7,2,3,9,1,4,5]
    print sorto(a)

