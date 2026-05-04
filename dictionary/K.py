import sys
words = sys.stdin.read().split()
counts = {}
result = []
for word in words:
    result.append(counts.get(word, 0))
    counts[word] = counts.get(word, 0) + 1
print(*result)
