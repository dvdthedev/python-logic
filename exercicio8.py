valor = int(input("Digite um valor: "))

while valor != 0:
    while valor >= 100:
        cedula = valor // 100
        valor = valor - cedula * 100
        print(f'Cédulas de R$100: {cedula}')
    while valor >= 50:
        cedula = valor // 50
        valor = valor - cedula * 50
        print(f'Cédulas de R$50: {cedula}')
    while valor >= 20:
        cedula = valor // 20
        valor = valor - cedula * 20
        print(f'Cédulas de R$20: {cedula}')
    while valor >= 10:
        cedula = valor // 10
        valor = valor - cedula * 10
        print(f'Cédulas de R$10: {cedula}')
    while valor >= 5:
        cedula = valor // 5
        valor = valor - cedula * 5
        print(f'Cédulas de R$5: {cedula}')
    while valor >= 1:
        cedula = valor // 1
        valor = valor - cedula * 1
        print(f'Cédulas de R$1: {cedula}')
