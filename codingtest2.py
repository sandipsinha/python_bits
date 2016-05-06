from collections import deque

def rotateArray(L,n):
    d = deque(L)
    d.rotate(n)
    m=list(d)
    n=[int(i) for i in m]
    return n

def Main():
    n=input('Enter a number')
    l=[1, 2, 3, 4, 5, 6]
    m=[str(i) for i in l]
    print 'The rotated array is ', rotateArray(l,n)


if __name__ == '__main__':
    Main()
