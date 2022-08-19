# https://www.beecrowd.com.br/judge/pt/problems/view/1002

class Bee_1002:
    def __init__(self):
        self._pi = 3.14159
        self.r = 0
        
    def inputs(self):
        self.r = float(input().strip())
    
    def calc(self):
        result = self._pi * (self.r * self.r)
        print(f'A={result:.4f}')
        
    def result(self):
        self.inputs()
        self.calc()

if(__name__ == '__main__'):
    bee = Bee_1002()
    bee.result()