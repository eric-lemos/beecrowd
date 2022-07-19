# https://www.beecrowd.com.br/judge/pt/problems/view/1064

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

numbers = [a, b, c, d, e, f]
count_positive_numbers = 0
avg_positive_numbers = 0

for number in numbers:
    if(number > 0):
        count_positive_numbers += 1
        avg_positive_numbers += number

print(f'{count_positive_numbers} valores positivos')
print(f'{avg_positive_numbers/count_positive_numbers:.1f}')