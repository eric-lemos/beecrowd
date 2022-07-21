# https://www.beecrowd.com.br/judge/pt/problems/view/1004

class Bee_1004:
    def init(self):
        self.n1 = 0
        self.n2 = 0
    
    def inputs(self):
        self.n1 = int(input().strip())
        self.n2 = int(input().strip())
        
    def calc(self):
        result = self.n1 * self.n2
        print(f'PROD = {result}')
    
    def result(self):
        self.inputs()
        self.calc()

if(__name__  == '__main__'):
    bee = Bee_1004()
    bee.result()