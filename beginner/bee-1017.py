# https://www.beecrowd.com.br/judge/pt/problems/view/1017

class Bee_1017:
    def __init__(self):
        self.avg_speed = 0
        self.travel_time = 0
        
    def inputs(self):
        self.avg_speed = int(input().strip())
        self.travel_time = int(input().strip())

    def calc(self):
        distance = float((self.avg_speed * self.travel_time) / 12)
        print(f'{(distance):0.3f}')

    def result(self):
        self.inputs()
        self.calc()

if(__name__ == '__main__'):
    bee = Bee_1017()
    bee.result()