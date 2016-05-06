from collections import OrderedDict
import string  

als = dict.fromkeys(string.ascii_lowercase, 0)

def is_panagram(words):
    for letter in words:
        if letter.strip(' ') > ' ': 
            cav = letter.lower()
            als[cav] += 1  

    newl = [vals for vals in als.values()]
    if 0 in newl:
        return False
    else:
        return True


if __name__=="__main__":
    print 'The word radar is a panagram', is_panagram('The quick brown fox jumps over the lazy dog')
