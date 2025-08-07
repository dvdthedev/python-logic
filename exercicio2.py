from operator import truediv

var = 2 + 2
if(var < 4):
    print(True)

if(7 // 3 == 1 + 1):

    print(True)

if((3 ** 2) + (4 ** 2) == 25):
    print("Sim")

if(2+4+6 < 12):
    print(True)

if (1387 % 19 == 0):
    print("Sim")

if (31 % 2 != 0):
    print("Ímpar")

if(min(29,30,34) < 30):
    print("É menor!")

idade = int(input('Idade?'))

if(idade > 60):
    print("Você tem direito aos benefícios!")

dano = int(input('Dano ?'))
escudo = int(input('Escudo ?'))
if(dano > 10 and escudo <= 0):
    print("Você está morto!")

norte = True
sul = False

if(norte or sul):
    print('Escapou')