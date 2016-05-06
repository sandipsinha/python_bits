def paisum(arr, k):
    if len(arr) <2:
        return
    arr.sort()
    left, right = (0, len(arr) - 1)
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentsum == k:
            print arr[left] + arr[arr[right]
            left +=1
        elif currentsum < k:
            left +=1
        else:
            right -=1                                  

def paisum2(arr, k):
    if len(arr) <2:
        return
    output = set()
    seen = set()
    for items in arr:
        m = k - items
        if m not in seen:
            seen.add(items)
        else:
            output.add((min(items, k), max(m, k)))
    print '\n'.join(map(str, list(output)))
       

                                  
                                  
                                  
