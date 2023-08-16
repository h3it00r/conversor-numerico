import time
import os

class HexDec:

    def __init__(self):
        self.__numero = None
        self.__resultado = 0
    
    '''Retorna o tamanho do dado fornecido.'''
    def __tamanho(self):
        return len(self.__numero)
    
    '''Validação do dado fornecidos.'''
    def __dado_valido(self):
        for i in range (self.__tamanho()):
            if ((self.__numero[i]) < 'A' or (self.__numero[i]) > 'F') and ((self.__numero[i]) < '0' or (self.__numero[i]) > '9'):
                return False
        return True
    
    '''Método usado para a entrada de dados.'''
    def __entrada (self):
        '''Loop executado enquando o dado fornecido for inválido.'''
        while True:
            self.__numero = input('Digite um número hexadecimal para convertê-lo em decimal: ').upper()
            time.sleep(3)
            os.system('cls')
            '''Caso o dado fornecido seja inválido, um a mensagem abaixo é exibida.'''
            if not self.__dado_valido():
                print('Você deve digitar um número hexadecimal para convertê-lo em decimal.')
                time.sleep(3)
                os.system('cls')
            else:
                return

    '''Conversão hexadecimal - binário.'''
    def __conversao (self):
        posicao = self.__tamanho() - 1
        for i in range (self.__tamanho()):
            if self.__numero[i] >= 'A' and self.__numero[i] <= 'F':
                valor = ord(self.__numero[i]) - 55
                self.__resultado += (valor * 16 ** posicao)
                posicao -= 1
            
            else:
                valor = ord(self.__numero[i]) - 48
                self.__resultado += (valor * 16 ** posicao)
                posicao -= 1
        
        print(f'{self.__numero} no sistema hexadecimal é igual a {self.__resultado}',end='')
        print(' no sistema decimal.')
        self.__resultado = 0
        time.sleep(5)
        os.system('cls')

    '''Início do processo de conversão hexadecimal - decimal.'''        
    def iniciar(self):
        '''Chamada para o método de entrada de dados.'''
        self.__entrada()
        '''Chamada para a conversão do número.'''
        self.__conversao()