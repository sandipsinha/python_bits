from collections import Counter
inptstr = raw_input()
inptarray = [c for c in inptstr]
k = Counter(inptarray).most_common(3)
print k
m = sorted(k, key = lambda x: str(x[1]) + x[0])
n = sorted(m, key = lambda x: x[1], reverse=True)
for items in n:
    print items[0], ' ', items[1]
