from menu import Menu
from bindec import BinDec
from binhex import BinHex
from decbin import DecBin
from dechex import DecHex
from hexbin import HexBin
from hexdec import HexDec

class Main:

    def __init__(self):
        self.menu = Menu()
        self.bin_dec = BinDec()
        self.bin_hex = BinHex()
        self.dec_bin = DecBin()
        self.dec_hex = DecHex()
        self.hex_bin = HexBin()
        self.hex_dec = HexDec()
    
    def executar (self):
        
        while True:
            opcao = self.menu.exibir_menu()

            if opcao == 1:
                self.bin_dec.iniciar()
            
            elif opcao == 2:
                self.bin_hex.iniciar()
            
            elif opcao == 3:
                self.dec_bin.iniciar()
            
            elif opcao == 4:
                self.dec_hex.iniciar()
            
            elif opcao == 5:
                self.hex_bin.iniciar()
            
            elif opcao == 6:
                self.hex_dec.iniciar()

            else:
                return

main = Main()
main.executar()