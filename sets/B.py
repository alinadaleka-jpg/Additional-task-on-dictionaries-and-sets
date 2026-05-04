a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())
common = a.intersection(b)
print(len(common))
