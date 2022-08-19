# https://www.beecrowd.com.br/judge/pt/problems/view/1007

class Bee_1007:
    def init(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
    
    def inputs(self):
        self.n1 = int(input().strip())
        self.n2 = int(input().strip())
        self.n3 = int(input().strip())
        self.n4 = int(input().strip())
        
    def calc(self):
        result = (self.n1 * self.n2) - (self.n3 * self.n4)
        print(f'DIFERENCA = {result}')
    
    def result(self):
        self.inputs()
        self.calc()

if(__name__  == '__main__'):
    bee = Bee_1007()
    bee.result()