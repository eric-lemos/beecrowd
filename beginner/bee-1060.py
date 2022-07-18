# https://www.beecrowd.com.br/judge/pt/problems/view/1060
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

values = [a, b, c, d, e, f]
count_positive_numbers = 0

for item in values:
    if(item > 0):
        count_positive_numbers += 1

print(f'{count_positive_numbers} valores positivos')