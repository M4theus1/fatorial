n = int(input('''Digite um número para
calcular seu fatorial: '''))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))