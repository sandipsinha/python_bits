import string
letdict = {i:v for i, v in enumerate(list(string.ascii_lowercase))}
def nextletter(let):
    #print 'processing the letter', let
    letter=[key for key, value in letdict.iteritems() if value == let][0]
    if letter <= 23:
        letter+=2
        return letdict[letter]
    elif letter == 24:
        return letdict[0]
    elif letter == 25:
        return letdict[1]

 
message='http://www.pythonchallenge.com/pc/def/map.html'
decodestr=' '
for letters in message:
    if letters in letdict.values():
        decodestr+=nextletter(letters)
    else:
        decodestr+=letters

print decodestr
