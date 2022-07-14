# https://www.beecrowd.com.br/judge/pt/problems/view/1005
p1 = 3.5
p2 = 7.5

a = float(input())
b = float(input())
media = float( ((a * p1) + (b * p2)) / (p1 + p2) ) 

print(f'MEDIA = {media:.5f}')