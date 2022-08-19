# https://www.beecrowd.com.br/judge/pt/problems/view/1009

class Bee_1009:
    def init(self):
        self.seller_name = 0
        self.fixed_salary = 0
        self.sales_amount_month = 0
    
    def inputs(self):
        self.seller_name = str(input().strip())
        self.fixed_salary = float(input().strip())
        self.sales_amount_month = float(input().strip())
        
    def salary(self):
        salary = float(self.fixed_salary + ((self.sales_amount_month * 15) / 100))
        print(f'TOTAL = R$ {salary:.2f}')
    
    def result(self):
        self.inputs()
        self.salary()

if(__name__  == '__main__'):
    bee = Bee_1009()
    bee.result()