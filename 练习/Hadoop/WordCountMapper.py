import sys

for line in sys.stdin:
    words = line.split(" ")
    print(words + '\t' +1)
