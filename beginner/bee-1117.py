# https://www.beecrowd.com.br/judge/pt/problems/view/1117

count = 0
result = 0

while(count != 2):
    x = float(input().strip())
    
    if(x >= 0 and x <= 10): 
        result += x
        count += 1
    else: print('nota invalida')

print(f'media = {result/2:.2f}')