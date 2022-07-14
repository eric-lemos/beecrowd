input_numbers = tuple(input().strip().split())
a = float(input_numbers[0])
b = float(input_numbers[1])
c = float(input_numbers[2])
pi = 3.14159

calc_a = float( (a * c) / 2)
calc_b = float( pi * (c * c) )
calc_c = float( ((a + b) * c) / 2)
calc_d = float( b * b )
calc_e = float( a * b )

print(f"TRIANGULO: {calc_a:.3f}")
print(f"CIRCULO: {calc_b:.3f}")
print(f"TRAPEZIO: {calc_c:.3f}")
print(f"QUADRADO: {calc_d:.3f}")
print(f"RETANGULO: {calc_e:.3f}")