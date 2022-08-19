# https://www.beecrowd.com.br/judge/pt/problems/view/1014

class Bee_1014:
    def init(self):
        self.distance = 0
        self.gasoline = 0
    
    def inputs(self):
        self.distance = float(input().strip())
        self.gasoline = float(input().strip())
        
    def average(self):
        average = float(self.distance / self.gasoline)
        print(f'{average:.3f} km/l')
    
    def result(self):
        self.inputs()
        self.average()

if(__name__  == '__main__'):
    bee = Bee_1014()
    bee.result()