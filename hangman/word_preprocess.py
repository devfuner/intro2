words = []

with open('words_org.txt', 'r') as f:
    for l in f.readlines():
        print(l.split('\t')[0])
        words.append(l.split('\t')[0])

with open('words.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')
