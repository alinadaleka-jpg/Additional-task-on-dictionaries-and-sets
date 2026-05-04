n = int(input())
possible = set(range(1, n + 1))
while True:
    line = input()
    if line == 'HELP':
        break
    guess = set(map(int, line.split()))
    answer = input()

    if answer == 'YES':
        possible &= guess
    else:
        possible -= guess
print(*sorted(possible))