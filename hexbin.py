import time
import os

class HexBin:
    
    def __init__(self):
        self.__numero = None
        self.__resultado = ''
    
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
            self.__numero = input('Digite um número hexadecimal para convertê-lo em binário: ').upper()
            time.sleep(3)
            os.system('cls')
            '''Caso o dado fornecido seja inválido, um a mensagem abaixo é exibida.'''
            if not self.__dado_valido():
                print('Você deve digitar um número hexadecimal para convertê-lo em binário.')
                time.sleep(3)
                os.system('cls')
            else:
                return
    
    '''Dicionário usado para fazer a conversão numérica.'''
    def __dicionario_hex_bin (self, numero):
        num = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', 
               '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
        return num[numero]
    
    '''Conversão hexadecimal - binário.'''
    def __conversao (self):
            for i in self.__numero:
                self.__resultado += self.__dicionario_hex_bin(i)
    
            print(f'{self.__numero} no sistema hexadecimal é igual a {self.__resultado}',end='')
            print(' no sistema binário.')
            self.__resultado = ''
            time.sleep(5)
            os.system('cls')
    
    '''Início do processo de conversão hexadecimal - binário.'''        
    def iniciar(self):
        '''Chamada para o método de entrada de dados.'''
        self.__entrada()
        '''Chamada para a conversão do número.'''
        self.__conversao()