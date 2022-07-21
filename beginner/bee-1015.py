# https://www.beecrowd.com.br/judge/pt/problems/view/1015

class Bee_1015:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        
    def inputs(self):
        self.x1, self.y1 = list(map(float, input().strip().split()))
        self.x2, self.y2 = list(map(float, input().strip().split()))

    def calc(self):
        result = float((((self.x2-self.x1) * (self.x2-self.x1)) + ((self.y2-self.y1) * (self.y2-self.y1))) ** (0.5))
        print(f'{result:.4f}')

    def result(self):
        self.inputs()
        self.calc()

if(__name__ == '__main__'):
    bee = Bee_1015()
    bee.result()