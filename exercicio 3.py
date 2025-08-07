# ano = int(input('Qual ano ?'))
#
# if(ano % 4 == 0):
#     print('Pode ser um ano bissexto')
# else:
#     print('Não é um ano bissexto')

# baixo = True
# cima = False
# if(baixo and cima):
#     print('Decida-se!')
# else:
#     print('Você escolheu um caminho!')

# lado_a = int(input('Qual a tamanho da lado a?'))
# lado_b = int(input('Qual a tamanho da lado b?'))
# lado_c = int(input('Qual a tamanho da lado c?'))

# if(min(lado_a, lado_b, lado_c) <= 0):
#     print('Triângulo não tem lados menores ou igual a 0')
#
# elif(lado_a + lado_b < lado_c or lado_a + lado_c < lado_b or lado_c + lado_b < lado_a):
#     print('Triângulos não tem um lado maior que a soma dos outros dois')
# elif(lado_a == lado_b and lado_a == lado_c):
#     print('Triângulo Equilátero')
# elif(lado_b != lado_a and lado_b != lado_c):
#     print('Triângulo Escaleno')
# else:
#     print("Triângulo Isósceles")
print('Calculadora')

print('Operações:')
print('/ Divisão')
print('* Multiplicação')
print('+ Soma')
print('- Subtração')

operacao = input('Qual operacao deseja realizar?')

a = int(input('Digite o valor do a?'))
b = int(input('Digite o valor do b?'))

resultado = 0

if operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b
elif operacao == '/':
    resultado = a / b

print(f'Resultado: {resultado}')