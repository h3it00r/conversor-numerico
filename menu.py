import time
import os

class Menu:

    def __init__(self) -> None:
        self.__opcao = None

    def exibir_menu (self):
            while True:
                try:
                    print('''CONVERSOR NUMÉRICO
                
Escolha o tipo de conversão que deseja fazer:

1 - Binário para decimal
2 - Binário para hexadecimal
3 - Decimal para binário
4 - Decimal para hexadecimal
5 - Hexadecimal para binário
6 - Hexadecimal para decimal
7 - Sair\n''')
                
                    self.__opcao = int(input ('Digite a sua opção: '))
                    
                    erro = False
            
                except ValueError:
                    erro = True
                    os.system('cls')
                    print('Opção inválida.')
                    time.sleep(3)
                    os.system('cls')

                if not erro:

                    if self.__opcao >= 1 and self.__opcao <= 7:
                        os.system('cls')
                        return self.__opcao
                    
                    else:
                        os.system('cls')
                        print('Opção inválida.')
                        time.sleep(3)
                        os.system('cls')