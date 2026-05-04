numbers = [int(x) for x in input().split()]
seen = set()
for x in numbers:
    if x in seen:
        print("YES")
    else:
        print("NO")
        seen.add(x)