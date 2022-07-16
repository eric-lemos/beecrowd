# https://www.beecrowd.com.br/judge/pt/problems/view/1012
x, y, z = list(map(float, input().strip().split()))

result1 = float((x * z) / 2)
result2 = float(3.14159 * (z * z))
result3 = float(((x + y) * z) / 2)
result4 = float(y * y)
result5 = float(x * y)

print(f"TRIANGULO: {result1:.3f}")
print(f"CIRCULO: {result2:.3f}")
print(f"TRAPEZIO: {result3:.3f}")
print(f"QUADRADO: {result4:.3f}")
print(f"RETANGULO: {result5:.3f}")