def findindex(array, val):
    floor = 1
    ceil  = len(array)


    while floor < ceil:
        mid = (ceil+floor)/2 + 1
        print 'Value of floor and ceiling is ', floor ,' And ', ceil, 'And', mid
        if array[mid] > val:
            ceil = mid
        elif array[mid] < val:
            floor = mid
        else:
            return mid

onesucharray=[2,4,7,8,9,12,13,18, 19,20, 34, 35, 36, 38, 43, 46, 49, 53, 59, 61, 73, 79, 81]
print findindex(onesucharray, 8)
            
  
    
