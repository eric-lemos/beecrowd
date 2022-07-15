data = list(map(float, input().strip().split()))
a, b, c = data[:]
data.sort()

if((data[0] + data[1]) > data[2]):
    p = a + b + c
    print(f'Perimetro = {p:.1f}')
else:
    area = ((a + b) * c) / 2
    print(f'Area = {area:.1f}')