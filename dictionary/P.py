import sys
words = sys.stdin.read().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: (-x[1], x[0]))
for word, count in items:
    print(word)