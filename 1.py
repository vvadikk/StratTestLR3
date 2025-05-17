n = int(input('Введите n: '))
while n >= 10 or n < 1:
    print('n ∈ [1; 9]')
    n = int(input('Введите n: '))
else:
    for i in range(1, n + 1):
        print('$' + (i - 1) * ' ' + '$')
