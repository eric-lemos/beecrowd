# https://www.beecrowd.com.br/judge/pt/problems/view/1006

class Bee_1006:
    def init(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
    
    def inputs(self):
        self.n1 = float(input().strip())
        self.n2 = float(input().strip())
        self.n3 = float(input().strip())
        
    def calc(self):
        result = float(((self.n1*2) + (self.n2*3) + (self.n3*5)) / 10)
        print(f'MEDIA = {result:.1f}')
    
    def result(self):
        self.inputs()
        self.calc()

if(__name__  == '__main__'):
    bee = Bee_1006()
    bee.result()