# https://www.beecrowd.com.br/judge/pt/problems/view/1008

class Bee_1008:
    def init(self):
        self.employee = 0
        self.hours_worked = 0
        self.value_per_hour = 0
    
    def inputs(self):
        self.employee = int(input().strip())
        self.hours_worked = int(input().strip())
        self.value_per_hour = float(input().strip())
        
    def salary(self):
        salary = float(self.value_per_hour * self.hours_worked)
        print(f'NUMBER = {self.employee}')
        print(f'SALARY = U$ {salary:.2f}')
    
    def result(self):
        self.inputs()
        self.salary()

if(__name__  == '__main__'):
    bee = Bee_1008()
    bee.result()