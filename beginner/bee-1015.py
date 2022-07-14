values1 = tuple(input().strip().split())
values2 = tuple(input().strip().split())

x1 = float(values1[0])
x2 = float(values2[0])
y1 = float(values1[1])
y2 = float(values2[1])

calc = float( (((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1))) ** (0.5) )
print(f'{calc:.4f}')