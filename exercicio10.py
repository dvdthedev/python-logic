ingressos = 0
acumulador_valor = 0
idades = 0

while True:
    idade = int(input('Insira sua idade: '))

    if idade <= 0:
        break

    elif idade < 3:
        ingressos += 1
        idades += idade
        print('idade 1')

    elif idade > 12:
        ingressos += 1
        idades += idade
        acumulador_valor += 30
        print('idade 2')

    else:
        ingressos += 1
        idades += idade
        acumulador_valor += 15
        print('idade 3')

print(f'Quantidade de ingressos: {ingressos}')
print(f'Valor arrecadado: R${acumulador_valor}')
print(f'Média de idade: {idades / ingressos}')
