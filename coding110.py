wordcounts={}
with open('exam.txt') as f:
    texts = f.read()
    sentences = texts.split(' ')
    sentences.replace(',','')
    sentences.replace('.','')
    for word in sentences:
        if word.lower() in wordcounts:
            wordcounts[word.lower()] =  wordcounts[word.lower()] + 1
        else:
            wordcounts[word.lower()] = 1
            
