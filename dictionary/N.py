import sys
words = sys.stdin.read().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
max_count = max(counts.values())
most_frequent = [word for word, count in counts.items() if count == max_count]
print(min(most_frequent))