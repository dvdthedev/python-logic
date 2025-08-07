quantidade = float(input('Quantidade de kWh: '))
print('C - Comércio')
print('I - Industria')
print('R - Residencial')
tipo = input('Tipo de instalação: ')
valor = 0

if tipo == 'R':
    if quantidade < 500:
        valor = quantidade * 0.40
    else:
            valor = quantidade * 0.65
if tipo == 'C':
    if quantidade < 1000:
        valor = quantidade * 0.55
    else:
            valor = quantidade * 0.60
if tipo == 'I':
    if quantidade < 5000:
        valor = quantidade * 0.55
    else:
            valor = quantidade * 0.60

print(f'Valor: {valor}')