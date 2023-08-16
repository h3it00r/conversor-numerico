import time
import os

class BinDec:

    def __init__(self):
        self.__numero = None
        self.__resultado = 0

    '''Retorna o tamanho do dado fornecido.'''
    def __tamanho(self):
        return len(self.__numero)

    '''Validação do dado fornecidos.'''
    def __dado_valido(self):
        for i in range (self.__tamanho()):
            if self.__numero[i] not in ('0','1'):
                return False
        return True
    
    '''Conversão binário - decimal.'''
    def __conversao (self):
        valor = 2 ** (self.__tamanho() - 1)
        for i in range (self.__tamanho()):
            if self.__numero [i] == '1':
                self.__resultado += valor
            valor /= 2
        
        '''Resultado da conversão.'''
        print(f'{self.__numero} no sistema binário é igual a {self.__resultado:.0f}',end='')
        print(' no sistema decimal.')
        self.__resultado = 0
        time.sleep(5)
        os.system('cls')
    
    '''Método usado para a entrada de dados.'''
    def __entrada (self):
        '''Loop executado enquando o dado fornecido for inválido.'''
        while True:
            self.__numero = input('Digite um número binário para convertê-lo em decimal: ')
            time.sleep(3)
            os.system('cls')
            '''Caso o dado fornecido seja inválido, um a mensagem abaixo é exibida.'''
            if not self.__dado_valido():
                print('Você deve digitar um número binário para convertê-lo ao sistema decimal.')
                time.sleep(3)
                os.system('cls')
            else:
                return
    
    '''Início do processo de conversão binário - decimal.'''        
    def iniciar(self):
        '''Chamada para o método de entrada de dados.'''
        self.__entrada()
        '''Chamada para a conversão do número.'''
        self.__conversao()