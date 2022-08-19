# https://www.beecrowd.com.br/judge/pt/problems/view/1010

class Bee_1010:
    def init(self):
        self.item_1 = []
        self.item_1 = []
    
    def inputs(self):
        self.item_1 = list(input().strip().split())
        self.item_2 = list(input().strip().split())
        
    def total(self):
        x, n1, n2 = self.item_1
        y, n3, n4 = self.item_2
        total = float((float(n2) * int(n1)) + (float(n4) * int(n3)))
        print(f'VALOR A PAGAR: R$ {total:.2f}')
    
    def result(self):
        self.inputs()
        self.total()

if(__name__  == '__main__'):
    bee = Bee_1010()
    bee.result()