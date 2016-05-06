def creatPalindrome(n):
    if n == 1:
        return 1
    apps = []
    for x in range(1,n):
        apps.append(str(x))

    xsd = ''.join(apps) + str(n)
    spp = reversed(apps)
    return xsd+''.join(spp)

for x in xrange(1,6):
    print creatPalindrome(x)
