# https://www.beecrowd.com.br/judge/pt/problems/view/1041
input_numbers = tuple(input().strip().split())
x = float(input_numbers[0])
y = float(input_numbers[1])

if(x > 0 and y > 0):
    print('Q1')

elif(x < 0 and y > 0):
    print('Q2')

elif(x < 0 and y < 0):
    print('Q3')

elif(x > 0 and y < 0):
    print('Q4')

elif(y == 0 and (x < 0 or x > 0)):
    print('Eixo X')

elif(x == 0 and (y < 0 or y > 0)):
    print('Eixo Y')

else:
    print('Origem')