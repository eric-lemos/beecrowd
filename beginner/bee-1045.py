# https://www.beecrowd.com.br/judge/pt/problems/view/1045
inputs = list(map(float, input().strip().split()))
inputs.sort(reverse=True)
a, b, c = inputs

if(a >= (b + c)): print('NAO FORMA TRIANGULO')
else:
    if((a ** 2) == ((b ** 2) + (c ** 2))):
        print('TRIANGULO RETANGULO') 
    if((a ** 2) > ((b ** 2) + (c ** 2))):
        print('TRIANGULO OBTUSANGULO')  
    if((a ** 2) < ((b ** 2) + (c ** 2))):
        print('TRIANGULO ACUTANGULO')
    if(a == b and a == c):
        print('TRIANGULO EQUILATERO') 
    if( (a == b and a != c) or 
        (a == c and a != b) or 
        (b == c and b != a) ):
        print('TRIANGULO ISOSCELES')