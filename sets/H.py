n = int(input())
possible = set(range(1, n + 1))
while True:
    line = input()
    if line == 'HELP':
        break
    guess = set(map(int, line.split()))
    if len(possible & guess) > len(possible) / 2:
        print('YES')
        possible &= guess
    else:
        print('NO')
        possible -= guess
print(*sorted(possible))