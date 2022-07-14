# https://www.beecrowd.com.br/judge/pt/problems/view/1008
employee = int(input())
hours_worked = int(input())
value_per_hour = float(input())
salary = float(value_per_hour * hours_worked)

print(f'NUMBER = {employee}')
print(f'SALARY = U$ {salary:.2f}')