# https://www.beecrowd.com.br/judge/pt/problems/view/1048
x = round(float(input()), 2)

if(x > 0 and x <= 400): percentage = 15
elif(x > 400 and x <= 800): percentage = 12
elif(x > 800 and x <= 1200): percentage = 10
elif(x > 1200 and x <= 2000): percentage = 7
elif(x > 2000): percentage = 4

salary = (x + ((x * percentage) / 100))
readjustment = ((x * percentage) / 100)

print(f'Novo salario: {salary:.2f}')
print(f'Reajuste ganho: {readjustment:.2f}')
print(f'Em percentual: {percentage} %')