import sys

count = 0
word = ''
for line in sys.stdin:
    words = line.strip().split(" ")
    count += 1
    print(words)
    for word in words:
        print(word +"\t"+ "1")
    if count == 2:
        break
        