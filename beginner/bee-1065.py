# https://www.beecrowd.com.br/judge/pt/problems/view/1065
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

numbers = [a, b, c, d, e]
counter = 0

for number in numbers:
    if(number % 2 == 0):
        counter += 1

print(f'{counter} valores pares')