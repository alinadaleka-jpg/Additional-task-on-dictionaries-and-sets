import sys
accounts = {}
for line in sys.stdin:
    line = line.strip()
    if not line or line == 'Exit':
        break
    data = line.split()
    cmd = data[0]
    if cmd == 'DEPOSIT':
        name, amount = data[1], int(data[2])
        accounts[name] = accounts.get(name, 0) + amount
    elif cmd == 'WITHDRAW':
        name, amount = data[1], int(data[2])
        accounts[name] = accounts.get(name, 0) - amount
    elif cmd == 'BALANCE':
        name = data[1]
        print(accounts[name] if name in accounts else 'ERROR')
    elif cmd == 'TRANSFER':
        name1, name2, amount = data[1], data[2], int(data[3])
        accounts[name1] = accounts.get(name1, 0) - amount
        accounts[name2] = accounts.get(name2, 0) + amount
    elif cmd == 'INCOME':
        percent = int(data[1])
        for name in accounts:
            if accounts[name] > 0:
                accounts[name] = int(accounts[name] * (100 + percent) // 100)