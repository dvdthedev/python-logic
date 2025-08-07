
acumulador = 0

i = 1

while(i <= 5):
    nota = float(input('Digite sua nota: '))
    acumulador += nota
    i += 1

print(f'Média final: {acumulador / (i-1)}')