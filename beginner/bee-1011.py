# https://www.beecrowd.com.br/judge/pt/problems/view/1011

class Bee_1011:
    def __init__(self):
        self._pi = 3.14159
        self.r = 0
        
    def inputs(self):
        self.r = float(input().strip())
    
    def calc(self):
        result = float((4 * self._pi * (self.r ** 3)) / 3)
        print(f'VOLUME = {result:.3f}')
        
    def result(self):
        self.inputs()
        self.calc()

if(__name__ == '__main__'):
    bee = Bee_1011()
    bee.result()