n, m = map(int, input().split())
irina = {int(input()) for _ in range(n)}
igor = {int(input()) for _ in range(m)}
common = sorted(irina & igor)
print(len(common))
print(*common)
only_irina = sorted(irina - igor)
print(len(only_irina))
print(*only_irina)
only_igor = sorted(igor - irina)
print(len(only_igor))
print(*only_igor)