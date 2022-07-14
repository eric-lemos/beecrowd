# https://www.beecrowd.com.br/judge/pt/problems/view/1035
input_numbers = tuple(input().strip().split())

a = int(input_numbers[0])
b = int(input_numbers[1])
c = int(input_numbers[2])
d = int(input_numbers[3])

if((b > c) and (d > a) and (c + d) > (a + b) and 
   (c > 0) and (d > 0) and (a % 2) == 0): 
    print('Valores aceitos')
else: 
    print('Valores nao aceitos')