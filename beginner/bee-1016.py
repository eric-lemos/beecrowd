# https://www.beecrowd.com.br/judge/pt/problems/view/1016

class Bee_1016:
    def __init__(self):
        self.distance = 0
        
    def inputs(self):
        self.distance = int(input().strip())

    def calc(self):
        x = self.distance * 2
        print(f'{x} minutos')

    def result(self):
        self.inputs()
        self.calc()

if(__name__ == '__main__'):
    bee = Bee_1016()
    bee.result()