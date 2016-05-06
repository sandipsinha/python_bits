def fib(n):
   fibValues = [0,1]
   for i in range(2,n+1):
      fibValues.append(fibValues[i-1] + fibValues[i-2])
      print fibValues
   return fibValues[n]

def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print fib(4)

print fibo(4)
