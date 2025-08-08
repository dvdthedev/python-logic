
def calc_fatorial(numero):

    """
    Função que calcula o fatorial de um numero inteiro
    :param numero:
    :return fatorial:
    """

    if valida_fatoravel(numero) == False:
        print('Numero invalido')
    elif numero == 0:
            return 1;

    else:
        acumulador = numero

        for i in range(numero,1,-1):

            numero = numero - 1
            acumulador *= numero

        return acumulador

def valida_fatoravel(numero):
    if numero == 0:
        return True
    elif numero > 0:
        return True
    else:
        return False

try:
    print(calc_fatorial(int(input('Digite um numero inteiro positivo para a fatoração: '))))
except:
    print('Você não digitou um numero inteiro postiivo')