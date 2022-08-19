# https://www.beecrowd.com.br/judge/pt/problems/view/1035
a, b, c, d = list(map(int, input().strip().split()))

if((b > c) and (d > a) and (c + d) > (a + b) and 
   (c > 0) and (d > 0) and (a % 2) == 0): 
    print('Valores aceitos')
else: 
    print('Valores nao aceitos')