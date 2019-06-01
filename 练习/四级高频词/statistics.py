import os
import re

base_path = './data/'
filenames = os.listdir(base_path)
all_words = []
stat = {}

# load data
print("loading data...")
for fn in filenames:
    print(fn)
    with open(os.path.join(base_path, fn), encoding='utf-8') as f:
        context = f.readlines()
    for line in context:
        words = line.strip().split()
        for i, word in enumerate(words):
            words[i] = ''.join(list(filter(str.isalpha, word))).lower()   # filter letter and ignore case 
        all_words.extend(words)

# wordcount
for word in all_words:
    stat[word] = stat.get(word, 0) + 1
word_count = sorted(stat.items(), key=lambda d: d[1], reverse=True)


# save result
totol_words = 0
with open('./result.csv','w', encoding='utf-8') as f:
    for word_num in word_count:
        totol_words += word_num[1]
        f.write(word_num[0] + ',' + str(word_num[1]) + '\n')
print(totol_words)