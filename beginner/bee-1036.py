# https://www.beecrowd.com.br/judge/pt/problems/view/1036
input_numbers = tuple(input().strip().split())
a = float(input_numbers[0])
b = float(input_numbers[1])
c = float(input_numbers[2])
d = (b * b) - (4 * a * c)

if(d < 0 or a == 0):
    print('Impossivel calcular')
else:
    r1 = (-b + d ** (0.5)) / (2 * a)
    r2 = (-b - d ** (0.5)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')