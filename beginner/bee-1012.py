# https://www.beecrowd.com.br/judge/pt/problems/view/1012

class Bee_1011:
    def __init__(self):
        self._pi = 3.14159
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        
    def inputs(self):
        self.n1, self.n2, self.n3 = list(map(float, input().strip().split()))
    
    def calcs(self):
        print(f'TRIANGULO: {float((self.n1 * self.n3) / 2):.3f}')
        print(f'CIRCULO: {float(self._pi * (self.n3 ** 2)):.3f}')
        print(f'TRAPEZIO: {float(((self.n1 + self.n2) * self.n3) / 2):.3f}')
        print(f'QUADRADO: {float(self.n2 ** 2):.3f}')
        print(f'RETANGULO: {float(self.n1 * self.n2):.3f}')
        
    def result(self):
        self.inputs()
        self.calcs()

if(__name__ == '__main__'):
    bee = Bee_1011()
    bee.result()