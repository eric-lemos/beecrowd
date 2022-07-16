# https://www.beecrowd.com.br/judge/pt/problems/view/1015
x1, y1 = list(map(float, input().strip().split()))
x2, y2 = list(map(float, input().strip().split()))

result = float(( ((x2-x1) * (x2-x1)) + ((y2-y1) * (y2-y1)) ) ** (0.5))
print(f'{result:.4f}')