palavra = input('Digite uma palavra: ')

def bordinha(palavra):
        tracado = len(palavra)
        print('+' + '-' * tracado + '+')
        print('|' + palavra + '|')
        print('+' + '-' * tracado + '+')

bordinha(palavra)