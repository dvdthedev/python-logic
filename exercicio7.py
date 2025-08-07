print("Lanchonete")
print("1 Coxinha R$5,00")
print("2 Pastel R$7,00")
print("3 Café R$4,00")
print("4 Suco R$6,00")
print("5 SAIR")

opcao = 0
valor_total = 0

while(opcao != 5):
    opcao = int(input("Escolha uma opção entre 1 e 5: "))

    while (opcao < 1 or opcao > 5):
        opcao = int(input("Escolha uma opção entre 1 e 5: "))

    if (opcao == 5):
        break;

    quantidade = float(input("Qual a quantidade? "))
    if(opcao == 1):
        valor_total +=  5.00 * quantidade
    if(opcao == 2):
        valor_total += 7.00 * quantidade
    if(opcao == 3):
        valor_total += 4.00 * quantidade
    if(opcao == 4):
        valor_total += 6.00 * quantidade

if valor_total == False:
    print('Nenhum valor computado')
else:
    print(f'Valor total das vendas: R${valor_total:.2f}')