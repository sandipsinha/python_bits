def findsqrt(x,a):
    while True:
        print x
        y=(x+a/x)/2
        if y == x:
            break
        x = y

if __name__== "__main__":
    print findsqrt(2,16)
