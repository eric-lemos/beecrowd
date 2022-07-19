# https://www.beecrowd.com.br/judge/pt/problems/view/1079

n = int(input())

while(n > 0):
    x = list(map(float, input().strip().split()))
    result = ((x[0] * 2) + (x[1] * 3) + (x[2] * 5)) / (2 + 3 + 5)
    print(f'{result:.1f}')
    n -= 1