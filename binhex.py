import time
import os

class BinHex:

    def __init__(self):
        self.__numero = None
        self.__linhas = None
        self.__colunas = 4
        self.__mat = None
        self.__resultado = ''

    '''Retorna o tamanho do dado fornecido.'''
    def __tamanho(self):
        return len(self.__numero)
    
    '''Validação do dado fornecidos.'''
    def __dado_valido(self):
        for i in range (self.__tamanho()):
            if self.__numero[i] not in ('0','1'):
                return False
        return True
    
    '''Método usado para a entrada de dados.'''
    def __entrada (self):
        '''Loop executado enquando o dado fornecido for inválido.'''
        while True:
            self.__numero = input('Digite um número binário para convertê-lo em hexadecimal: ')
            time.sleep(3)
            os.system('cls')
            '''Caso o dado fornecido seja inválido, um a mensagem abaixo é exibida.'''
            if not self.__dado_valido():
                print('Você deve digitar um número binário para convertê-lo ao sistema hexadecimal.')
                time.sleep(3)
                os.system('cls')
            else:
                return
            
    '''Cálculo do resto. É usado para a criação da matriz vazia'''        
    def __resto (self):
        return self.__tamanho() % 4
    
    '''Cálculo de número usado para o preenchimento da matriz com o dado fornecido.'''
    def __calculo (self):
        if self.__resto() != 0:
            calc = 4 - self.__resto()
        else:
            calc = 4 - 4
        return calc
    
    '''Criação da matriz vazia, que servirá de base para a conversão.'''
    def __matriz_vazia (self):
        if self.__tamanho() <= 4:
            self.__linhas = 1
            self.__mat = [[None] * self.__colunas for i in range(self.__linhas)]
        if self.__tamanho() > 4 and self.__resto() == 0:
            self.__linhas = self.__tamanho()//4
            self.__mat = [[None] * self.__colunas for i in range(self.__linhas)]
        if self.__tamanho() > 4 and self.__resto() != 0:
            self.__linhas = (self.__tamanho()//4) + 1
            self.__mat = [[None] * self.__colunas for i in range(self.__linhas)]
    
    '''Preenchimento da matriz com o dado fornecido para a conversão.'''
    def __matriz (self):
        cont = 0
        tam = self.__tamanho()
        for l in range (self.__linhas):
            for c in range (self.__colunas):
                if self.__calculo() == 0:
                    self.__mat [self.__linhas - l - 1][4 - c - 1] = self.__numero[tam - c - 1]
                if self.__calculo() > 0 and l < self.__linhas - 1:
                    self.__mat [self.__linhas - l - 1][4 - c - 1] = self.__numero[tam - c - 1]
                if self.__calculo() > 0 and l == self.__linhas - 1 and c < self.__calculo():
                    self.__mat [self.__linhas - l - 1][c] = '0'
                if self.__calculo() > 0 and l == self.__linhas - 1 and c >= self.__calculo():
                    self.__mat [self.__linhas - l - 1][c] = self.__numero[cont]
                    cont += 1
            tam -= 4
    
    '''Dicionário usado para fazer a conversão numérica.'''
    def __dicionario_bin_hex (self, numero):
        num = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', '1000':'8', 
               '1001':'9', '1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'}
        return num[numero]
    
    '''Conversão binário - hexadecimal.'''
    def __conversao (self):
        num = ''
        for l in range (self.__linhas):
            for c in range (self.__colunas):
                num += self.__mat[l][c]
            self.__resultado += self.__dicionario_bin_hex(num)
            num = ''
        
        '''Resultado da conversão.'''
        print(f'{self.__numero} no sistema binário é igual a {self.__resultado}',end='')
        print(' no sistema hexadecimal.')
        self.__resultado = ''
        time.sleep(5)
        os.system('cls')
    
    '''Início do processo de conversão binário - hexadecimal.'''        
    def iniciar(self):
        '''Chamada para o método de entrada de dados.'''
        self.__entrada()
        '''Criação da matriz vazia que servirá para o processo de conversão.'''
        self.__matriz_vazia()
        '''Preenchimento da matriz com o dado fornecido.'''
        self.__matriz()
        '''Chamada para a conversão do número.'''
        self.__conversao()