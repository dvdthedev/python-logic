qualProduto = input('Qual produto deseja comprar? Banana, Maçã ou Laranja?')

qualPeso = float(input('Qual peso do produto?'))

if qualProduto.lower() == 'banana':
    print(1.90 * qualPeso)
if qualProduto.lower() == 'maçã':
    print(1.35 * qualPeso)
if qualProduto.lower() == 'laranja':
    print(1.50 * qualPeso)