with open('z3.1-1.txt') as f:
    numbers = [int(n) for n in f.readlines()]
    maxn, minn = max(numbers), min(numbers)
with open('srez.txt', 'w') as f:
    f.write(f'Макс: {maxn}\n')
    f.write(f'Мин: {minn}')

