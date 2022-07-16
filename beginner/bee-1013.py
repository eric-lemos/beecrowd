# https://www.beecrowd.com.br/judge/pt/problems/view/1013
x, y, z = list(map(int, input().strip().split()))
higher = int(((x + y) + abs(x-y)) / 2)

if(z > higher): higher = z
print(f'{higher} eh o maior')