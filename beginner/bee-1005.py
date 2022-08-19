# https://www.beecrowd.com.br/judge/pt/problems/view/1005

class Bee_1005:
    def init(self):
        self.n1 = 0
        self.n2 = 0
    
    def inputs(self):
        self.n1 = float(input().strip())
        self.n2 = float(input().strip())
        
    def calc(self):
        result = float(((self.n1*3.5) + (self.n2*7.5)) / 11) 
        print(f'MEDIA = {result:.5f}')
    
    def result(self):
        self.inputs()
        self.calc()

if(__name__  == '__main__'):
    bee = Bee_1005()
    bee.result()