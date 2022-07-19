# https://www.beecrowd.com.br/judge/pt/problems/view/1066
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

numbers = [a, b, c, d, e]
even, odd, positive, negative = [0, 0, 0, 0]

for number in numbers:
    if(number % 2 == 0):
        even += 1
        
    elif(number % 2 != 0):
        odd += 1
    
    if(number > 0):
        positive += 1
        
    elif(number < 0):
        negative += 1

print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{positive} valor(es) positivo(s)')
print(f'{negative} valor(es) negativo(s)')