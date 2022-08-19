# https://www.beecrowd.com.br/judge/pt/problems/view/1013

class Bee_1013:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        
    def inputs(self):
        self.n1, self.n2, self.n3 = list(map(int, input().strip().split()))

    def higher(self):
        return int(((self.n1 + self.n2) + abs(self.n1 - self.n2)) / 2)

    def check(self):
        higher = self.higher()
        if(self.n3 > higher): higher = self.n3
        print(f'{higher} eh o maior')

    def result(self):
        self.inputs()
        self.check()

if(__name__ == '__main__'):
    bee = Bee_1013()
    bee.result()