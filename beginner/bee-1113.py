# https://www.beecrowd.com.br/judge/pt/problems/view/1113

while(True):
    numbers = list(map(int, input().strip().split()))
    x, y = numbers
    sum = 0
    
    if(x == y): break
    elif(x < y): print('Crescente')
    elif(x > y): print('Decrescente')