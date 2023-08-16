import time
import os

class DecBin:

    def __init__(self):
        self.__numero = None
        self.__resultado = ''
    
    '''Retorna o tamanho do dado fornecido.'''
    def __tamanho(self):
        return len(self.__numero)

    '''Validação do dado fornecidos.'''
    def __dado_valido(self):
        for i in range (self.__tamanho()):
            if self.__numero[i] < '0' or self.__numero[i] > '9':
                return False
        return True
    
    '''Processo de conversão do tipo do dado, de str para int.'''
    def __converte_str_int(self):
        self.__numero = int(self.__numero)
    
    '''Método usado para a entrada de dados.'''
    def __entrada (self):
        '''Loop executado enquando o dado fornecido for inválido.'''
        while True:
            self.__numero = input('Digite um número inteiro positivo para convertê-lo em binário: ')
            time.sleep(3)
            os.system('cls')
            '''Caso o dado fornecido seja inválido, um a mensagem abaixo é exibida.'''
            if not self.__dado_valido():
                print('Você deve digitar um número inteiro positivo para convertê-lo em binário.')
                time.sleep(3)
                os.system('cls')
            else:
                return
    
    '''Conversão decimal - binário.'''
    def __conversao (self):
        '''Caso o número seja igual a 0 ou 1, o próprio número é apresentado como resultado.'''
        if self.__numero in (0,1):
            print(f'{self.__numero} no sistema decimal é igual a {self.__numero}',end='')
            print(' no sistema binário.')
            time.sleep(5)
            os.system('cls')
        
        #Se o número for maior que 1, o algoritmo de divisão é aplicado para realizar a conversão.
        else:
            dividendo = self.__numero
            divisor = 2
            valor = ''
            while dividendo + 1 >= divisor:
                quociente = dividendo // divisor
                resultado = quociente * divisor
                resto = dividendo - resultado
                dividendo = quociente
                
                '''Restos das divisões sucessivas.'''
                valor += str(resto)
            
            '''Processo de reversão dos restos para salvar o resultado.'''
            for i in range (len(valor), 0, -1):
                self.__resultado += valor[i - 1]
            
            '''Resultado da conversão.'''
            print(f'{self.__numero} no sistema decimal é igual a {self.__resultado}',end='')
            print(' no sistema binário.')
            self.__resultado = ''
            time.sleep(5)
            os.system('cls')

    '''Início do processo de conversão decimal - binário.'''        
    def iniciar(self):
        '''Chamada para o método de entrada de dados.'''
        self.__entrada()
        '''Conversão do tipo do dado, de str para int.'''
        self.__converte_str_int()
        '''Chamada para a conversão do número.'''
        self.__conversao()