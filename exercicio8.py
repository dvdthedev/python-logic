valor = int(input('Digite um valor: '))


while valor != 0:

    while valor >= 100:
        cedulas = valor // 100
        valor = valor - cedulas * 100
        print('Cedulas de 100: {}'.format(cedulas))
    while valor >= 50:
        cedulas = valor // 50
        valor = valor - cedulas * 50
        print('Cedulas de 50: {}'.format(cedulas))
    while valor >= 20:
        cedulas = valor // 20
        valor = valor - cedulas * 20
        print('Cedulas de 20: {}'.format(cedulas))
    while valor >= 10:
        cedulas = valor // 10
        valor = valor - cedulas * 10
        print('Cedulas de 10: {}'.format(cedulas))
    while valor >= 5:
        cedulas = valor // 5
        valor = valor - cedulas * 5
        print('Cedulas de 5: {}'.format(cedulas))
    while valor >= 1:
        cedulas = valor // 1
        valor = valor - cedulas * 1
        print('Cedulas de 1: {}'.format(cedulas))



