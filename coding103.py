from random import shuffle
def annograms(word):
    m=list(word)
    print 'array ', m
    x=''
    while True:
        shuffle(m)
        x=''.join(m)
        print 'shuffled word', x
        if x != word:
            break
        return x

        



if __name__ == "__main__":

    print annograms("train")
    print '--'
    print annograms('drive')
    print '--'
    print annograms('python')
