#calculadora
class Calc:
    
    def __init__(self):
        print("1- Somar \n2- Subtrair \n3- Multiplicar \n4- Dividir ")
        op=int(input('Escolha uma op: '))
        if op==1:
            self.somar()
        elif op==2:
            self.subtrair()
        elif op==3:
            self.multiplicar()
        elif op==4:
            self.dividir()
        else:
            print('Op inválida')

    def somar(self):
        n1=float(input('Digite o numb 1: '))
        n2=float(input('Digite o numb 2: '))
        return print('O resultado é',n1 + n2)

    def subtrair(self):
        n1=float(input('Digite o numb 1: '))
        n2=float(input('Digite o numb 2: '))
        return print('O resultado é',n1 - n2)

    def multiplicar(self):
        n1=float(input('Digite o numb 1: '))
        n2=float(input('Digite o numb 2: '))
        return print('O resultado é',n1 * n2)

    def dividir(self):
        n1=float(input('Digite o numb 1: '))
        n2=float(input('Digite o numb 2: '))
        return print('O resultado é',n1 / n2)

while True:
    Calc()