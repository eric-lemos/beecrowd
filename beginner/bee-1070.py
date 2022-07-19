# https://www.beecrowd.com.br/judge/pt/problems/view/1070
x, y = [int(input()), 0]

if(x % 2 == 0): y = 11
elif(x % 2 != 0): y = 10

for i in range(x, (x+y+1)):
    if(i % 2 != 0):
        print(i)