print(' - - Antigenicity Cover - - ')

d = 0

while True:
    a = int(input('Start site: '))
    b = int(input('End site '))

    c = b-a+1

    d = d + c

    open = str(input('Continuar? [S/N]'))
    if open == 'n':
        print(f'Cover: {d}')
        break
