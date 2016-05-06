def palindrome(stringpal):
    tempar = set(stringpal)
    print tempar
    count = 0
    templ = list(tempar)
    print templ
    for items in tempar:
        if stringpal.count(items) % 2 != 0:
            count += 1

    if count > 1 or count == 0:
        return False
    else:
        return True

print palindrome('civic')
        
