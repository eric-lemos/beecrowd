# https://www.beecrowd.com.br/judge/pt/problems/view/1043
inputs = list(map(float, input().strip().split()))
x, y, z = inputs[:]
inputs.sort()

if((inputs[0] + inputs[1]) > inputs[2]):
    result1 = x + y + z
    print(f'Perimetro = {result1:.1f}')
else:
    result2 = ((x + y) * z) / 2
    print(f'Area = {result2:.1f}')