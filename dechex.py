import time
import os

class DecHex:

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
            self.__numero = input('Digite um número inteiro positivo para convertê-lo em hexadecimal: ')
            time.sleep(3)
            os.system('cls')
            '''Caso o dado fornecido seja inválido, um a mensagem abaixo é exibida.'''
            if not self.__dado_valido():
                print('Você deve digitar um número inteiro positivo para convertê-lo em hexadecimal.')
                time.sleep(3)
                os.system('cls')
            else:
                return
            
    '''Dicionário usado para fazer a conversão numérica.'''
    def __dicionario_dec_hex (self, numero):
        num = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 
               9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        return num[numero]
    
    '''Conversão decimal - hexadecimal.'''
    def __conversao (self):
        if self.__numero >= 0 and self.__numero <= 15:
            self.__resultado = self.__dicionario_dec_hex(self.__numero)
            print(f'{self.__numero} no sistema decimal é igual a {self.__resultado}',end='')
            print(' no sistema hexadecimal.')
            self.__resultado = ''
            time.sleep(5)
            os.system('cls')
        
        #Se o número for maior que 15, o algoritmo de divisão é aplicado para realizar a conversão.
        else:
            dividendo = self.__numero
            divisor = 16
            valor = ''
            cont = 0
            while True:
                quociente = dividendo // divisor
                resultado = quociente * divisor
                resto = dividendo - resultado
                dividendo = quociente

                if dividendo == resto:
                    cont += 1

                if cont == 2:
                    break

                '''Restos das divisões sucessivas.'''
                valor += self.__dicionario_dec_hex(resto)
            
            '''Formatação dos restos para o resultado.'''
            if valor[-1] == '0':
                valor = valor [:-1]

            '''Processo de reversão dos restos para salvar o resultado.'''
            for i in range (len(valor), 0, -1):
                    self.__resultado += valor[i - 1]
            
            '''Resultado da conversão.'''
            print(f'{self.__numero} no sistema decimal é igual a {self.__resultado}',end='')
            print(' no sistema hexadecimal.')
            self.__resultado = ''
            time.sleep(5)
            os.system('cls')

    '''Início do processo de conversão decimal - hexadecimal.'''        
    def iniciar(self):
        '''Chamada para o método de entrada de dados.'''
        self.__entrada()
        '''Conversão do tipo do dado, de str para int.'''
        self.__converte_str_int()
        '''Chamada para a conversão do número.'''
        self.__conversao()