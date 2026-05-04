import sys
votes = {}
for line in sys.stdin:
    if not line.strip():
        continue
    candidate, count = line.split()
    count = int(count)
    votes[candidate] = votes.get(candidate, 0) + count
for candidate in sorted(votes.keys()):
    print(candidate, votes[candidate])