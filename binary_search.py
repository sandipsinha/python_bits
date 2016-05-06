def findinorderedset(looker, key):
    floor = -1
    ceiling = len(looker) 
    while floor <= ceiling - 2:
        mid_point = (floor + ceiling)/2
        print 'the mid point is', mid_point
        guess_num = looker[mid_point]
        if guess_num == key:
            return mid_point
        elif guess_num > key:
            ceiling = mid_point
        elif guess_num < key:
            floor = mid_point
        print 'floor, ceiling is', floor, ceiling
    return -1


a=[2,3,4,5,6,8,9,10,11,12,13,15,16,18]
print 'The number is ' , findinorderedset(a,19)
