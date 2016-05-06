def sortuples(words):
    testa=[(items[0],items) for items in words]
    testa.sort()

    return [val for (key,val) in testa]

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    ]



print words.index(sortuples(words)[0])
